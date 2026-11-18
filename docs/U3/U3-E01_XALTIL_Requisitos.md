<!-- Archivo: docs/U3/U3-E01_XALTIL_Requisitos.md -->
# U3 · Especificación de requisitos — XALTIL

**Versión:** 0.2

**Fecha:** 2026-11-16

**Equipo:** Webtons

**Materia:** Fundamentos de Ingeniería de Software (SCC-1007) · Unidad 3 · Ingeniería de Requisitos

**Estado del documento:** En elaboración

**Equipo y roles (U3):**

| Integrante | Rol principal en U3 |
|---|---|
| García Villegas Jorge Ignacio | Documentación |
| Martínez Aquino Jonnatan | Desarrollo / prototipo |
| Obregón Estrada Emmanuel | Coordinación |
| Ortiz Saucedo Jesús Adán | Análisis y QA / revisión |

- **Responsable de integración del documento:** García Villegas Jorge Ignacio (Documentación). Revisa los PR de los demás integrantes.
- **Responsable de revisión de los PR de Documentación:** Ortiz Saucedo Jesús Adán (QA). Nadie revisa su propio PR.

---

## A. Identificación y alcance

### A.1 Identificación del proyecto

XALTIL es una propuesta de plataforma web para consultar la disponibilidad y la saturación de centros de salud. Su propósito es ofrecer información centralizada para que pacientes y familiares comparen opciones de atención antes de desplazarse.

El sistema contempla mostrar centros de salud cercanos, su nivel de saturación, el tiempo estimado de espera y el tiempo estimado de traslado, y permitir solicitar un turno cuando exista disponibilidad.

### A.2 Proceso TO-BE seleccionado

**Proceso:** consulta de disponibilidad y solicitud de turno en centros de salud.

El usuario ingresa su ubicación y la especialidad que necesita. El sistema presenta los centros encontrados con su saturación y tiempos estimados. El usuario selecciona un centro y solicita un turno; si el centro no tiene disponibilidad, el sistema lo informa y el usuario puede elegir otro centro.

### A.3 Objetivo de esta especificación

Documentar y organizar los requisitos funcionales y no funcionales necesarios para definir el comportamiento esperado de XALTIL, con sus prioridades, fuentes, autores y criterios de aceptación.

### A.4 Alcance

**Dentro del alcance:**

- Consultar centros de salud con una ubicación y una especialidad ingresadas por el usuario.
- Mostrar centros cercanos con su nivel de saturación, tiempo estimado de espera y tiempo estimado de traslado.
- Solicitar un turno cuando el centro tenga disponibilidad, o informar cuando no la tenga.
- Mostrar una confirmación con folio de la solicitud realizada.
- Evitar la exposición pública de datos personales de pacientes.

**Fuera del alcance:**

- Realizar diagnósticos médicos.
- Sustituir los sistemas internos de administración hospitalaria.
- Garantizar la eliminación de los tiempos de espera.
- Garantizar que todos los centros compartan información en tiempo real.
- Administrar tratamientos o historiales clínicos.
- Garantizar la atención médica de un paciente.

### A.5 Indicador de mejora

Diferencia entre el tiempo de espera estimado que muestra XALTIL y el tiempo real que espera el paciente en el centro de salud.

### A.6 Aportaciones del equipo

| Nombre | Rol U3 | Requisitos que redactó |
|---|---|---|
| Martínez Aquino Jonnatan | Desarrollo | RF-01, RF-02 |
| Ortiz Saucedo Jesús Adán | Análisis y QA | RF-03, RF-04 |
| Obregón Estrada Emmanuel | Coordinación | RF-05, RF-06 |
| García Villegas Jorge Ignacio | Documentación | RF-07, RNF-01 |

**Estado del alcance:** definido con base en el documento U2-E01. Pendiente de validación con usuarios y representantes de centros de salud.

---

## B. Fuentes y necesidades

