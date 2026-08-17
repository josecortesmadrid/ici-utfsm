# GOBERNANZA

Una red de egresados sin gobernanza escrita muere de una de tres formas: la captura un recruiter, se le agota el mantenedor, o se convierte en un grupo de WhatsApp más. Esto es lo que lo previene.

## Los cinco sistemas

Estructura VSM. Cada uno tiene dueño, y ninguno se audita a sí mismo.

| Sistema | Qué es acá | Quién |
|---|---|---|
| **S1 — Operación** | Los tres activos: [`transito/`](transito/), [`atlas/`](atlas/), [`indice/`](indice/) | Quien aporte a cada uno |
| **S2 — Coordinación** | Plantillas de issue, etiquetas, formato de datos. Evita que dos personas resuelvan lo mismo distinto | Convención, no persona |
| **S3 — Control** | Merge de PRs, actualización del agregado, publicación | Mantenedores (ver abajo) |
| **S3\* — Auditoría** | `./verificar.sh` y `validar_k_anonimato.py`. **Los corre cualquiera, sin permiso** | Cualquier egresado |
| **S4 — Inteligencia** | Qué se pregunta y no tiene respuesta. Define qué se construye después | Las consultas abiertas |
| **S5 — Identidad** | El pacto, la línea roja de privacidad, y decidir cuándo esto se cierra | Mantenedores + quien quiera objetar |

**S3\* es el sistema que hace que lo demás sea creíble.** No confíes en que el mantenedor dice que los datos están bien agregados: clona y córrelo tú.

## Quién decide qué

| Decisión | Quién | Cómo |
|---|---|---|
| Aportar un dato o corregir uno | Cualquiera | Issue o PR |
| Mergear un PR de contenido | Un mantenedor ≠ el autor | CI verde + una revisión |
| Publicar una celda nueva del Atlas | Automático | Solo si pasa k≥5 |
| Bajar contenido por privacidad | **Cualquiera, de inmediato** | Se baja primero, se discute después |
| Cambiar el umbral de privacidad | Nadie | No se cambia. Ver abajo |
| Cerrar la red | Mantenedores, público | Anuncio con razón y datos |

## Lo que no se negocia

**El umbral k≥5 no se baja nunca.** Ni "por esta vez", ni "es que esta celda es interesante", ni "igual nadie se va a dar cuenta". Si una celda no llega a 5, se espera. Una regla de privacidad con excepciones no es una regla, es una intención.

**No entran recruiters ni headhunters** a extraer del Atlas o del Índice. El día que esto sea un canal de sourcing, la gente deja de poner su renta y el activo se muere. Es la razón de existir del repo, no una preferencia.

**No hay plata.** Sin sponsors, sin publicidad, sin membresía, sin cursos. Cualquier flujo de dinero introduce un incentivo para inflar los números, y el único valor acá es que los números sean ciertos.

**El método sube, el dato del empleador nunca.** Tu renta es tuya y la puedes compartir. Las tarifas, clientes, márgenes o procesos internos de tu empleador no son tuyos.

## Conflictos de interés

Se declaran acá, en público:

- **Jose Cortés** (mantenedor inicial) trabaja en PwC. **Nada de este repo se usa para trabajo de PwC, y nada de PwC entra acá.** Si alguna vez el Atlas se usara comercialmente, deja de ser mantenedor.

Si tienes un rol donde el contenido de acá te beneficia profesionalmente — recruiting, consultoría de compensaciones, relocation — decláralo en tu issue de entrada. No inhabilita, pero se sabe.

## Bus factor

Hoy hay **un solo mantenedor**, y eso es una falla conocida, no un diseño.

Mitigación mientras tanto: todo está en markdown y CSV planos, sin base de datos, sin servidor, sin dominio propio. **Cualquiera puede hacer fork y seguir.** Si el mantenedor desaparece, la red no muere: se clona.

Se busca un segundo y un tercer mantenedor, de promociones distintas. Si te interesa, dilo en un issue.

## Cuándo esto se declara muerto

Los criterios se fijan ahora, no cuando duela:

| Señal | Umbral | Qué pasa |
|---|---|---|
| Nadie reenvía | 90 días sin una entrada que diga "me lo pasó alguien" | El activo no vale. Se archiva |
| El Atlas no despega | 6 meses sin ninguna celda que llegue a k=5 | Se borra el Atlas, queda El Tránsito |
| Consultas sin responder | 30 días con la mitad sin respuesta | Se dice públicamente que está inactivo |
| Un incidente de privacidad | Uno solo | Se baja todo, se investiga, se avisa a los afectados |

Archivar es un resultado honesto. **Un repo que finge estar vivo es peor que uno cerrado**, porque el que llega pierde el tiempo y no vuelve.

## Cómo se mide si funciona

No por estrellas ni por miembros. Por estas tres:

1. **Tasa de reenvío** — cuántas entradas dicen "me lo pasó alguien". Es *la* métrica: mide si el valor es real o si solo lo parece.
2. **Consultas respondidas con un número**, no con opinión.
3. **Celdas que cruzan k=5** — mide si el Atlas está naciendo o estancado.

Las tres salen de los issues, así que **cualquiera las puede recontar** sin pedirle el dato a nadie.

---

## Este documento como holón

- **S1** — define derechos de decisión, roles y criterios de muerte de la red.
- **S2** — se acopla con [`PRIVACIDAD.md`](PRIVACIDAD.md), que manda por sobre esto en todo lo que toque datos personales.
- **S3** — cierra cuando toda decisión tomada en el repo se puede rastrear a una fila de la tabla "quién decide qué".
- **S3\*** — un tercero revisa los PRs mergeados y verifica que ninguno lo aprobó su propio autor.
- **S4** — los criterios de muerte se revisan cada 6 meses contra los números reales, no contra la intención.
- **S5** — sin esto, la red la termina capturando quien tenga más interés comercial en ella, que nunca es el egresado que la necesita.
