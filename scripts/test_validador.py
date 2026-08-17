#!/usr/bin/env python3
"""Test adversarial del validador de k-anonimato.

POR QUE EXISTE
--------------
`verificar.sh` corria `validar_k_anonimato.py atlas/datos.csv` y lo daba verde.
Pero `atlas/datos.csv` no existe todavia, asi que el validador retornaba 0 con
"Atlas vacio, nada que validar". Ese verde no decia NADA sobre si el validador
funciona: el chequeo de mayor riesgo del repo pasaba de forma vacua.

Un validador de privacidad que solo se prueba contra datos que no existen es
una promesa, no una garantia. Este archivo le pasa casos cuya respuesta ya
conocemos — la unica forma de saber si un instrumento mide.

Corre en verificar.sh. Si falla, no se publica nada.

HALLAZGO QUE MOTIVO EL CASO 8 (2026-08-16)
------------------------------------------
El validador aceptaba una columna `ciudad` no declarada: agrupaba solo por
pais/industria/nivel, veia n=5, e imprimia "todas las celdas cumplen el
umbral" — publicando una tabla donde cada fila era UNA persona identificable.
k=1 real, con el reporte diciendo k=5.

Modo de falla clasico del k-anonimato: un cuasi-identificador no declarado.
La defensa era una lista negra, y una lista negra siempre pierde contra la
columna que nadie penso. Se cambio a lista blanca (PERMITIDAS).

Uso:
    python scripts/test_validador.py
"""
import subprocess
import sys
import tempfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
VALIDADOR = RAIZ / "scripts" / "validar_k_anonimato.py"

# (nombre, csv, debe_rechazar, por_que_importa)
CASOS = [
    (
        "celda bajo umbral (n=3)",
        "pais,industria,nivel,n\nChile,Mineria,Senior,3\nChile,Mineria,Junior,9\n",
        True,
        "3 < 5: la celda identifica a tres personas",
    ),
    (
        "celda justo en el umbral (n=5)",
        "pais,industria,nivel,n\nChile,Mineria,Senior,5\n",
        False,
        "5 >= 5 cumple; el borde no se corre para ningun lado",
    ),
    (
        "columna prohibida (empleador)",
        "pais,industria,nivel,n,empleador\nChile,Mineria,Senior,9,Codelco\n",
        True,
        "empleador asociado a personas",
    ),
    (
        "columna prohibida con mayusculas y espacios",
        "pais,industria,nivel,n, Empleador \nChile,Mineria,Senior,9,Codelco\n",
        True,
        "no debe escaparse por diferencia de formato",
    ),
    (
        "cruce fino prohibido (promocion)",
        "pais,industria,nivel,promocion,n\nChile,Mineria,Senior,2015,9\n",
        True,
        "promocion cruzada con las tres dimensiones = cuasi-identificador",
    ),
    (
        "formato padron (sin columna n)",
        "pais,industria,nivel\nChile,Mineria,Senior\nChile,Mineria,Senior\n",
        True,
        "una fila por persona es cuasi-identificador aunque no lleve nombres",
    ),
    (
        "agregado valido",
        "pais,industria,nivel,n\nChile,Mineria,Senior,12\nCanada,Energia,Senior,7\n",
        False,
        "todas las celdas >= 5: este es el caso que SI se publica",
    ),
    (
        "columna no declarada (ciudad) — el hueco de 2026-08-16",
        "pais,industria,nivel,ciudad,n\n"
        "Chile,Mineria,Senior,Calama,1\n"
        "Chile,Mineria,Senior,Antofagasta,1\n"
        "Chile,Mineria,Senior,Santiago,1\n"
        "Chile,Mineria,Senior,Iquique,1\n"
        "Chile,Mineria,Senior,Rancagua,1\n",
        True,
        "suma n=5 en la celda de tres dimensiones, pero cada ciudad tiene UNA "
        "persona: el reporte diria k>=5 publicando k=1",
    ),
    (
        "esquema completo del README",
        "pais,industria,nivel,n,banda_renta_usd,fecha_corte\n"
        "Chile,Mineria,Senior,8,80-100k,2026-08\n",
        False,
        "el esquema que atlas/README.md publica tiene que pasar",
    ),
]


def main() -> int:
    if not VALIDADOR.exists():
        print("  FALLA - no existe scripts/validar_k_anonimato.py")
        return 1

    tmp = Path(tempfile.mkdtemp())
    huecos = []

    for nombre, contenido, debe_rechazar, porque in CASOS:
        f = tmp / "datos.csv"
        f.write_text(contenido, encoding="utf-8")
        p = subprocess.run(
            [sys.executable, str(VALIDADOR), str(f)],
            capture_output=True,
            cwd=str(RAIZ),
        )
        rechazo = p.returncode != 0
        if rechazo == debe_rechazar:
            print(f"  OK    {nombre}")
        else:
            esperado = "RECHAZA" if debe_rechazar else "acepta"
            obtenido = "RECHAZA" if rechazo else "acepta"
            print(f"  HUECO {nombre}")
            print(f"        esperado {esperado}, obtuvo {obtenido}")
            print(f"        {porque}")
            huecos.append(nombre)

    print()
    if huecos:
        print(f"  FALLA - {len(huecos)} hueco(s) en la garantia de privacidad.")
        print("  El repo es PUBLICO. No se publica nada hasta cerrarlos.")
        return 1
    print(f"  OK - los {len(CASOS)} casos adversariales se comportan como corresponde.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