### B1. Plan de obtención

Estas consultas **aún no se realizan**. Son plan, no fuentes; por eso no tienen ID F.

| Pregunta por resolver | Persona o documento a consultar | Técnica | Responsable | Estado |
|---|---|---|---|---|
| ¿Qué información necesita un paciente o familiar antes de acudir a un centro de salud? | Pacientes o familiares | Encuesta corta o entrevista | Ortiz Saucedo | Pendiente |
| ¿Cómo se registra y actualiza hoy la ocupación y la disponibilidad de turnos? | Personal de recepción o administrativo | Entrevista u observación | Obregón Estrada | Pendiente |
| ¿Qué condiciones y restricciones existen para compartir datos de ocupación? | Directivos o administradores, o aviso de privacidad público | Entrevista o análisis documental | García Villegas | Pendiente |
| ¿Con qué datos y método se estimaría el tiempo de traslado? | Documentación pública de servicios de mapas | Análisis documental | Martínez Aquino | Pendiente |

### B2. Fuentes realmente consultadas

| ID | Técnica o documento | Fecha | Hallazgo o necesidad | Estado | Referencia |
|---|---|---|---|---|---|
| F-01 | Documento U2-E01: Inicio del modelado del negocio (Equipo Webtons) | 2026-10-07 | Falta de información centralizada sobre saturación, disponibilidad y tiempos de espera de centros de salud. | Documentado; pendiente de validar con usuarios | `docs/U2/` |

### B3. Necesidades identificadas

| ID | Necesidad | Respaldo | Requisito vinculado |
|---|---|---|---|
| N-01 | Los pacientes necesitan conocer la saturación de los centros antes de desplazarse. | F-01 | RF-03 |
| N-02 | Los usuarios necesitan consultar centros distintos desde una misma plataforma. | F-01 | RF-01, RF-02 |
| N-03 | Los pacientes necesitan conocer el tiempo estimado de espera. | F-01 | RF-04 |
| N-04 | Los usuarios necesitan conocer el tiempo aproximado de traslado. | F-01 | RF-05 |
| N-05 | Los pacientes necesitan identificar centros con disponibilidad para solicitar turno y saber si su solicitud quedó registrada. | F-01 | RF-06, RF-07 |
| N-06 | El personal administrativo necesita que actualizar la información no sea una carga considerable. | F-01 | Sin requisito todavía (ver B4) |
| N-07 | Los centros necesitan proteger la información que no debe ser pública. | F-01 | RNF-01 |

### B4. Pendientes y suposiciones por comprobar

| ID | Duda o suposición | A quién consultar | Responsable | Estado |
|---|---|---|---|---|
| P-01 | Los hospitales y clínicas estarían dispuestos a compartir datos de ocupación. | Directivos o administradores | García Villegas | Pendiente |
| P-02 | La información podrá actualizarse con la frecuencia necesaria. | Personal de recepción | Obregón Estrada | Pendiente |
| P-03 | Es posible integrar centros con distintos sistemas internos. | Administradores de TI o directivos | Martínez Aquino | Pendiente |
| P-04 | Qué condiciones de privacidad aplican y quién es un «usuario autorizado» (afecta RG-03 y RNF-01). | Directivos o aviso de privacidad | García Villegas | Pendiente |
| P-05 | Cuántos centros suelen coincidir con una búsqueda (afecta RF-02). | Pacientes o fuente de datos | Ortiz Saucedo | Pendiente |
| P-06 | Cómo reduce XALTIL la carga del personal (N-06) y si requiere un RF propio. | Personal administrativo | Ortiz Saucedo | Pendiente |


---

## C. Organización del alcance

- **Ruta elegida:** A (con épica)
- **Motivo de elección:** el proceso agrupa varias capacidades relacionadas (búsqueda, visualización de información, consulta de disponibilidad y solicitud de turnos) que deben dividirse para analizarse y comprobarse por separado.

