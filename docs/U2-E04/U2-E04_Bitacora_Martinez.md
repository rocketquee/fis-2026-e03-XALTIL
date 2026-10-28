# Bitácora de Trabajo - Unidad 2: Modelado y Análisis del Negocio

**Alumno:** Martínez Aquino Jonnatan
**Equipo:** Webtons
**Proyecto:** XALTIL (Plataforma de consulta y reserva de turnos médicos)
**Materia:** Ingeniería de Software

## Registro de actividades

**Fecha de actualización:** [Pon la fecha de hoy, ej. 27 de Octubre de 2026]
**Evidencias atendidas:** U2-E02 (Análisis de Factibilidad y Riesgos Individual) y U2-E01 (Modelado del Negocio en Equipo)

### 1. Trabajo realizado y aportación individual

Durante el desarrollo de esta etapa del proyecto, mi enfoque principal se centró en la elaboración de la evidencia individual U2-E02, correspondiente al Análisis de Factibilidad y Riesgos. Mi aportación consistió en estructurar un documento analítico que evaluara la viabilidad real de la plataforma XALTIL desde cuatro dimensiones: técnica, operativa, económica y legal.

Para fundamentar este análisis con rigor académico, llevé a cabo una investigación autónoma que me permitió recopilar y estructurar fuentes bibliográficas en formato APA 7. Destaca la consulta de la *Ley Federal de Protección de Datos Personales en Posesión de los Particulares*, la cual fue crucial para identificar el riesgo legal inherente al manejo de información médica sensible (un aspecto que el equipo no había considerado a fondo). Asimismo, investigué documentación técnica oficial de Amazon Web Services (AWS) sobre pruebas de carga y escalabilidad. Esta investigación me permitió proponer soluciones concretas y viables al riesgo de saturación del servidor durante los picos de demanda (por ejemplo, en temporadas de influenza).

En cuanto a la redacción del documento individual, no solo me limité a enlistar los riesgos, sino que construí una matriz de factibilidad que resume el nivel de viabilidad de cada dimensión, concluyendo que el proyecto es técnicamente viable pero que su éxito operativo depende completamente de la voluntad de los hospitales para compartir sus datos.

De forma paralela, en el trabajo colaborativo, participé activamente en la revisión y refinamiento del archivo Markdown del U2-E01. Durante la sesión de revisión en equipo, analizamos el diagrama TO-BE (que incluye los carriles de responsabilidad). Detectamos un error de coherencia metodológica: el carril izquierdo del diagrama arrastraba el nombre de "Auxiliar administrativo" (un rol perteneciente al ejemplo de facturas que el profesor utilizó como referencia en clase). Mi aportación crítica fue señalar esta incongruencia y proponer el cambio a "Paciente" para alinear el diagrama con nuestra área de dominio de citas médicas. Además, verifiqué que las condiciones de las decisiones (como la validación de disponibilidad) tuvieran sus flechas de retorno lógicas para garantizar que el flujo del proceso fuera comprensible.

### 2. Evidencia de la aportación

El trabajo realizado se encuentra respaldado por los siguientes entregables:
- **Archivo `U2-E02_Martinez_Analisis.pdf`**: Documento formal de aproximadamente 3 páginas, formateado estrictamente bajo las normas solicitadas (Arial 12, interlineado 1.5, texto justificado). Incluye la definición de la regla de negocio, la tabla de los dos riesgos con sus respectivos planes de mitigación, la matriz de factibilidad y las cuatro fuentes consultadas en formato APA 7. Este archivo fue subido a la plataforma Classroom y resguardado en la carpeta `U2-E02` del repositorio.
- **Archivo `U2-E01_Webtons_ModeloNegocio.md`**: Documento del equipo actualizado en la carpeta `U2-E01`. Mi contribución se ve reflejada en la sección del TO-BE, donde se integró el diagrama corregido (con los archivos `as-is.png` y `to-be.png` debidamente enlazados en el código Markdown).
- **Declaración de IA**: Redactada de forma transparente y ética al final del documento individual, especificando el uso de Perplexity para la búsqueda de fuentes, pero aclarando que el análisis y la redacción final fueron realizados por el estudiante.

