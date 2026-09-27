**Fecha:** 27 de septiembre de 2026, 1:18 p.m.  
**Actividad:** ACT-07  
**Actividad evaluada:** U1-E01  
**Caso:** Corrección de la estructura de carpetas del repositorio en GitHub  
**Responsabilidad:** Como Coordinación, verificar que la estructura de carpetas del repositorio coincidiera con lo definido en el README.md.

**Hallazgo:** Al revisar GitHub.com, se detectó que las carpetas `docs/U1-E01`, `docs/U1-E02`, `docs/U1-E04` y `gestion/acuerdos` no aparecían en el repositorio remoto, ya que estaban vacías y Git no rastrea carpetas sin contenido. Además, se encontró que las carpetas `Acuerdos` y `bitacoras` estaban ubicadas sueltas en la raíz del proyecto, en lugar de estar dentro de la carpeta `gestion` como correspondía.

**Decisión:** Crear la carpeta `gestion` y mover dentro de ella `acuerdos` (corrigiendo también el nombre, que estaba con mayúscula) y `bitacoras`. Se agregaron archivos `.gitkeep` en las carpetas vacías (`docs/U1-E01`, `docs/U1-E02`, `docs/U1-E04` y `gestion/acuerdos`) para que Git pudiera subirlas correctamente.

**Siguiente paso:** Confirmar que el contenido de cada carpeta sea el correcto, corregir las tarjetas duplicadas del tablero de Trello, y continuar con el análisis individual de U1-E02.

**Evidencia:** Repositorio en GitHub (`fis-2026-e03-XALTIL`) con la estructura completa visible: `docs/`, `gestion/acuerdos/`, `gestion/bitacoras/` y `README.md`.