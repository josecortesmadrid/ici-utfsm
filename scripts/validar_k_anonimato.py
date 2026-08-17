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

# Las dimensiones que definen una celda. Cruzarlas es lo que puede identificar.
DIMENSIONES = ["promocion", "pais", "industria", "nivel", "experiencia"]

# Columnas que jamas deben existir en el CSV, ni vacias.
PROHIBIDAS = {
    "nombre", "apellido", "email", "correo", "telefono", "fono",
    "empleador", "empresa", "compania", "linkedin", "rut", "url",
    "renta_exacta", "sueldo_exacto", "salario",
}


def cargar(ruta: Path) -> list[dict]:
    with ruta.open(encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh))


def revisar_columnas(campos: list[str]) -> list[str]:
    """Ninguna columna puede ser identificante, aunque venga vacia."""
    return [c for c in campos if c.strip().lower() in PROHIBIDAS]


def celdas(filas: list[dict], dims: list[str]) -> Counter:
    return Counter(tuple(f.get(d, "").strip() for d in dims) for f in filas)


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
        print("  OK — archivo sin filas.")
        return 0

    problemas = []

    malas = revisar_columnas(list(filas[0].keys()))
    if malas:
        problemas.append(f"columnas prohibidas presentes: {', '.join(malas)}")

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
            print(f"    n={n}  {' · '.join(x or '(vacio)' for x in c)}")
        problemas.append(f"{len(bajo)} celda(s) bajo el umbral k={args.k}")

    print()
    if problemas:
        print("  FALLA — no se puede publicar:")
        for p in problemas:
            print(f"    - {p}")
        print()
        print("  El umbral no se baja. Si quieres publicar esa celda, junta mas filas.")
        return 1

    print("  OK — todas las celdas cumplen el umbral.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