### 3. Revisión cruzada (Retroalimentación entre pares)

El trabajo no fue aislado; se sometió a un proceso de coevaluación para garantizar su calidad:
- **Revisión recibida:** Mi compañero Adan Ortiz revisó mi borrador del documento E02. Su observación fue que el texto era muy denso y las tablas estaban dispersas. Me sugirió agregar una "Matriz de Factibilidad" que resumiera los niveles de viabilidad (Alta, Media, Baja) para que el lector (en este caso, el profesor) pudiera identificar rápidamente las conclusiones del análisis. Acepté la sugerencia, rediseñé el documento y el resultado final quedó mucho más estructurado y profesional.
- **Revisión otorgada:** En reciprocidad, revisé la sección de riesgos del borrador de [Pon el nombre de otro compañero, ej. Jorge García]. Le señalé que sus acciones de prevención eran muy generales (decía "mejorar el sistema"). Le sugerí que especificara el mecanismo, es decir, que indicara *cómo* se prevendría (por ejemplo, añadir un indicador de "última actualización" y alertas automáticas si el dato tiene más de 2 horas de antigüedad). Considero que esta retroalimentación ayudó a elevar la calidad de su análisis.

### 4. Seguimiento y correcciones

- **Acciones corregidas:** Se editó el documento E02 para eliminar la palabra "equipo" de la declaración de IA, sustituyéndola por "el estudiante", para mantener la coherencia de que se trata de un trabajo individual. Asimismo, se ajustó el formato del texto para cumplir con las especificaciones de márgenes y tipografía. El PDF ya está listo en Classroom.
- **Acciones pendientes:** Queda pendiente que el compañero encargado de Documentación realice el `git push` final a la rama `main` del repositorio de GitHub para publicar el archivo Markdown del E01 junto con las imágenes de los diagramas. A nivel personal, el siguiente paso es estudiar los conceptos de AS-IS, TO-BE, la simbología UML y las alternativas de solución (construir, adquirir, adaptar, integrar) para presentar con éxito el examen presencial (U2-E03) programado para el día jueves.

### 5. Nota sobre el uso de Inteligencia Artificial y ajustes de redacción

Para la elaboración de este documento y del análisis individual (U2-E02), se utilizó una Inteligencia Artificial (IA) especializada en redacción y estructuración de textos académicos. El objetivo principal de apoyarnos en esta herramienta fue optimizar la organización de las ideas y elevar el nivel del lenguaje técnico utilizado en el proyecto.

Sin embargo, durante el proceso nos encontramos con ciertas limitaciones o "percances" técnicos de la herramienta. Específicamente, al solicitarle que redactara la bitácora, la IA generaba textos con *placeholders* o ejemplos genéricos (como el texto literal `[Pon el nombre de un compañero, ej. Emmanuel Obregón]`). Esto nos obligó a realizar una revisión crítica y manual del texto, ya que como autores del proyecto, tuvimos que reemplazar esos espacios con los nombres reales de nuestros compañeros y adaptar los ejemplos a las vivencias reales de nuestro equipo (Webtons).

Asimismo, aunque la IA fungió como un excelente apoyo para estructurar las tablas de riesgos y la matriz de factibilidad, el análisis profundo de la problemática (la saturación de hospitales), la elección de las fuentes legales en APA y la toma de decisiones sobre el diagrama TO-BE fueron redactados y validados enteramente por el equipo de manera crítica. Consideramos que el uso de estas herramientas es válido siempre que el estudiante mantenga el criterio, el pensamiento crítico y la responsabilidad ética sobre el producto final que entrega.
---
*Documento generado como evidencia de la bitácora individual (U2-E04) para la materia de Ingeniería de Software.*