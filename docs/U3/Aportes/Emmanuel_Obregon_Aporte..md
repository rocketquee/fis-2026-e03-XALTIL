# Aporte individual — Emmanuel Obregon Estrada

**Proyecto:** XALTIL
**Sección del proceso asignada:** Búsqueda de centros de salud y visualización de resultados (Alineado al RF-01 y RF-02).
**Rol principal de la U3:** Coordinación
**Fecha:** 2026-11-17

## 1. Información que necesito obtener
- **Pregunta 1:** ¿Qué datos exactos requiere un paciente para considerar que una búsqueda de centro de salud es exitosa? (Ej. ¿Basta con la especialidad, o requiere filtrar también por turno mañana/tarde?).
- **Pregunta 2:** Si un paciente busca en una zona donde no hay centros con esa especialidad, ¿qué espera que haga el sistema? (¿Mostrar los más cercanos aunque estén lejos, o un mensaje de "sin resultados"?).
- **Técnica elegida y motivo:** Análisis documental y revisión de requerimientos. Se elige esta técnica porque actualmente no tenemos acceso directo a una muestra grande de pacientes para entrevistar, pero el documento U2-E01 ya define claramente el proceso de negocio y la propuesta de valor.
- **Fuente a consultar:** Documento U2-E01 (Modelado del negocio).
- **Fecha prevista o estado:** Completado (basado en fuentes documentales del 07/10/2026). Pendiente la validación directa con un usuario (entrevista).

## 2. Información que ya tengo
- **Fuente real:** F-01 (Documento U2-E01 del equipo Webtons, con fecha del 07/10/2026. Respaldo en el repositorio de GitHub del equipo).
- **Hallazgo comprobable:** El proceso TO-BE inicia estrictamente cuando el usuario ingresa su ubicación y especialidad. La propuesta de valor del sistema se basa en que el usuario pueda comparar opciones *antes* de salir de casa para evitar desplazamientos innecesarios.
- **Dudas:** No está definido en el documento si la ubicación debe ingresarse por texto (ej. "Colonia Centro") o si el sistema obligará a usar el GPS del celular/mapa interactivo.

## 3. Necesidad identificada
**N-01:** El paciente necesita un mecanismo de búsqueda que reciba su ubicación y especialidad médica, y que le devuelva un listado claro y ordenado de los centros de salud que cumplen con esos criterios. Esto es indispensable para que pueda comparar sus opciones y decidir a dónde acudir, cumpliendo así con el objetivo del proyecto.