### C.1 Épica

**EP-01 · Consultar centros de salud y gestionar solicitudes de turno.**

**Objetivo:** permitir que pacientes y familiares encuentren centros cercanos, consulten su ocupación y disponibilidad, y soliciten un turno antes de desplazarse.

### C.2 Capacidades desglosadas

| ID | Capacidad | Descripción | Requisitos vinculados |
|---|---|---|---|
| CAP-01 | Búsqueda de centros | Consultar centros por ubicación y especialidad. | RF-01, RF-02 |
| CAP-02 | Consulta de información | Visualizar saturación y tiempos estimados. | RF-03, RF-04, RF-05 |
| CAP-03 | Solicitud de turno | Solicitar turno si hay disponibilidad y confirmar el registro. | RF-06, RF-07 |
| CAP-04 | Protección de información | Evitar la exposición de datos personales. | RNF-01 |


---

## D. Reglas del dominio

| ID | Regla del contexto | Quién la establece | Origen en B2 | Estado |
|---|---|---|---|---|
| RG-01 | Un paciente solo podrá solicitar turno en un centro cuando exista disponibilidad para atenderlo. | Cada centro de salud | F-01 | Por validar |
| RG-02 | La información de ocupación y disponibilidad debe ser proporcionada o actualizada por los centros correspondientes. | Cada centro de salud | F-01 | Por validar |
| RG-03 | Los datos que identifiquen a pacientes no deben exponerse públicamente. | Centro de salud y normativa de privacidad aplicable (por confirmar, ver P-04) | F-01 | Por validar |

**Relación con los requisitos:** RG-01 condiciona RF-06; RG-02 condiciona RF-03 y RF-04 (de dónde viene el dato); RG-03 condiciona RNF-01. Las reglas **no** se cuentan como requisitos adicionales: RNF-01 expresa la condición verificable de RG-03, no un comportamiento repetido.

---

## E. Catálogo de requisitos priorizado

Equipo de cuatro integrantes: **8 requisitos** (7 funcionales y 1 no funcional), **dos por integrante**. RF y RNF se numeran por separado; los IDs no indican orden de ejecución.

| ID | Tipo | Requisito verificable | Origen (F / N) | Prioridad | Motivo | Autor | Estado |
|---|---|---|---|---|---|---|---|
| RF-01 | RF | El sistema debe permitir al usuario ingresar una ubicación y una especialidad médica para buscar centros de salud, y avisar con texto cuando falte alguno de los dos datos. | F-01 / N-02 | P1 | Es el punto de inicio del proceso; sin él no hay consulta. | Martínez Aquino Jonnatan | Por validar |
| RF-02 | RF | El sistema debe mostrar una lista de centros de salud que coincidan con la búsqueda (al menos tres cuando existan) e informar si hay menos resultados. | F-01 / N-02 | P1 | Permite comparar opciones; sin lista no se puede elegir centro. | Martínez Aquino Jonnatan | Por validar |
| RF-03 | RF | El sistema debe mostrar el nivel de saturación de cada centro con las categorías Bajo, Medio o Alto. | F-01 / N-01 | P1 | Es el valor central del proyecto; si se pospone, la primera versión no cumple su objetivo. | Ortiz Saucedo Jesús Adán | Por validar |
| RF-04 | RF | El sistema debe mostrar el tiempo estimado de espera de cada centro cuando exista información para calcularlo, e indicar «No disponible» cuando no exista. | F-01 / N-03 | P1 | Es la base del indicador de mejora de A.5. | Ortiz Saucedo Jesús Adán | Por validar |
| RF-05 | RF | El sistema debe mostrar el tiempo estimado de traslado desde la ubicación ingresada hasta cada centro de los resultados. | F-01 / N-04 | P2 | Ayuda a comparar, pero el usuario puede consultar saturación y solicitar turno sin este dato. | Obregón Estrada Emmanuel | Por validar |
| RF-06 | RF | El sistema debe permitir solicitar un turno solo en un centro con disponibilidad, y mostrar un aviso en texto cuando el centro seleccionado no tenga disponibilidad. | F-01 / N-05 (RG-01) | P1 | Sin esta condición el proceso no se completa o se confirmaría un turno inexistente (regla esencial RG-01). | Obregón Estrada Emmanuel | Por validar |
| RF-07 | RF | El sistema debe mostrar un mensaje de confirmación con un folio cuando una solicitud de turno se registre correctamente. | F-01 / N-05 | P2 | Informa al usuario el resultado; el registro funciona sin el folio, pero la comprobación posterior lo necesita. | García Villegas Jorge Ignacio | Por validar |
| RNF-01 | RNF | El sistema debe mostrar a usuarios no autorizados únicamente información del centro (nombre, ubicación, saturación y tiempos estimados) y no debe mostrar datos personales de pacientes. | F-01 / N-07 (RG-03) | P1 | Existe un riesgo grave de exposición de datos sensibles; es una regla esencial (RG-03). | García Villegas Jorge Ignacio | Por validar |


