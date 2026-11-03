# U3 · Especificación de requisitos — XALTIL

**Equipo:** Webtons  
**Proyecto:** XALTIL  
**Versión:** 0.1  
**Fecha:** 03/11/2026  
**Estado del documento:** En elaboración  
**Unidad:** 3 · Ingeniería de Requisitos  
**Materia:** Fundamentos de Ingeniería de Software (SCC-1007)

**Integrantes:**
- García Villegas Jorge Ignacio
- Martínez Aquino Jonnatan
- Obregon Estrada Emmanuel
- Ortiz Saucedo Jesús Adán

**Responsable de integración:** Por asignar  
**Responsable de revisión:** Por asignar  

---

## A. Identificación y alcance

### A.1 Identificación del proyecto

XALTIL es una propuesta de plataforma web orientada a facilitar la consulta de disponibilidad y saturación de centros de salud. Su propósito es proporcionar información centralizada para que los pacientes y familiares puedan comparar opciones de atención antes de desplazarse.

El sistema contempla mostrar información sobre los centros de salud cercanos, su nivel de saturación, el tiempo estimado de espera y el tiempo de traslado. También considera la posibilidad de solicitar un turno o cita cuando exista disponibilidad.

### A.2 Proceso TO-BE seleccionado

**Proceso:** Consulta de disponibilidad y solicitud de turno en centros de salud.

El proceso comienza cuando el usuario ingresa su ubicación y la especialidad médica que necesita. Posteriormente, el sistema consulta y presenta los centros de salud disponibles, junto con información sobre su saturación y tiempos estimados. Finalmente, el usuario puede seleccionar un centro y solicitar un turno.

### A.3 Objetivo de esta especificación

Documentar y organizar los requisitos funcionales y no funcionales necesarios para definir el comportamiento esperado de XALTIL, estableciendo sus prioridades, fuentes, responsables y criterios de aceptación.

### A.4 Alcance

**Dentro del alcance:**
- Consultar centros de salud utilizando una ubicación ingresada por el usuario.
- Filtrar o consultar centros según la especialidad requerida.
- Mostrar centros de salud cercanos.
- Visualizar el nivel de saturación de los centros.
- Consultar el tiempo estimado de espera.
- Mostrar el tiempo estimado de traslado.
- Solicitar un turno o cita cuando exista disponibilidad.
- Mostrar una confirmación de la solicitud realizada.
- Proteger la información que no debe ser de acceso público.

**Fuera del alcance:**
- Realizar diagnósticos médicos.
- Sustituir los sistemas internos de administración hospitalaria.
- Garantizar la eliminación de los tiempos de espera.
- Garantizar que todos los centros de salud compartan información en tiempo real.
- Administrar tratamientos o historiales clínicos.
- Garantizar la atención médica de un paciente.

### A.5 Indicador de mejora

La mejora se evaluará mediante la diferencia entre el tiempo de espera estimado que muestra XALTIL y el tiempo real que espera el paciente en el centro de salud.

**Estado del alcance:** Definido inicialmente con base en el documento U2-E01. Pendiente de validación con los stakeholders.

---

## B. Fuentes y necesidades

Las necesidades documentadas se obtuvieron inicialmente del análisis del negocio realizado en la Unidad 2. Todavía es necesario contrastarlas con usuarios y representantes de los centros de salud.

### B.1 Registro de fuentes

| ID | Técnica o documento | Fecha | Hallazgo o necesidad | Estado | Enlace o referencia |
|---|---|---|---|---|---|
| F-01 | Documento U2-E01: Inicio del modelado del negocio | 07/10/2026 | Se identificó la falta de información centralizada sobre saturación, disponibilidad y tiempos de espera de los centros de salud. | Documentado; pendiente de validación con usuarios | docs/U2/ |
| F-02 | Entrevista a pacientes o familiares | Por realizar | Identificar qué información necesitan consultar antes de acudir a un centro de salud. | Pendiente | Por registrar |
| F-03 | Consulta al personal administrativo o de recepción | Por realizar | Conocer cómo se registra y actualiza actualmente la ocupación y disponibilidad. | Pendiente | Por registrar |
| F-04 | Consulta a directivos o administradores de centros de salud | Por realizar | Identificar condiciones y restricciones para compartir información de ocupación. | Pendiente | Por registrar |

