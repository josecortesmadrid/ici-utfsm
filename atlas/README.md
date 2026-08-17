# El Atlas

**Bandas de renta y trayectoria, solo ICI UTFSM.** El dato que no existe en ninguna otra parte.

## Estado: vacío

**0 filas. 0 celdas publicables.**

Esto no es un placeholder que después alguien va a llenar. Es el estado real, y va a decir la verdad siempre: cuando tenga datos dirá cuántos y de qué fecha.

Un Atlas que promete datos que no tiene es peor que uno vacío, porque quema la única cosa que hace que alguien entregue su renta: que acá no se exagera.

## Por qué esto vale más que Glassdoor

Glassdoor tiene millones de filas y no te sirve, porque "Ingeniero Industrial" en Chile mezcla a un analista de 25 con un gerente de operaciones de 45. La dispersión es tan grande que la mediana no significa nada.

Acá el denominador es fijo: **misma carrera, misma escuela**. Con eso, la banda de "promoción 2010, minería, Canadá, 13 años" te dice algo real sobre tu oferta.

Es un activo que **solo se puede construir entre nosotros**, y esa es toda su ventaja.

## Cuándo vas a poder ver algo

Cada celda se publica cuando junta **5 personas o más**. Ni una menos.

**Cuántas filas hacen falta — medido, no estimado:**

```bash
python scripts/probe_masa_critica.py
```

| Escenario | 5 dimensiones | 3 dimensiones |
|---|---|---|
| Optimista (red-clan: 80% Chile, 60% minería) | 32 filas | 18 |
| **Realista** | **246 filas** | **77** |
| Disperso (la red logra variedad) | 2.271 filas | 450 |

Este README decía antes *"del orden de 40 a 60 filas"*. **Ese número era falso**: solo se cumple en el escenario optimista, que es una red-clan poco realista, y se publicó sin calcularlo. El probe de arriba lo corrigió el mismo día.

**Por eso el Atlas publica en 3 dimensiones**, no en 5: `país × industria × nivel`. Soltar promoción y experiencia baja el requisito de 246 a 77 filas — la diferencia entre alcanzable e imposible. Promoción y experiencia se piden igual, pero se publican por separado y **nunca cruzadas** con las otras tres.

Es también la decisión más segura: cruzar cinco atributos en una cohorte chica es lo que convierte un agregado en un nombre propio.

Las celdas raras quizás nunca se abran. Es correcto, y es el precio de que nadie quede identificado.

## Formato del dato

`datos.csv` es un **agregado, no un padrón**. Una fila = una celda con su conteo, nunca una fila por persona:

```csv
pais,industria,nivel,n,banda_renta_usd,fecha_corte
Canadá,Minería,Superintendencia,7,120000-180000,2026-08
```

Esto no es cosmético. Un CSV con una fila por persona y cinco atributos es un **cuasi-identificador**: aunque no lleve nombres, cada fila describe a un individuo con precisión suficiente para despejarlo. El agregado no tiene esa propiedad — y el `n` de cada fila hace que el umbral sea auditable de un vistazo.

Los aportes individuales viven en los issues, no en el repo.

## Verifícalo tú

No confíes en que el agregado está bien hecho:

```bash
python scripts/validar_k_anonimato.py atlas/datos.csv
```

Te dice cuántas celdas hay, cuáles pasan el umbral y cuáles no. Si encuentras una celda publicada con menos de 5, **es un incidente de privacidad** — repórtalo y se baja de inmediato.

## Cómo aportar tu fila

[Formulario de entrada](../../../issues/new?template=00-entrada.yml) — 3 minutos, todo en tramos, nada te identifica.

La renta es opcional. Pero es **el dato**: sin ella el Atlas es un censo de dónde trabaja la gente, que ya lo hace LinkedIn gratis.

---

## Este documento como holón

- **S1** — agregar filas en bandas y publicar solo las celdas que cruzan k≥5. Artefacto: `datos.csv` + este README con el conteo real.
- **S2** — se alimenta de los issues de entrada; se acopla a [`PRIVACIDAD.md`](../PRIVACIDAD.md), que puede bloquear cualquier publicación.
- **S3** — cierra cuando existe **al menos una celda publicada** con k≥5. Hoy: **no cierra, 0 celdas**.
- **S3\*** — cualquiera corre el validador contra `datos.csv` y recuenta. El conteo de este README tiene que coincidir con la salida del script; si no coincide, el README miente.
- **S4** — a medida que entran filas, celdas bloqueadas se abren solas. El patrón de qué celda cruza primero dice dónde está concentrada realmente la red.
- **S5** — es el activo que compone: cada fila lo hace más valioso para todos, incluido el que la puso. Es la única pieza con efecto de red genuino. **Si muere, quedan un playbook y una lista de contactos, que es lo que ya tenías.**
