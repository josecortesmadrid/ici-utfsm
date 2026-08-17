#!/usr/bin/env python3
"""Valida k-anonimato sobre los datos del Atlas.

La regla de PRIVACIDAD.md: ninguna celda con menos de K personas se publica.
Este script la hace cumplir. Corre en cada PR y bloquea el merge si falla.

Uso:
    python scripts/validar_k_anonimato.py atlas/datos.csv
    python scripts/validar_k_anonimato.py atlas/datos.csv --k 5

Salida: 0 si todo cumple, 1 si hay celdas bajo umbral o columnas prohibidas.

Por que existe: una regla de privacidad que depende de que un humano se
acuerde de revisarla ya fallo, solo que todavia no te enteraste.
"""

import argparse
import csv
import sys
from collections import Counter
from pathlib import Path

K_DEFAULT = 5

# Las dimensiones de publicacion. Son TRES, no cinco, y es a proposito:
# el probe de masa critica midio que cruzar 5 exige 246 filas en el escenario
# realista contra 77 con 3. Ademas, cruzar 5 atributos en una cohorte chica
# convierte el agregado en un cuasi-identificador.
# Promocion y experiencia se publican por separado, nunca cruzadas con estas.
DIMENSIONES = ["pais", "industria", "nivel"]

# Si aparecen en el CSV, es que alguien intento publicar el cruce fino.
CRUCE_PROHIBIDO = {"promocion", "experiencia"}

# Columnas que jamas deben existir en el CSV, ni vacias.
PROHIBIDAS = {
    "nombre", "apellido", "email", "correo", "telefono", "fono",
    "empleador", "empresa", "compania", "linkedin", "rut", "url",
    "renta_exacta", "sueldo_exacto", "salario",
}

# LISTA BLANCA: el esquema completo y cerrado que atlas/README.md publica.
# Cualquier columna fuera de esto se rechaza, aunque parezca inofensiva.
#
# Por que lista blanca y no solo la negra de arriba:
# el test adversarial del 2026-08-16 metio una columna 'ciudad' con cinco filas
# Chile/Mineria/Senior, una por ciudad. El validador agrupaba solo por las tres
# DIMENSIONES, veia n=5, e imprimia "todas las celdas cumplen el umbral" —
# publicando una tabla donde cada fila era UNA persona identificable. k=1 real
# con el reporte diciendo k=5.
#
# Ese es el modo de falla clasico del k-anonimato: un cuasi-identificador que
# nadie declaro. Una lista negra siempre pierde contra la columna que nadie
# penso (ciudad, cargo, universidad, anio_titulacion, genero...). La lista
# blanca invierte la carga de la prueba: para agregar una columna hay que
# declararla acá y en atlas/README.md, y pensar que le hace al umbral.
PERMITIDAS = set(DIMENSIONES) | {"n", "banda_renta_usd", "fecha_corte"}


def cargar(ruta: Path) -> list[dict]:
    with ruta.open(encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh))


def revisar_columnas(campos: list[str]) -> list[str]:
    """Ninguna columna puede ser identificante, aunque venga vacia."""
    return [c for c in campos if c.strip().lower() in PROHIBIDAS]


def celdas(filas: list[dict], dims: list[str]) -> Counter:
    """Cuenta personas por celda.

    Formato agregado (el correcto): una fila por celda con columna 'n'.
    Formato padron (una fila por persona): se cuenta, pero se advierte —
    un CSV con una fila por persona es un cuasi-identificador aunque no
    lleve nombres.
    """
    c: Counter = Counter()
    for f in filas:
        celda = tuple(f.get(d, "").strip() for d in dims)
        if "n" in f:
            try:
                c[celda] += int(str(f["n"]).strip() or 0)
            except ValueError:
                c[celda] += 0
        else:
            c[celda] += 1
    return c


def main() -> int:
    ap = argparse.ArgumentParser(description="Valida k-anonimato del Atlas")
    ap.add_argument("csv", type=Path)
    ap.add_argument("--k", type=int, default=K_DEFAULT)
    args = ap.parse_args()

    if not args.csv.exists():
        # Atlas vacio es un estado valido: todavia nadie aporto.
        print(f"  {args.csv} no existe todavia - Atlas vacio, nada que validar.")
        print("  OK (0 filas, 0 celdas publicables)")
        return 0

    filas = cargar(args.csv)
    if not filas:
        print("  OK - archivo sin filas.")
        return 0

    problemas = []

    campos = list(filas[0].keys())

    malas = revisar_columnas(campos)
    if malas:
        problemas.append(f"columnas prohibidas presentes: {', '.join(malas)}")

    # Lista blanca: toda columna no declarada es un cuasi-identificador potencial.
    # Se evalua antes que el umbral, porque una columna extra hace que el conteo
    # por celda mida algo distinto de lo que el reporte dice medir.
    no_declaradas = [
        c for c in campos
        if c.strip().lower() not in PERMITIDAS
        and c.strip().lower() not in PROHIBIDAS
        and c.strip().lower() not in CRUCE_PROHIBIDO
    ]
    if no_declaradas:
        problemas.append(
            f"columnas no declaradas: {', '.join(no_declaradas)} - el esquema es "
            f"{'/'.join(sorted(PERMITIDAS))}. Una columna extra subdivide cada celda "
            f"sin que el conteo lo refleje: el reporte diria k>={args.k} publicando k=1"
        )

    cruce = [c for c in campos if c.strip().lower() in CRUCE_PROHIBIDO]
    if cruce:
        problemas.append(
            f"cruce fino prohibido: {', '.join(cruce)} no se publica junto a "
            f"{'/'.join(DIMENSIONES)} - se publica por separado"
        )

    if "n" not in campos:
        problemas.append(
            "falta la columna 'n' - el Atlas se publica agregado (una fila = "
            "una celda con su conteo), no como padron de una fila por persona"
        )

    dims = [d for d in DIMENSIONES if d in filas[0]]
    faltantes = set(DIMENSIONES) - set(dims)
    if faltantes:
        problemas.append(f"faltan dimensiones esperadas: {', '.join(sorted(faltantes))}")

    conteo = celdas(filas, dims) if dims else Counter()
    bajo = {c: n for c, n in conteo.items() if n < args.k}

    print(f"  filas totales        : {len(filas)}")
    print(f"  celdas distintas     : {len(conteo)}")
    print(f"  publicables (n>={args.k}) : {len(conteo) - len(bajo)}")
    print(f"  bajo umbral          : {len(bajo)}")

    if bajo:
        print()
        print(f"  Estas celdas NO se pueden publicar (menos de {args.k} personas):")
        for c, n in sorted(bajo.items(), key=lambda kv: kv[1], reverse=True):
            print(f"    n={n}  {' | '.join(x or '(vacio)' for x in c)}")
        problemas.append(f"{len(bajo)} celda(s) bajo el umbral k={args.k}")

    print()
    if problemas:
        print("  FALLA - no se puede publicar:")
        for p in problemas:
            print(f"    - {p}")
        print()
        print("  El umbral no se baja. Si quieres publicar esa celda, junta mas filas.")
        return 1

    print("  OK - todas las celdas cumplen el umbral.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
