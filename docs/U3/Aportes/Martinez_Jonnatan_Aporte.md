# Aporte individual — Martínez Aquino Jonnatan

**Proyecto:** XALTIL (Equipo Webtons)
**Sección del proceso asignada:** Búsqueda de centros (CAP-01): ingreso de ubicación y especialidad, y lista de resultados
**Rol principal de la U3:** Desarrollo / prototipo
**Fecha:** 2026-11-16

> Este borrador no sustituye al PDF `U3-E02_Jonnatan_Martinez_ObtencionYRedaccion.pdf`. Todo lo no confirmado queda como «Pendiente» o «Por validar».

## 1. Información que necesito obtener

- **Pregunta 1:** ¿Qué datos ingresa normalmente un paciente o familiar para buscar un centro de salud, y qué errores comete al hacerlo (ubicación vacía o mal escrita, especialidad que no sabe elegir)?
- **Pregunta 2:** ¿Cuántos centros suelen coincidir con una búsqueda y cuántos resultados necesita ver para comparar? (relacionada con P-05 de la sección B4 del E01)
- **Pregunta 3:** ¿Con qué datos y método se estimaría el tiempo de traslado? (B1 del E01, asignada a mí)
- **Técnica elegida y motivo:** encuesta corta a pacientes o familiares (junto con Análisis), porque da acceso rápido a varias personas; y análisis documental de la documentación pública de servicios de mapas para la pregunta 3.
- **Fuente a consultar:** pacientes o familiares; documentación pública de servicios de mapas.
- **Fecha prevista o estado:** Pendiente.

## 2. Información que ya tengo

- **Fuente real:** F-01, documento U2-E01 «Inicio del modelado del negocio» (Equipo Webtons), fecha 2026-10-07. Respaldo: `docs/U2/`.
- **Hallazgo comprobable:** U2-E01 identifica la falta de información centralizada sobre saturación, disponibilidad y tiempos de espera de centros de salud. Es un antecedente del equipo, no una confirmación por usuarios.
- **Dudas:** aún no hay consulta con usuarios; no sé si la ubicación se escribirá a mano o se tomará del dispositivo, ni cuántos centros coinciden normalmente con una búsqueda.

## 3. Necesidad identificada

- **N-02:** los usuarios necesitan consultar centros distintos desde una misma plataforma (respaldo: F-01).

## 4. Requisitos propuestos

### RF-01

| Campo | Contenido |
|---|---|
| ID provisional | RF-01 |
| Tipo | Funcional |
| Enunciado | El sistema debe permitir al usuario ingresar una ubicación y una especialidad médica para buscar centros de salud, y avisar con texto cuando falte alguno de los dos datos. |
| Fuente | F-01 / N-02 |
| Prioridad | P1: es el punto de inicio del proceso; sin él no hay consulta. |
| Estado | Por validar |

**Criterios de aceptación**

| ID | Dado | Cuando | Entonces |
|---|---|---|---|
| CA-RF-01a (éxito) | El usuario escribe una ubicación y elige una especialidad. | Presiona «Buscar centros». | El sistema ejecuta la búsqueda y muestra la lista de resultados. |
| CA-RF-01b (alternativa) | Falta la ubicación o la especialidad. | Presiona «Buscar centros». | No se ejecuta la búsqueda y aparece un texto que indica qué dato falta. |

### RF-02

| Campo | Contenido |
|---|---|
| ID provisional | RF-02 |
| Tipo | Funcional |
| Enunciado | El sistema debe mostrar una lista de centros de salud que coincidan con la búsqueda (al menos tres cuando existan) e informar si hay menos resultados. |
| Fuente | F-01 / N-02 |
| Prioridad | P1: permite comparar opciones; sin lista no se puede elegir centro. |
| Estado | Por validar |

**Criterios de aceptación**

| ID | Dado | Cuando | Entonces |
|---|---|---|---|
| CA-RF-02a (éxito) | Existen al menos tres centros que coinciden con la búsqueda. | El usuario realiza la búsqueda. | Se muestran al menos tres centros. |
| CA-RF-02b (alternativa) | Coinciden menos de tres centros. | El usuario realiza la búsqueda. | Se muestran los centros existentes y un texto indica que hay pocos resultados. |

## 5. Aporte al boceto (rol Desarrollo)

- Cuatro momentos del recorrido: 01 Inicio, 02 Acción, 03 Respuesta (03A éxito y 03B error) y 04 Consulta.
- Archivo: `docs/U3/prototipo/U3_Prototipo_XALTIL_Recorrido.png`.
- El estado 04 queda como **provisional, pendiente de validar**, porque no tiene un RF propio.
- Los datos del boceto (centros, tiempos, folio) son ficticios.

## 6. Pendientes

- Hacer la consulta real (preguntas 1 y 2) y registrarla como fuente con fecha y respaldo.
- Consultar la documentación de mapas para el tiempo de traslado (pregunta 3).
- Abrir el PR de este aporte y del boceto, y pedir revisión a otro integrante.