### B.2 Necesidades identificadas

A partir del análisis realizado en U2, se identifican las siguientes necesidades:

1. Los pacientes necesitan conocer la saturación de los centros de salud antes de desplazarse.
2. Los usuarios necesitan consultar información de diferentes centros desde una misma plataforma.
3. Los pacientes necesitan conocer el tiempo estimado de espera.
4. Los usuarios necesitan conocer el tiempo aproximado de traslado.
5. Los pacientes necesitan identificar centros que cuenten con disponibilidad para solicitar un turno.
6. El personal administrativo necesita que la actualización de información no represente una carga adicional considerable.
7. Los centros de salud necesitan mantener protegida la información que no debe ser pública.

### B.3 Suposiciones pendientes de comprobar

- Los hospitales y clínicas estarán dispuestos a compartir sus datos de ocupación.
- La información podrá actualizarse con la frecuencia necesaria.
- Será posible integrar información de centros que utilizan diferentes sistemas internos.
- Se podrán cumplir las condiciones de privacidad y confidencialidad aplicables.

Estas suposiciones no se consideran requisitos confirmados hasta contar con evidencia de las fuentes correspondientes.

---

## C. Organización del alcance

**Ruta elegida:** A (con épica).

**Motivo de elección:**

Se selecciona la Ruta A porque el proceso de XALTIL agrupa varias capacidades relacionadas que deben organizarse y analizarse por separado. El proceso no se limita a una sola consulta, ya que contempla búsqueda, visualización de información, consulta de disponibilidad y solicitud de turnos.

### C.1 Épica

**EP-01 · Consultar centros de salud y gestionar solicitudes de turno.**

**Objetivo:**

Permitir que los pacientes y familiares encuentren centros de salud cercanos, consulten su situación de ocupación y disponibilidad, y soliciten un turno antes de desplazarse.

### C.2 Capacidades desglosadas

| ID | Capacidad | Descripción | Requisitos vinculados |
|---|---|---|---|
| CAP-01 | Búsqueda de centros | Consultar centros mediante ubicación y especialidad. | RF-01, RF-02 |
| CAP-02 | Consulta de información | Visualizar saturación y tiempos estimados. | RF-03, RF-04, RF-05 |
| CAP-03 | Solicitud de turno | Solicitar un turno cuando exista disponibilidad. | RF-06, RF-07 |
| CAP-04 | Protección de información | Evitar la exposición pública de datos personales. | RNF-01 |

La épica organiza las necesidades del proyecto, mientras que los requisitos funcionales y no funcionales especifican los comportamientos y condiciones que deberán comprobarse.

---

## D. Reglas del dominio

Las siguientes reglas se derivan del proceso descrito en U2-E01. Su aplicación y detalle deberán confirmarse con los responsables de los centros de salud.

| ID | Regla del contexto | Fuente | Estado |
|---|---|---|---|
| RG-01 | Un paciente solamente podrá solicitar un turno en un centro de salud cuando exista disponibilidad para atenderlo. | F-01 | Por validar |
| RG-02 | La información de ocupación y disponibilidad debe ser proporcionada o actualizada por los centros de salud correspondientes. | F-01 | Por validar |
| RG-03 | La información que permita identificar datos personales de pacientes no deberá exponerse públicamente. | F-01 | Por validar |

**Observación:** Las reglas del dominio establecen condiciones del contexto. No deben contabilizarse como requisitos adicionales cuando describan exactamente el mismo comportamiento de un requisito funcional.

---

## E. Catálogo de requisitos priorizado

El equipo está conformado por cuatro integrantes, por lo que se establece un catálogo inicial de ocho requisitos: siete funcionales y uno no funcional.

