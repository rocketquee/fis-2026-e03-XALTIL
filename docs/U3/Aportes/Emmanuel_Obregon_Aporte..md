# Aporte individual — Emmanuel Obregón Estrada

**Proyecto:** XALTIL (Plataforma web de consulta de disponibilidad hospitalaria).  
**Sección del proceso asignada:** Consulta de información y solicitud de turno (RF-05 y RF-06).  
**Rol principal de la U3:** Coordinación.  
**Fecha:** 2026-11-17

## 1. Información que necesito obtener

- **Pregunta 1:** ¿Cómo se calculará el tiempo estimado de traslado desde la ubicación ingresada por el usuario hasta cada centro de salud?
- **Pregunta 2:** ¿Cómo se comprobará que un centro tiene disponibilidad antes de permitir registrar una solicitud de turno?
- **Técnica elegida y motivo:** Análisis documental, porque permite revisar los requisitos del proyecto y consultar documentación técnica que respalde el cálculo de rutas y la gestión de disponibilidad.
- **Fuente a consultar:** Documento U3-E01 de XALTIL, documentación oficial de Google Maps Routes API y estándar HL7 FHIR R5.
- **Fecha prevista o estado:** Consulta documental realizada el 17/11/2026. Pendiente validar la información con usuarios y centros de salud.

## 2. Información que ya tengo

- **Fuente real:** Documento U3-E01: Especificación de requisitos — XALTIL, versión 0.2, del equipo Webtons (16/11/2026). También se consultó la documentación oficial de Google Maps Routes API y HL7 FHIR R5.
- **Hallazgo comprobable:** El proyecto establece que los usuarios necesitan conocer el tiempo aproximado de traslado (N-04) y que los pacientes necesitan identificar centros con disponibilidad para solicitar turno (N-05). Google Routes API permite calcular tiempos de traslado y HL7 FHIR contempla estados de disponibilidad mediante el recurso Slot.
- **Dudas:** Falta definir el medio de transporte para calcular los traslados y comprobar cómo los centros de salud actualizarán su disponibilidad.

## 3. Necesidad identificada

Los usuarios necesitan conocer el tiempo estimado de traslado hacia los centros de salud para comparar sus opciones. Además, requieren que el sistema permita solicitar turnos únicamente en centros que tengan disponibilidad, evitando solicitudes de atención inexistentes.