---

## F. Criterios de aceptación

Formato: Condición (Dado) → Acción (Cuando) → Resultado comprobable (Entonces).

| ID criterio | Requisito | Condición (Dado) | Acción (Cuando) | Resultado esperado (Entonces) |
|---|---|---|---|---|
| CA-RF-01a (éxito) | RF-01 | El usuario escribe una ubicación y elige una especialidad. | Presiona «Buscar centros». | El sistema ejecuta la búsqueda y muestra la lista de resultados. |
| CA-RF-01b (alternativa) | RF-01 | Falta la ubicación o la especialidad. | Presiona «Buscar centros». | No se ejecuta la búsqueda y aparece un texto que indica qué dato falta. |
| CA-RF-02a (éxito) | RF-02 | Existen al menos tres centros que coinciden con la búsqueda. | El usuario realiza la búsqueda. | Se muestran al menos tres centros. |
| CA-RF-02b (alternativa) | RF-02 | Coinciden menos de tres centros. | El usuario realiza la búsqueda. | Se muestran los centros existentes y un texto indica que hay pocos resultados. |
| CA-RF-03 | RF-03 | Existen datos de saturación de los centros mostrados. | El usuario consulta los resultados. | Cada centro muestra «Bajo», «Medio» o «Alto». |
| CA-RF-04a (éxito) | RF-04 | Un centro tiene información suficiente para estimar la espera. | El usuario consulta los resultados. | El centro muestra su tiempo estimado de espera. |
| CA-RF-04b (alternativa) | RF-04 | Un centro no tiene información para estimar la espera. | El usuario consulta los resultados. | El centro muestra el texto «No disponible» en lugar de un tiempo. |
| CA-RF-05a (éxito) | RF-05 | La ubicación es válida y hay resultados. | El usuario consulta los centros. | Cada centro muestra su tiempo estimado de traslado. |
| CA-RF-05b (alternativa) | RF-05 | La ubicación no es reconocida. | El usuario realiza la búsqueda. | No se muestran traslados y aparece un texto que pide corregir la ubicación. |
| CA-RF-06a (éxito) | RF-06 | El centro seleccionado tiene disponibilidad. | El usuario presiona «Solicitar turno». | Se registra la solicitud y se pasa a la confirmación (RF-07). |
| CA-RF-06b (alternativa) | RF-06 | El centro seleccionado no tiene disponibilidad. | El usuario presiona «Solicitar turno». | No se registra la solicitud; aparece «Este centro no tiene disponibilidad» y la opción «Elegir otro centro». |
| CA-RF-07 | RF-07 | Una solicitud se registró correctamente. | El sistema finaliza el registro. | Se muestra un mensaje de confirmación y un folio. |
| CA-RNF-01 | RNF-01 | Un usuario sin autorización consulta resultados o intenta abrir una solicitud ajena. | Realiza la consulta. | Solo ve datos del centro; no se muestra ningún dato personal de pacientes. |