Los requisitos se presentan como propuestas derivadas del proceso TO-BE de U2. Su redacción, prioridad y aceptación definitiva quedan sujetas a validación.

### E.1 Requisitos funcionales

| ID | Tipo | Requisito verificable | Fuente | Prioridad | Motivo | Autor | Estado |
|---|---|---|---|---|---|---|---|
| RF-01 | Funcional | El sistema debe permitir al usuario ingresar una ubicación y una especialidad médica para realizar una búsqueda de centros de salud. | F-01 | P1 | Es el punto de inicio del proceso de consulta. | Por asignar | Por validar |
| RF-02 | Funcional | El sistema debe mostrar una lista de al menos tres centros de salud que coincidan con los criterios de búsqueda, cuando existan suficientes resultados. | F-01 | P1 | Permite comparar diferentes opciones de atención. | Por asignar | Por validar |
| RF-03 | Funcional | El sistema debe mostrar el nivel de saturación de cada centro de salud mediante las categorías Bajo, Medio o Alto. | F-01 | P1 | Permite identificar visualmente la ocupación de los centros. | Por asignar | Por validar |
| RF-04 | Funcional | El sistema debe mostrar el tiempo estimado de espera de cada centro de salud cuando exista información disponible para calcularlo. | F-01 | P1 | Permite que el usuario valore cuánto podría esperar para recibir atención. | Por asignar | Por validar |
| RF-05 | Funcional | El sistema debe mostrar el tiempo estimado de traslado desde la ubicación ingresada por el usuario hasta cada centro de salud de los resultados. | F-01 | P1 | Ayuda a comparar las opciones considerando el desplazamiento. | Por asignar | Por validar |
| RF-06 | Funcional | El sistema debe permitir al usuario solicitar un turno en un centro de salud cuando exista disponibilidad. | F-01 | P1 | Es una de las capacidades principales del proceso TO-BE. | Por asignar | Por validar |
| RF-07 | Funcional | El sistema debe mostrar un mensaje de confirmación cuando una solicitud de turno se haya registrado correctamente. | F-01 | P2 | Informa al usuario que su solicitud fue procesada. | Por asignar | Por validar |

### E.2 Requisito no funcional

| ID | Tipo | Requisito verificable | Fuente | Prioridad | Motivo | Autor | Estado |
|---|---|---|---|---|---|---|---|
| RNF-01 | No funcional | El sistema debe proteger los datos personales de los pacientes y evitar que información confidencial sea visible para usuarios no autorizados. | F-01 | P1 | La confidencialidad es necesaria para evitar la exposición de información sensible. | Por asignar | Por validar |

**Nota sobre las prioridades:**

- **P1 · Alta:** Requisito indispensable para cumplir el objetivo principal de la primera versión.
- **P2 · Media:** Aporta valor, pero puede desarrollarse después de los requisitos P1.
- **P3 · Baja:** Mejora opcional que puede incorporarse en una versión futura.

Las prioridades anteriores son iniciales y deberán revisarse después de consultar las fuentes pendientes.

---

## F. Criterios de aceptación

Los siguientes criterios permiten comprobar el comportamiento esperado de cada requisito. Se presentan como pruebas propuestas para la validación del equipo.

| Requisito | Entrada o condición | Acción | Resultado esperado |
|---|---|---|---|
| RF-01 | El usuario dispone de una ubicación y una especialidad médica. | Ingresa ambos datos y realiza la búsqueda. | El sistema recibe los datos y ejecuta la consulta de centros de salud. |
| RF-02 | Existen al menos tres centros que coinciden con los criterios de búsqueda. | El usuario realiza una consulta. | El sistema muestra al menos tres centros de salud coincidentes. |
| RF-03 | Existen datos de saturación para los centros consultados. | El usuario visualiza los resultados. | Cada centro muestra su nivel de saturación como Bajo, Medio o Alto. |
| RF-04 | Un centro cuenta con información suficiente para estimar el tiempo de espera. | El usuario consulta los resultados. | El sistema muestra el tiempo estimado de espera correspondiente. |
| RF-05 | El usuario ingresó una ubicación válida y existen resultados de búsqueda. | El usuario consulta los centros encontrados. | Cada centro muestra su tiempo estimado de traslado desde la ubicación ingresada. |
| RF-06 | El centro seleccionado tiene disponibilidad de turnos. | El usuario selecciona el centro y solicita un turno. | El sistema procesa la solicitud y permite continuar con el registro del turno. |
| RF-07 | Una solicitud de turno se registró correctamente. | El sistema finaliza el registro. | Se muestra un mensaje que confirma que la solicitud fue realizada correctamente. |
| RNF-01 | Un usuario sin autorización intenta acceder a información personal de pacientes. | Se intenta consultar información confidencial. | El sistema impide el acceso y no muestra los datos protegidos. |

