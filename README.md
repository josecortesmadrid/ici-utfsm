# ICI UTFSM — la red

**Ingeniería Civil Industrial, Universidad Técnica Federico Santa María. Ex alumnos y amigos.**

Esto no es una comunidad. Es un **oráculo**: vienes cuando tienes una pregunta cara, te llevas una respuesta con números, y te vas. No hay que sumarse a nada para usarlo.

---

## Empieza acá

Estás en uno de estos tres momentos. Anda directo al tuyo:

| Tu situación | Anda a |
|---|---|
| Me voy del país, o lo estoy pensando | **[El Tránsito](transito/)** — validación de título, P.Eng, rutas migratorias, plata y plazos reales |
| Tengo una oferta y no sé si es buena | **[El Atlas](atlas/)** — bandas de renta y trayectoria, solo ICI UTFSM |
| Necesito hablar con alguien que ya lo hizo | **[El Índice](indice/)** — quién cruzó por dónde, y cómo pedirle una conversación |

Todo es público y se lee sin cuenta, sin formulario y sin pedir permiso.

## Por qué esto existe teniendo LinkedIn

LinkedIn te dice quién trabaja dónde. No te dice **cuánto**, ni **qué costó llegar**, ni **qué haría distinto**.

Y Glassdoor no te sirve porque mezcla peras con manzanas: "Ingeniero Industrial" en Chile abarca desde un analista recién salido hasta un gerente de operaciones con 20 años. Acá el denominador es el mismo — misma carrera, misma escuela — así que las comparaciones son reales.

Eso solo se puede construir entre nosotros. Es la única ventaja que tiene esta red, y es toda su razón de ser.

## El pacto

**Primero recibes. Después decides si aportas.** En ese orden, y nunca al revés.

No hay peaje de entrada porque el peaje mata el reenvío: si te pido un formulario antes de darte algo, te vas y no le pasas el link a nadie. Entonces: lee todo, úsalo, y **si te sirvió**, [deja tu fila](../../issues/new?template=00-entrada.yml). Toma tres minutos.

Lo que se pide es lo mínimo para que el Atlas funcione, y está diseñado para no identificarte:

- **Quién** — promoción y país. No tu nombre completo si no quieres
- **Haciendo qué** — rol y industria
- **Con qué** — títulos, certificaciones, idiomas, herramientas
- **Qué esperas** — para qué viniste, qué pregunta traías
- **Qué aceptas** — el pacto de datos: qué se puede publicar de lo tuyo y qué no

## Cómo se protege tu información

Este repo es **público**, así que la regla es dura y no se negocia:

> **Nada se publica en una celda con menos de 5 personas.** Bandas, nunca cifras exactas. Jamás el cruce empleador × cargo × promoción.

En una cohorte chica, "gerente de operaciones, promoción 2008, en una minera canadiense" es **una sola persona con otro nombre**. Un CI de validación bloquea cualquier publicación que rompa el umbral. Los detalles están en **[PRIVACIDAD.md](PRIVACIDAD.md)**, y son la regla que manda por sobre cualquier cosa que alguien quiera publicar.

## Estado real, hoy

Esto recién parte y decirlo es parte del trato:

| Pieza | Estado | Medido |
|---|---|---|
| El Tránsito | **esqueleto** — 4 hechos oficiales, 6 huecos, 0 testimonios | conteo de marcas |
| El Atlas | **vacío** — 0 filas, 0 celdas publicables | `validar_k_anonimato.py` |
| El Índice | **vacío** — 0 personas ofrecidas | conteo de issues |

Dos correcciones hechas el mismo día de publicar, porque los números iniciales estaban mal:

- El Atlas decía necesitar *"40 a 60 filas"*. **Medido: 246** en el escenario realista. El número se había escrito sin calcularlo. Por eso el Atlas pasó a publicar en 3 dimensiones en vez de 5, lo que lo baja a **77**. Corre `python scripts/probe_masa_critica.py` y lo reproduces.
- El Tránsito decía ser *"utilizable"*. Contado: **4 hechos contra 6 huecos**. Es un esqueleto, y ahora lo dice.

Ese es el estándar acá: **cuando un número de este repo resulta falso, se corrige a la vista, no se borra.**

## Cómo se gobierna

Roles, quién decide qué, y cuándo esto se declara muerto: **[GOBERNANZA.md](GOBERNANZA.md)**.
La estructura completa en holones VSM: **[HOLONES.md](HOLONES.md)**.

Regla de fondo, heredada: **el que audita ejecuta, no lee.** Ningún número acá vale si no viene con el comando o la fuente que lo reproduce.

---

## Si esto te sirvió

Pásaselo al que lo va a necesitar. No a todos — **al que está justo en ese momento**: el que te dijo que está pensando en irse, el que te contó que le llegó una oferta, el que quedó fuera en la última reestructuración.

Esa es la única forma en que esto crece, y es la que estamos midiendo: el formulario de entrada pregunta **quién te pasó el link**. Si nadie reenvía, se nota en los datos y esto se cierra en vez de fingir que está vivo.

*Mantenido por egresados. Sin fines de lucro, sin publicidad, sin recruiters.*