---

## G. Backlog y boceto

### G.1 Backlog

Ordenado por prioridad y dependencias reales (no por ID). En U3 las tareas son de especificación; no se programa.

| Orden | ID | Actividad (tarea del equipo) | Prioridad | Depende de | Trello |
|---|---|---|---|---|---|
| 1 | RF-01 | Documentar y verificar el requisito de búsqueda por ubicación y especialidad. | P1 | Ninguno | Tarjetas «Redactar Catálogo de Requisitos (E)» y «Definir Criterios de Aceptación (F)» · URL: [pegar] |
| 2 | RF-02 | Documentar el requisito de lista de centros. | P1 | RF-01 | Tarjetas «Redactar Catálogo de Requisitos (E)» y «Definir Criterios de Aceptación (F)» · URL: [pegar] |
| 3 | RF-03 | Documentar el requisito de nivel de saturación. | P1 | RF-02 | Tarjetas «Redactar Catálogo de Requisitos (E)» y «Definir Criterios de Aceptación (F)» · URL: [pegar] |
| 4 | RF-04 | Documentar el requisito de tiempo de espera. | P1 | RF-02 | Tarjetas «Redactar Catálogo de Requisitos (E)» y «Definir Criterios de Aceptación (F)» · URL: [pegar] |
| 5 | RF-06 | Documentar el requisito de solicitud de turno y caso sin disponibilidad. | P1 | RF-02 | Tarjetas «Redactar Catálogo de Requisitos (E)» y «Definir Criterios de Aceptación (F)» · URL: [pegar] |
| 6 | RNF-01 | Documentar y definir la prueba de protección de datos personales. | P1 | Ninguno | Tarjetas «Redactar Catálogo de Requisitos (E)» y «Definir Criterios de Aceptación (F)» · URL: [pegar] |
| 7 | RF-05 | Documentar el requisito de tiempo de traslado. | P2 | RF-01, RF-02 | Tarjetas «Redactar Catálogo de Requisitos (E)» y «Definir Criterios de Aceptación (F)» · URL: [pegar] |
| 8 | RF-07 | Documentar el requisito de confirmación con folio. | P2 | RF-06 | Tarjetas «Redactar Catálogo de Requisitos (E)» y «Definir Criterios de Aceptación (F)» · URL: [pegar] |


### G.2 Boceto del recorrido prioritario

**Nombre del recorrido:** recorrido del usuario mediante wireframes de baja fidelidad. Los datos mostrados (centros, tiempos, folio) son **ficticios** y solo ilustran la estructura. No es una aplicación funcional.



| Estado | Qué representa | Requisitos | Flecha de salida |
|---|---|---|---|
| 01 · Inicio | Pantalla donde el usuario escribe ubicación y especialidad. | RF-01 | «Buscar» → 02 |
| 02 · Acción | Lista de centros con saturación, espera y traslado, y botón «Solicitar turno». | RF-02, RF-03, RF-04, RF-05, RF-06 | Con disponibilidad → 03A; sin disponibilidad → 03B |
| 03A · Éxito | Confirmación de la solicitud con folio. | RF-07 | «Ver estado» → 04 |
| 03B · Error | Aviso en texto de que no hay disponibilidad y botón «Elegir otro centro». | RF-06, RG-01 | Regresa a 02 |
| 04 · Consulta | Consulta posterior del estado con el folio. **Provisional · pendiente de validar** (sin RF propio). | — | Fin |

---

## H. Trazabilidad y cambios

### H.1 Matriz de trazabilidad