**Observación:** Los criterios describen resultados esperados. Las condiciones técnicas, reglas de autorización y disponibilidad de datos deberán precisarse durante la validación con los stakeholders.

---

## G. Backlog y boceto

### G.1 Backlog inicial

El siguiente backlog organiza el trabajo del equipo según la prioridad de los requisitos y el recorrido principal del usuario.

| Orden | ID | Actividad | Prioridad | Dependencia | Estado |
|---|---|---|---|---|---|
| 1 | RF-01 | Implementar la consulta por ubicación y especialidad. | P1 | Ninguna | To Do |
| 2 | RF-02 | Mostrar los centros de salud encontrados. | P1 | RF-01 | To Do |
| 3 | RF-03 | Incorporar la visualización de saturación. | P1 | RF-02 | To Do |
| 4 | RF-04 | Mostrar los tiempos estimados de espera. | P1 | RF-02 | To Do |
| 5 | RF-05 | Mostrar los tiempos estimados de traslado. | P1 | RF-01, RF-02 | To Do |
| 6 | RF-06 | Permitir la solicitud de turnos. | P1 | Disponibilidad del centro | To Do |
| 7 | RF-07 | Mostrar la confirmación de solicitud. | P2 | RF-06 | To Do |
| 8 | RNF-01 | Comprobar la protección de información confidencial. | P1 | Diseño de acceso a información | To Do |

**Nota:** Los estados son una propuesta inicial para organizar el trabajo. Deben actualizarse conforme avance el equipo en Trello.

### G.2 Organización en Trello

Cada requisito deberá contar con una tarjeta de trabajo que incluya:

- Identificador del requisito.
- Título de la actividad.
- Integrante responsable.
- Integrante revisor.
- Resultado esperado.
- Enlace al requisito correspondiente.
- Evidencia del Pull Request cuando se integre el trabajo.

**Tarjeta de referencia de U2:** `[ACT-12][U2-E01] Modelar el negocio del proyecto`.

**Tarjetas correspondientes a U3:** Pendientes de crear y vincular.

### G.3 Boceto del recorrido prioritario

**Recorrido principal del usuario en XALTIL:**

```text
          INICIO
             |
             v
  Ingresar ubicación y especialidad
             |
             v
       Buscar centros
             |
             v
    Mostrar centros cercanos
             |
             v
  Consultar información de cada uno
  - Nivel de saturación
  - Tiempo estimado de espera
  - Tiempo estimado de traslado
             |
             v
      Seleccionar centro
             |
             v
    ¿Existe disponibilidad?
          /       \
        NO         SÍ
        |           |
        v           v
  Mostrar aviso   Solicitar turno
  de falta de          |
  disponibilidad       v
        |        Confirmar solicitud
        |               |
        v               v
   Elegir otro        FIN
      centro
```

**Objetivo del boceto:** Representar el recorrido prioritario desde la búsqueda de centros de salud hasta la solicitud de un turno, incluyendo la decisión de disponibilidad.

**Ubicación del material gráfico:** `docs/U3/prototipo/`

El boceto es una representación inicial del proceso y no constituye una aplicación funcional.

---

## H. Trazabilidad y cambios

### H.1 Matriz de trazabilidad

Esta matriz permite relacionar las fuentes de información con las reglas, requisitos y criterios de aceptación.

