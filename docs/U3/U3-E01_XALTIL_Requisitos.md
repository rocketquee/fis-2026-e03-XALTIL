# U3 · Especificación de requisitos — XALTIL

**Equipo:** Webtons  
**Proyecto:** XALTIL  
**Versión:** 0.1  
**Fecha:** 03/11/2026  
**Estado del documento:** En elaboración  
**Unidad:** 3 · Ingeniería de Requisitos  
**Materia:** Fundamentos de Ingeniería de Software (SCC-1007)

**Integrantes:**
- García Villegas Jorge Ignacio --- Calidad y Documentacion
- Martínez Aquino Jonnatan -------- Desarrollo
- Obregon Estrada Emmanuel -------- Cordinacion
- Ortiz Saucedo Jesús Adán -------- Analisis

**Responsable de integración:**  Jonnatan Martinez Aquino(desarrollo)
**Responsable de revisión:**  Garcia Villegas Jorge Ignacion (Calidad y Docucemntacion)

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

**Ruta elegida:** A

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
