# ici-utfsm — Instrucciones de trabajo

Red de ex alumnos de Ing. Civil Industrial UTFSM. Un oráculo, no una comunidad.

Estructura y razonamiento de diseño: [`HOLONES.md`](HOLONES.md)
Reglas y derechos de decisión: [`GOBERNANZA.md`](GOBERNANZA.md)
La regla que manda sobre todas: [`PRIVACIDAD.md`](PRIVACIDAD.md)

## ⚠️ Este repo es PÚBLICO

Todo lo que se commitea acá lo lee cualquiera: recruiters, tu jefe, tu futuro jefe.

- **Nunca**: nombres completos, empleadores asociados a personas, contactos, cifras exactas de renta
- **Nunca**: datos internos de un empleador — sus tarifas, clientes, márgenes o procesos
- **Nunca**: contenido de repos privados del mantenedor, sea cual sea
- Nombres de terceros solo con permiso explícito

## Todo en holones

Seis preguntas antes de empezar: **S1** qué ejecuta · **S2** a quién afecta y por qué canal · **S3** el comando que decide si cerró · **S3\*** cómo otro lo refuta ejecutando · **S4** qué se aprendió · **S5** qué se pierde si se borra.

Una en UNKNOWN es respuesta válida. Rellenarla por inferencia no.

**Los READMEs cargan el peso.** El README de cada carpeta *es* su holón — no hay documentación aparte que se desincronice.

## Las tres reglas duras

1. **El criterio de muerte se declara antes.** Declararlo después es elegir el que ya sabes que vas a pasar.
2. **El que audita ejecuta, no lee.** Un número sin comando que lo reproduzca no entra.
3. **El umbral k≥5 no se baja nunca.** Ni por esta vez, ni porque la celda es interesante. Una regla de privacidad con excepciones no es una regla.

## Antes de afirmar algo en un README

```bash
./verificar.sh
```

Ejecuta toda afirmación del repo: que los tres activos declaren su holón, que las rutas citadas existan, que el formulario capture los campos que promete, que el Atlas no diga tener datos que no tiene, y que las fuentes oficiales del Tránsito sigan vivas.

Existe porque un README solo lleva carga si algo lo prueba.

**Gotcha del verificador**: varios colegios profesionales están detrás de Cloudflare y devuelven 403 a un curl sin User-Agent de navegador. Un 403 por bot-protection no es un link muerto — no quites el `-A` o el script reporta falsos positivos.

## Estado

| Activo | Estado | Depende de |
|---|---|---|
| `transito/` | utilizable | nada — funciona a n=0 |
| `atlas/` | vacío | ~40-60 filas antes de la primera celda con k≥5 |
| `indice/` | vacío | gente que se ofrezca |

El README raíz publica este estado. **Si cambia acá, cambia allá** — prometer un Atlas lleno que no existe quema lo único que hace que alguien entregue su renta.
