# HOLONES — ICI UTFSM

Cada pieza de este repo es un **holón**: una caja autónoma que responde seis preguntas y contiene otras cajas que responden las mismas seis. El README de cada carpeta *es* su holón — no hay documentación aparte que se desincronice.

## La plantilla

- **S1 Operación** — qué ejecuta, con qué comando, qué artefacto produce
- **S2 Coordinación** — con quién se acopla y por qué canal
- **S3 Control** — el comando cuya salida decide si cerró. Nunca "revisar que esté bien"
- **S3\* Auditoría** — cómo un tercero lo refuta **ejecutando**, sin confiar en el reporte
- **S4 Inteligencia** — qué aprende del entorno
- **S5 Identidad** — qué se pierde si se borra

Dos reglas que vienen con la plantilla: **el kill criterion se declara antes de empezar**, y **el auditor ejecuta, no lee**.

## El árbol

```
L0  La red ICI UTFSM
├── L1.1  Los activos (S1 — lo que produce valor)
│   ├── L2.1  transito/   → cómo se cruza          [utilizable a n=0]
│   ├── L2.2  atlas/      → cuánto se gana         [vacío, necesita k≥5]
│   └── L2.3  indice/     → quién ya lo hizo       [vacío]
├── L1.2  El pacto (S5 — la condición de posibilidad)
│   ├── L2.4  PRIVACIDAD.md   → k≥5, sin excepciones
│   └── L2.5  GOBERNANZA.md   → quién decide, cuándo se muere
└── L1.3  El torniquete (S2/S3* — entrada y prueba)
    ├── L2.6  .github/ISSUE_TEMPLATE/  → captura los 5 campos + la arista
    └── L2.7  verificar.sh + validar_k_anonimato.py → prueban que el repo no miente
```

---

# L0 — LA RED

- **S1**: un oráculo público de tres activos. Se consulta en un evento de vida — una oferta, una mudanza, un despido —, entrega un número con su fuente, y no pide nada a cambio para entrar.
- **S2**: el canal es GitHub Issues. Sin Slack, sin WhatsApp, sin newsletter: **todo canal que exige presencia recurrente decae**, y este está diseñado para que puedas no aparecer por dos años y siga sirviéndote.
- **S3**: cierra cuando **una persona que no conocía el repo llega por un reenvío, resuelve su pregunta y deja su fila**. Ese ciclo completo es la unidad de éxito. Hoy: no ha ocurrido.
- **S3\***: `./verificar.sh` — ejecuta toda afirmación de los READMEs. Cualquiera lo corre sin permiso. Además, la tasa de reenvío es recontable desde los issues por cualquiera.
- **S4**: el campo *"¿cómo llegaste acá?"* es el sensor. Distingue crecimiento orgánico de gente que Jose invitó a mano. Sin él, "esto se pasa solo" sería **infalsificable**.
- **S5**: es el único lugar donde un ICI UTFSM puede comparar su carrera con un denominador idéntico. Si se borra, esa comparación no existe en ninguna otra parte — ni LinkedIn, ni Glassdoor, ni el grupo de WhatsApp de la promoción.

## El razonamiento que define qué se sube

La pregunta de diseño fue: *¿qué se sube para que lo reenvíen orgánicamente?* Cinco inversiones, y la última es la que manda:

1. **El reenvío es estatus, no utilidad.** No se reenvía lo que te sirvió; se reenvía lo que te hace quedar bien al mandarlo. Un número que el otro no consigue en ninguna parte da estatus.
2. **La ventaja es el denominador.** Glassdoor mezcla peras con manzanas; acá la carrera y la escuela son las mismas. Inobtenible fuera, e inútil en single-player: **requiere que el grupo exista.**
3. **Oráculo, no comunidad.** El *engagement* recurrente es caro y decae. El reenvío se dispara por **evento de vida**, no por hábito: "¿te vas a Canadá? mira esto". Eso no necesita retención.
4. **El peaje mata el reenvío.** Si el link exige formulario antes de dar valor, el que lo recibe rebota y no lo vuelve a pasar. Por eso el valor es abierto y el aporte se pide **en el momento de máxima gratitud**, después de recibir.
5. **A n=0 hay que subir lo que no depende de n.** El Atlas necesita ~40-60 filas antes de mostrar su primera celda. Prometerlo hoy sería documentar la intención como si fuera el estado. Por eso arranca **`transito/`**, que se escribe con hechos oficiales y sirve el primer día. El Atlas compone después.

**Contraria contra la propia tesis**: el activo obvio — renta por persona — es un dossier identificable en una cohorte de este tamaño. "Gerente de operaciones, promoción 2008, minera canadiense" es un nombre propio disfrazado. Por eso k≥5 no es cumplimiento: es la condición que permite que el activo exista.

---

# L1.2 — EL PACTO

- **S1**: dos documentos que definen qué se puede publicar y quién decide.
- **S3**: cierra cuando CI está verde y toda decisión tomada se rastrea a una fila de "quién decide qué".
- **S3\***: clonar, correr `validar_k_anonimato.py`, y revisar que ningún PR lo haya aprobado su propio autor.
- **S5**: **manda sobre todo lo demás.** Nadie entrega su renta a un repo público donde puede quedar con su nombre al lado, y un solo incidente termina la red entera.

# L1.3 — EL TORNIQUETE

- **S1**: capturar en 3 minutos *quién · haciendo qué · con qué · qué espera · qué acepta*, más **quién le pasó el link**.
- **S2**: es la única entrada de datos del sistema. Todo lo que publica el Atlas viene de acá.
- **S3**: `./verificar.sh` confirma que el formulario captura los 7 campos que los READMEs prometen.
- **S3\***: ejecutado — **7/7 campos verificados**.
- **S4**: el campo *"qué esperas"* es el backlog real. Lo más preguntado se construye primero, en vez de adivinar qué necesita la gente.
- **S5**: sin la arista de reenvío no se puede saber si la red crece sola o si Jose la está empujando a mano. **Es la diferencia entre un activo y un pasatiempo.**

---

## Estado y criterios de muerte

| Holón | Estado | S3 cierra cuando | Kill criterion |
|---|---|---|---|
| L0 la red | arrancando | un ciclo completo reenvío→consulta→aporte | 90 días sin reenvío orgánico |
| L2.1 `transito/` | **utilizable** | cero afirmaciones sin marca `[OFICIAL]`/`[VIVIDO]` | — |
| L2.2 `atlas/` | vacío | ≥1 celda con k≥5 | 6 meses sin ninguna celda |
| L2.3 `indice/` | vacío | ≥1 transición con persona ofrecida | — |
| L2.4 privacidad | activo | CI verde | un incidente → se baja todo |
| L2.7 verificador | activo | `./verificar.sh` sale 0 | — |

Archivar es un resultado honesto. **Un repo que finge estar vivo es peor que uno cerrado.**