| Fuente | Necesidad o regla | Requisito relacionado | Criterio de aceptación |
|---|---|---|---|
| F-01 | Consultar centros mediante ubicación y especialidad. | RF-01 | CA-RF-01 |
| F-01 | Visualizar diferentes centros de salud. | RF-02 | CA-RF-02 |
| F-01 | Conocer la saturación de los centros. | RF-03 | CA-RF-03 |
| F-01 | Consultar el tiempo estimado de espera. | RF-04 | CA-RF-04 |
| F-01 | Conocer el tiempo de traslado. | RF-05 | CA-RF-05 |
| F-01 | Solicitar un turno cuando exista disponibilidad. | RG-01, RF-06 | CA-RF-06 |
| F-01 | Recibir confirmación de la solicitud. | RF-07 | CA-RF-07 |
| F-01 | Proteger información confidencial. | RG-03, RNF-01 | CA-RNF-01 |

### H.2 Historial de cambios

| Versión | Fecha | Cambio realizado | Responsable |
|---|---|---|---|
| 0.1 | 03/11/2026 | Creación de la estructura inicial A-I y documentación preliminar del alcance, fuentes y requisitos. | Equipo Webtons |
| 0.2 | Pendiente | Incorporación de resultados de consultas y validación de requisitos. | Por asignar |
| 1.0 | Pendiente | Revisión final e integración de la especificación del equipo. | Por asignar |

### H.3 Revisión entre pares

Antes de considerar validado un requisito, otro integrante deberá revisar:

- Que el requisito describa una sola necesidad.
- Que su redacción sea clara y verificable.
- Que tenga una fuente identificada.
- Que la prioridad esté justificada.
- Que tenga un criterio de aceptación.
- Que no duplique una regla del dominio o algún otro requisito.

Los cambios deberán registrarse en el historial y reflejarse tanto en el catálogo como en los criterios de aceptación y la matriz de trazabilidad.

**Estado de revisión:** Pendiente de revisión entre integrantes.

---

## I. Referencias y herramientas

### I.1 Fuentes del proyecto

| Referencia | Descripción | Uso |
|---|---|---|
| U2-E01 | Inicio del modelado del negocio — Proyecto XALTIL. Equipo Webtons, 07/10/2026. | Identificación del proceso AS-IS, TO-BE, stakeholders, necesidades y supuestos. |
| SCC-1007 | Material de clase de la Unidad 3: Ingeniería de Requisitos. | Estructura documental, clasificación, priorización y criterios de aceptación. |

### I.2 Herramientas utilizadas

| Herramienta | Uso dentro del proyecto |
|---|---|
| GitHub | Control de versiones, almacenamiento de documentación y revisión de cambios mediante Pull Requests. |
| Git | Administración de ramas y registro del historial de modificaciones. |
| Trello | Organización de actividades, responsables, revisiones y seguimiento del backlog. |
| Markdown | Elaboración de la especificación de requisitos. |

**Enlaces oficiales:**

- GitHub: https://github.com/
- Git: https://git-scm.com/
- Trello: https://trello.com/
- Markdown: https://www.markdownguide.org/

### I.3 Consideraciones finales

La presente especificación constituye el primer avance de requisitos del proyecto XALTIL.

Su contenido parte del análisis del negocio realizado en U2 y establece una base para continuar con la obtención, análisis, priorización y validación de necesidades.

Los requisitos identificados como pendientes deberán contrastarse con pacientes, familiares, personal administrativo y representantes de los centros de salud antes de considerarse definitivos.

El equipo mantendrá este documento como la especificación integrada del proyecto, actualizándolo conforme se obtenga nueva evidencia y se realicen revisiones.

---

**Documento elaborado por:** Equipo Webtons  
**Proyecto:** XALTIL  
**Materia:** Fundamentos de Ingeniería de Software  
**Unidad:** 3 · Ingeniería de Requisitos  
**Archivo:** `docs/U3/U3-E01_XALTIL_Requisitos.md`