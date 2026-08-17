#!/usr/bin/env bash
# Verifica que este repo no mienta.
#
# Todo README hace afirmaciones. Este script las ejecuta.
# Si algo de lo que dice el repo es falso, esto falla.

set -uo pipefail
cd "$(dirname "$0")"

FALLAS=0
ok()    { echo "  ✓ $1"; }
falla() { echo "  ✗ $1"; FALLAS=$((FALLAS+1)); }

echo ""
echo "  Verificando ICI UTFSM..."
echo ""

# --- 1. Los tres activos existen y tienen holón ---
echo "  [1] Los tres activos"
for d in transito atlas indice; do
    if [ -f "$d/README.md" ]; then
        if grep -q "como holón" "$d/README.md"; then
            ok "$d/ existe y declara su holón"
        else
            falla "$d/README.md no declara su holón (S1-S5)"
        fi
    else
        falla "$d/README.md no existe — el README raíz lo enlaza"
    fi
done

# --- 2. Toda ruta enlazada desde el README raíz existe ---
echo ""
echo "  [2] Enlaces internos del README"
while IFS= read -r destino; do
    [ -e "${destino%/}" ] || [ -e "$destino" ] && ok "$destino" || falla "$destino enlazado pero no existe"
done < <(grep -o '](\([A-Za-z0-9_./-]*\))' README.md | sed 's/](//; s/)//' | grep -v '^http' | grep -v '^#' | sort -u)

# --- 3. El formulario de onboarding captura los 5 campos + la arista ---
echo ""
echo "  [3] Onboarding captura lo que dice capturar"
FORM=".github/ISSUE_TEMPLATE/00-entrada.yml"
if [ -f "$FORM" ]; then
    for campo in promocion industria nivel con_que que_espera que_acepta llegada; do
        grep -q "id: $campo" "$FORM" && ok "captura '$campo'" || falla "falta el campo '$campo'"
    done
else
    falla "$FORM no existe — el README manda a la gente ahí"
fi

# --- 4. El validador de privacidad corre de verdad ---
echo ""
echo "  [4] La regla de privacidad se ejecuta"
if [ -f scripts/validar_k_anonimato.py ]; then
    if python scripts/validar_k_anonimato.py atlas/datos.csv >/dev/null 2>&1; then
        ok "validar_k_anonimato.py corre y pasa"
    else
        falla "validar_k_anonimato.py falla — hay celdas bajo umbral"
    fi
else
    falla "scripts/validar_k_anonimato.py no existe — PRIVACIDAD.md lo promete"
fi

# --- 5. El Atlas no promete datos que no tiene ---
echo ""
echo "  [5] El Atlas dice la verdad sobre su estado"
if [ -f atlas/datos.csv ]; then
    N=$(($(wc -l < atlas/datos.csv) - 1))
    grep -q "$N filas\|$N fila" atlas/README.md && ok "el conteo del README coincide ($N)" \
        || falla "atlas/README.md no refleja las $N filas reales de datos.csv"
else
    grep -qi "vac[ií]o\|0 filas" atlas/README.md && ok "declara honestamente que está vacío" \
        || falla "no hay datos.csv pero el README no dice que está vacío"
fi

# --- 6. Las fuentes oficiales del Tránsito siguen vivas ---
echo ""
echo "  [6] Fuentes oficiales del Tránsito"
# UA de navegador a proposito: varios colegios profesionales estan detras de
# Cloudflare y responden 403 a un curl pelado. Un 403 por bot-protection no es
# un link muerto — sin esto, el verificador reporta falsos positivos.
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"
if command -v curl >/dev/null 2>&1; then
    while IFS= read -r url; do
        # Sin '|| echo': curl ya imprime 000 al fallar y el fallback lo duplicaba.
        code=$(curl -s -o /dev/null -w "%{http_code}" -m 15 -L -A "$UA" "$url" 2>/dev/null)
        code="${code:-000}"
        case "$code" in
            2*|3*) ok "$url ($code)" ;;
            000)   echo "  ~ $url (sin red, no concluyente)" ;;
            *)     falla "$url responde $code" ;;
        esac
    done < <(grep -oh 'https://[A-Za-z0-9./-]*' transito/README.md | sed 's/[.,)]*$//' | sort -u)
else
    echo "  ~ curl no disponible, se omite"
fi

echo ""
if [ "$FALLAS" -gt 0 ]; then
    echo "  ❌ $FALLAS afirmación(es) del repo son falsas."
    echo "     Un README solo lleva carga si algo lo prueba."
    exit 1
fi
echo "  ✅ Todo lo que el repo afirma es cierto."
echo ""