| Fuente (B2) | Necesidad (B3) | ID (E) | Criterio (F) | Boceto o comprobación (G) |
|---|---|---|---|---|
| F-01 | N-02 | RF-01 | CA-RF-01a, CA-RF-01b | Estado 01 |
| F-01 | N-02 | RF-02 | CA-RF-02a, CA-RF-02b | Estado 02 |
| F-01 | N-01 | RF-03 | CA-RF-03 | Estado 02 |
| F-01 | N-03 | RF-04 | CA-RF-04a, CA-RF-04b | Estado 02 |
| F-01 | N-04 | RF-05 | CA-RF-05a, CA-RF-05b | Estado 02 |
| F-01 (RG-01) | N-05 | RF-06 | CA-RF-06a, CA-RF-06b | Estados 02 y 03B |
| F-01 | N-05 | RF-07 | CA-RF-07 | Estado 03A |
| F-01 (RG-03) | N-07 | RNF-01 | CA-RNF-01 | No representable en boceto; prueba propuesta: con un usuario sin autorización, revisar que los resultados y cualquier solicitud ajena no muestren datos personales de pacientes. |

### H.2 Historial de cambios

| Versión | Fecha | Motivo / cambio | IDs afectados | Decisión | Enlace al PR |
|---|---|---|---|---|---|
| 0.1 | 2026-11-03 | Estructura inicial A–I y documentación preliminar. | Todos | Creación del documento | Pendiente |
| 0.2 | 2026-11-16 | Corrección tras revisión contra el material de clase: B1–B4, IDs de necesidades, autores, criterios con alternativas, RNF-01 verificable, prioridades, backlog, trazabilidad y boceto. | RF-01 a RF-07, RNF-01 | RF-05 baja a P2; RF-06 y RF-07 se reformulan; F-02 a F-04 pasan a plan (B1) | Pendiente |
| 1.0 | Pendiente | Integración final con consultas reales y revisión entre pares. | — | — | Pendiente |

### H.3 Revisión entre pares

Antes de marcar un requisito como validado, otro integrante revisa que:

- describa una sola necesidad;
- sea claro y verificable;
- tenga una fuente real identificada;
- tenga prioridad justificada y criterio de aceptación;
- no duplique una regla del dominio ni otro requisito.

**Estado de revisión:** pendiente de revisión entre integrantes (PR abierto o por abrir).

---

## I. Referencias y herramientas

### I.1 Fuentes consultadas

| Referencia | Descripción | Uso |
|---|---|---|
| U2-E01 | Inicio del modelado del negocio, proyecto XALTIL. Equipo Webtons, 2026-10-07. | Proceso AS-IS/TO-BE, partes interesadas, necesidades y supuestos. |
| SCC-1007 | Material de clase de la Unidad 3: Ingeniería de Requisitos. | Estructura documental, clasificación, priorización y criterios de aceptación. |


### I.2 Herramientas utilizadas

| Herramienta | Proveedor | Uso real en el proyecto | Enlace oficial |
|---|---|---|---|
| GitHub | GitHub, Inc. | Almacenamiento, ramas y revisión mediante Pull Requests. |https://github.com/rocketquee/fis-2026-e03-XALTIL.git|
| Trello | Atlassian | Tablero de tareas, responsables y revisiones. | https://trello.com/invite/b/6ab3e1e69ddbfdfb65d743b3/ATTI15901626cd3b02df1fcdb142d9ead4393461F259/xaltil |
| Claude | Anthropic | Apoyo en la revisión de coherencia con el material de clase y en el borrador de redacción y del boceto. | https://claude.ai/ |



### I.3 Consideraciones finales

Esta especificación parte del análisis de U2 y es la base para continuar con la obtención y validación de necesidades. Los requisitos marcados «Por validar» deben contrastarse con pacientes, familiares, personal administrativo y representantes de centros de salud antes de considerarse definitivos. El equipo mantiene este documento como la especificación integrada del proyecto y lo actualiza conforme obtenga evidencia y realice revisiones.
