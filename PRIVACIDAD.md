# PRIVACIDAD — la regla que manda sobre todas las demás

Este repo es **público**. Cualquiera lo lee: recruiters, tu jefe, tu futuro jefe, tu ex jefe. Todo lo que sigue está diseñado para eso.

## La regla dura

> **Ninguna celda con menos de 5 personas se publica.**
> **Bandas, nunca cifras exactas.**
> **Jamás el cruce empleador × cargo × promoción.**

No es una recomendación. Es un chequeo automático que corre en cada PR y lo bloquea.

## Por qué 5, y por qué esto es en serio

En una cohorte chica, un cruce de tres atributos **es un nombre propio con otro disfraz**:

> "Gerente de operaciones · promoción 2008 · minera canadiense"

Eso no es un dato anónimo. En ICI UTFSM, cualquiera del rubro lo despeja en treinta segundos. Y ya despejado, quedó publicada su renta en un repo público, para siempre, sin que él lo autorizara.

Un seudónimo no anonimiza a nadie en un grupo donde todos se conocen. **Tampoco lo hace agregar, si el agregado tiene n=1.**

Con n≥5 y bandas anchas, saber que alguien está en la celda no te dice cuál de los cinco es ni cuánto gana exactamente.

## Qué nunca entra al repo

- Nombres completos y apellidos
- Empleadores actuales asociados a una persona o a una renta
- Correos, teléfonos, links a perfiles personales
- Cifras exactas de renta — siempre banda
- Capturas de ofertas, contratos, liquidaciones o correos
- Cualquier dato interno de una empresa: sus tarifas, sus clientes, sus márgenes, sus procesos

Ese último punto es importante y tiene poco que ver con la privacidad personal: varios de nosotros firmamos confidencialidad. **Tu renta es tuya y la puedes compartir. Los datos de tu empleador no son tuyos.**

## Qué sí entra

- Tramos: promoción, experiencia, renta, todo en banda
- País, industria, nivel — categorías cerradas, elegidas de una lista
- Certificaciones, títulos, idiomas — son públicos en tu perfil de todas formas
- Rutas y procesos: cómo se saca una colegiatura, qué demoró, qué costó
- Hechos verificables de fuentes oficiales, con su link

## Cómo se hace cumplir

`scripts/validar_k_anonimato.py` corre en cada PR sobre los datos agregados. Si alguna celda queda bajo el umbral, **el PR no se puede mergear**. No hay override manual: si quieres publicar esa celda, junta más filas.

```bash
python scripts/validar_k_anonimato.py atlas/datos.csv
```

Esto es deliberadamente automático. Una regla de privacidad que depende de que un humano se acuerde de revisarla ya falló — solo que todavía no te enteraste.

## Cómo retirar tus datos

Comenta `retirar` en tu issue de entrada y ciérralo. Sale del agregado en la siguiente actualización, y la fecha de esa actualización está publicada en el Atlas.

No hay que dar explicaciones ni pedirle permiso a nadie.

## Si ves algo que no debería estar

Abre un issue con la etiqueta `privacidad`, o escríbele directo al mantenedor. **Se baja primero y se discute después** — nunca al revés.

---

## Este documento como holón

- **S1 Operación** — un umbral k≥5 aplicado por `validar_k_anonimato.py` en cada PR.
- **S2 Coordinación** — manda sobre cualquier propuesta de contenido, venga de quien venga. Ninguna otra regla del repo la sobreescribe.
- **S3 Control** — cierra cuando el CI está verde: cero celdas bajo umbral en los datos publicados.
- **S3\* Auditoría** — cualquiera clona el repo y corre el validador contra los datos publicados. Si encuentra una celda bajo umbral, el sistema falló y hay que bajarla. **No hay que confiar en la palabra del mantenedor: el chequeo es reproducible por cualquiera.**
- **S4 Inteligencia** — a medida que crecen las filas, celdas que hoy están bloqueadas se van abriendo solas. El umbral no cambia; lo que cambia es cuánto se puede mostrar.
- **S5 Identidad** — sin esto la red no puede existir en un repo público. Nadie entrega su renta a un lugar donde puede quedar con su nombre al lado, y el primer incidente termina con la red entera. **Es la condición de posibilidad de todo lo demás, no una capa de cumplimiento encima.**
