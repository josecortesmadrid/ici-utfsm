#!/usr/bin/env python3
"""Probe: cuantas filas necesita el Atlas para publicar su primera celda.

Por que existe: el README del Atlas afirmaba "del orden de 40 a 60 filas".
Ese numero se escribio sin calcularlo. Esto lo calcula.

Metodo: Monte Carlo. Se sortean contribuyentes desde marginales plausibles
sobre las 5 dimensiones que definen una celda, y se cuenta cuantos hacen
falta hasta que alguna celda llega a k=5.

El test esta SESGADO A FAVOR de la hipotesis: el escenario "optimista"
concentra la red mucho mas de lo realista (una sola promocion domina, un
solo pais, una sola industria). Si la hipotesis muere incluso ahi, esta
muerta de verdad y la incertidumbre de parametros no la salva.

Uso:
    python scripts/probe_masa_critica.py
    python scripts/probe_masa_critica.py --k 5 --sims 2000
"""

import argparse
import random
from collections import Counter

# --- Marginales por escenario ---------------------------------------------
# Cada dimension es una lista de (valor, peso). Los pesos no necesitan sumar 1.
#
# OPTIMISTA: la red es un clan - casi todos de las mismas 2 promociones,
# en Chile, en mineria. Es deliberadamente irreal, a favor de H.
# REALISTA: concentracion moderada, como se ve en redes de egresados.
# DISPERSO: la red logra atraer variedad, que es lo que uno querria.

ESCENARIOS = {
    "optimista": {
        "promocion":   [("2005-2009", 55), ("2010-2014", 30), ("2000-2004", 15)],
        "pais":        [("Chile", 80), ("Canada", 15), ("EEUU", 5)],
        "industria":   [("Mineria", 60), ("Consultoria", 25), ("Energia", 15)],
        "nivel":       [("Jefatura", 45), ("Subgerencia", 30), ("Gerencia", 25)],
    },
    "realista": {
        "promocion":   [("1995-1999", 8), ("2000-2004", 15), ("2005-2009", 22),
                        ("2010-2014", 25), ("2015-2019", 20), ("2020-2024", 10)],
        "pais":        [("Chile", 55), ("Canada", 12), ("EEUU", 12),
                        ("Australia", 5), ("LatAm", 10), ("Europa", 6)],
        "industria":   [("Mineria", 25), ("Consultoria", 18), ("Banca", 12),
                        ("Tecnologia", 12), ("Energia", 10), ("Retail", 8),
                        ("Logistica", 7), ("Manufactura", 8)],
        "nivel":       [("Analista", 20), ("Jefatura", 30), ("Subgerencia", 20),
                        ("Gerencia", 20), ("Direccion", 10)],
    },
    "disperso": {
        "promocion":   [(f"p{i}", 1) for i in range(8)],
        "pais":        [(f"c{i}", 1) for i in range(7)],
        "industria":   [(f"i{i}", 1) for i in range(12)],
        "nivel":       [(f"n{i}", 1) for i in range(7)],
    },
}

# experiencia esta casi determinada por promocion (correlacion ~0.9).
# Modelarla como libre inflaria artificialmente el espacio de celdas, o sea
# que tratarla como determinada tambien favorece a H.
def experiencia_de(promocion: str) -> str:
    return f"exp({promocion})"


def sortear(marginal):
    vals = [v for v, _ in marginal]
    pesos = [w for _, w in marginal]
    return random.choices(vals, weights=pesos, k=1)[0]


def simular(esc: dict, k: int, dims: list[str], tope: int) -> int | None:
    """Devuelve cuantos contribuyentes hicieron falta hasta la primera celda k."""
    celdas: Counter = Counter()
    for n in range(1, tope + 1):
        fila = {d: sortear(esc[d]) for d in esc}
        fila["experiencia"] = experiencia_de(fila["promocion"])
        celda = tuple(fila[d] for d in dims)
        celdas[celda] += 1
        if celdas[celda] >= k:
            return n
    return None


def correr(nombre: str, esc: dict, k: int, sims: int, dims: list[str], tope: int):
    res = [simular(esc, k, dims, tope) for _ in range(sims)]
    logrados = sorted(r for r in res if r is not None)
    fallidos = len(res) - len(logrados)
    if not logrados:
        print(f"  {nombre:11s} NUNCA llego a k={k} en {tope} filas ({sims} sims)")
        return None
    mediana = logrados[len(logrados) // 2]
    p90 = logrados[int(len(logrados) * 0.9)]
    nota = f"  ({fallidos}/{sims} sims no llegaron en {tope})" if fallidos else ""
    print(f"  {nombre:11s} mediana={mediana:4d} filas   p90={p90:4d}{nota}")
    return mediana


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--k", type=int, default=5)
    ap.add_argument("--sims", type=int, default=2000)
    ap.add_argument("--tope", type=int, default=20000)
    args = ap.parse_args()
    random.seed(42)  # reproducible: cualquiera obtiene estos mismos numeros

    print()
    print(f"  PROBE - filas necesarias para la primera celda con k>={args.k}")
    print(f"  {args.sims} simulaciones por escenario, semilla fija.")
    print()

    dims5 = ["promocion", "pais", "industria", "nivel", "experiencia"]
    dims3 = ["pais", "industria", "nivel"]

    print("  [A] Diseno publicado - 5 dimensiones")
    print("      promocion x pais x industria x nivel x experiencia")
    m5 = {}
    for nombre, esc in ESCENARIOS.items():
        m5[nombre] = correr(nombre, esc, args.k, args.sims, dims5, args.tope)

    print()
    print("  [B] Alternativa - 3 dimensiones (se sueltan promocion y experiencia)")
    print("      pais x industria x nivel")
    m3 = {}
    for nombre, esc in ESCENARIOS.items():
        m3[nombre] = correr(nombre, esc, args.k, args.sims, dims3, args.tope)

    # --- Veredicto contra el kill criterion declarado antes de correr ------
    print()
    print("  " + "-" * 62)
    UMBRAL = 120  # 2x el techo publicado (40-60). Declarado ANTES de correr.
    opt5 = m5.get("optimista")
    print(f"  KILL CRITERION (declarado antes): H1 muere si el escenario")
    print(f"  OPTIMISTA con 5 dimensiones exige mas de {UMBRAL} filas.")
    print()
    if opt5 is None:
        print(f"  VEREDICTO: H1 REFUTADA - ni siquiera converge.")
        return 1
    if opt5 > UMBRAL:
        print(f"  VEREDICTO: H1 REFUTADA. Optimista exige {opt5} filas, no 40-60.")
        print(f"             El numero publicado esta {opt5/50:.0f}x subestimado.")
        return 1
    print(f"  VEREDICTO: H1 SOBREVIVE. Optimista = {opt5} filas (<= {UMBRAL}).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
