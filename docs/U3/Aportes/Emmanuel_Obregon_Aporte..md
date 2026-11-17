# Aporte individual — Emmanuel Obregon Estrada
**Proyecto:** XALTIL
**Sección del proceso asignada:** Búsqueda y visualización de centros de salud (RF-01 y RF-02)
**Rol principal de la U3:** Coordinación
**Fecha:** 2026-11-17

## 1. Información que necesito obtener
- **Pregunta 1:** ¿Qué estándares técnicos existen para que un sistema permita a un paciente buscar y encontrar centros de salud por ubicación y especialidad?
- **Pregunta 2:** ¿Cómo deben presentarse los resultados de búsqueda para que el usuario pueda comparar opciones de atención de manera útil?
- **Técnica elegida y motivo:** Análisis documental de estándares internacionales de salud digital y guías de implementación. Se elige esta técnica porque permite fundamentar los requisitos con fuentes técnicas verificables y reconocidas en la industria, sin depender de entrevistas que aún no se han realizado.
- **Fuente a consultar:** Especificación SMART Scheduling Links de HL7 International (basada en el estándar FHIR) y documentos de la Organización Panamericana de la Salud (OPS) sobre sistemas de información en salud.
- **Fecha prevista o estado:** Completado (consulta realizada el 17/11/2026).

## 2. Información que ya tengo
- **Fuente real:**
  - **F-01:** Documento `U3-E01_XALTIL_Requisitos.md` del equipo Webtons (Sección E.1), consultado en el repositorio de GitHub (Noviembre 2026).
  - **F-02:** HL7 International. (2026). *SMART Scheduling Links* (v1.0.0). Recuperado de http://hl7.org/fhir/uv/smart-scheduling-links/
  - **F-03:** Organización Panamericana de la Salud (OPS). *IS4H Foundations: Sistemas de Información para la Salud*. Recuperado de https://www.paho.org/en/is4h-information-systems-health/is4h-foundations
- **Hallazgo comprobable:**
  - El estándar HL7 SMART Scheduling Links establece explícitamente que las herramientas de reserva deben permitir al paciente **"encontrar horarios de citas buscando por geografía, especialidad, sistema de salud, etc."** [citation:1][citation:8]. Además, define casos de prueba específicos para búsquedas por ubicación y por especialidad, donde el sistema debe filtrar resultados y presentar información suficiente para que el usuario seleccione [citation:6]. Esto respalda directamente la necesidad del **RF-01** (ingreso de ubicación y especialidad).
  - La OPS, a través de su marco IS4H, promueve sistemas de información **interconectados e interoperables** que permitan generar información estratégica para la salud pública [citation:4]. La falta de un sistema unificado obliga a los pacientes a desplazarse sin certeza, por lo que la visualización consolidada de opciones (RF-02) contribuye a reducir esa brecha de información.
- **Dudas:**
  - El documento del equipo no especifica si la lista de resultados debe incluir filtros adicionales (ej. tipo de institución, horario) ni el criterio de orden (ej. cercanía, tiempo de espera). Queda pendiente validar con el equipo de desarrollo y con usuarios reales.

## 3. Necesidad identificada
El paciente necesita una interfaz que le permita **ingresar su ubicación y la especialidad requerida de forma clara**, y que el sistema le devuelva **una lista comprensible de los centros de salud que coinciden con su búsqueda**, priorizando la utilidad para la toma de decisiones. Los estándares internacionales de salud digital (HL7 FHIR) confirman que la búsqueda por geografía y especialidad es un requisito fundamental en los sistemas modernos de agendamiento, y que los resultados deben presentarse con información suficiente para que el usuario pueda comparar y elegir [citation:1][citation:6]. Sin esta capacidad, XALTIL no podría cumplir su propuesta de valor de permitir al usuario decidir a qué centro acudir antes de desplazarse.
