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

Con las dimensiones que se piden — promoción × país × industria × nivel × experiencia — hacen falta del orden de **40 a 60 filas** antes de que las primeras celdas crucen el umbral, y van a ser las combinaciones más comunes: minería en Chile, consultoría en Chile, minería en Canadá.

Las celdas raras quizás nunca se abran. Eso es correcto y es el precio de que nadie quede identificado.

## Formato del dato

Cuando existan, los datos viven en `datos.csv`, plano y auditable:

```csv
promocion,pais,industria,nivel,experiencia,banda_renta_usd,fecha_aporte
2005-2009,Canadá,Minería,Superintendencia,13-20,120000-180000,2026-08
```

Sin nombres, sin empleadores, sin cifras exactas. Solo bandas.

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
