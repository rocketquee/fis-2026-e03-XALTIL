# U2-E01: Inicio del modelado del negocio - Proyecto XALTIL

**Equipo:** Webtons  
**Proyecto:** XALTIL  
**Fecha:** 07/10/2026  
**Tarjeta de Trello:** `[ACT-12][U2-E01] Modelar el negocio del proyecto`

**Integrantes:**
- García Villegas Jorge Ignacio
- Martínez Aquino Jonnatan
- Obregon Estrada Emmanuel
- Ortiz Saucedo Jesús Adán

---

## Tabla de Contenido
1. [Delimitación del proceso](#1-delimitación-del-proceso)
2. [Stakeholders](#2-stakeholders)
3. [Propuesta de valor](#3-propuesta-de-valor)
4. [Suposiciones por comprobar](#4-suposiciones-por-comprobar)
5. [Proceso Actual (AS-IS)](#5-proceso-actual-as-is)
6. [Mejora Propuesta (TO-BE)](#6-mejora-propuesta-to-be)
7. [Preguntas para responder sin leer](#7-preguntas-para-responder-sin-leer)
8. [Verificación del avance (Parte D)](#8-verificación-del-avance-parte-d)

---

## 1. Delimitación del proceso

| Elemento | Respuesta del equipo |
| :--- | :--- |
| **Área u organización** | Centros de salud (hospitales y clínicas) y las personas que buscan atención médica. |
| **Proceso principal** | Consultar la saturación y disponibilidad de los centros de salud y asegurar un turno o agendar una cita. |
| **Inicio** | El usuario entra a la plataforma y busca un centro de salud según su ubicación y la especialidad que necesita. |
| **Entrada** | Ubicación del usuario, especialidad requerida y datos de ocupación y disponibilidad que comparten los centros de salud. |
| **Salida** | Nivel de saturación, tiempo de espera estimado, tiempo de traslado y un turno o cita confirmada. |
| **Final** | El usuario recibe la confirmación de su turno o cita, o decide acudir a otro centro porque no hay disponibilidad. |
| **Usuario directo** | Pacientes y familiares que necesitan atención médica oportuna. |
| **Otros stakeholders** | Personal administrativo y de recepción de los centros de salud, directivos y administradores de hospitales, equipo que mantiene la plataforma. |
| **Problema concreto** | No existe un sistema unificado con información en tiempo real sobre ocupación, disponibilidad y tiempos de espera, así que el usuario se desplaza sin saber si lo van a atender a tiempo. |
| **Valor esperado** | Que el usuario decida a qué centro ir antes de salir, con menos desplazamientos innecesarios y menos tiempo perdido. |
| **Indicador** | Diferencia entre el tiempo de espera que muestra la plataforma y el tiempo real que espera el paciente en el centro de salud. |

---

## 2. Stakeholders

| Stakeholder | Participación | Necesidad |
| :--- | :--- | :--- |
| **Paciente o familiar** | Usa la plataforma para consultar y reservar. | Saber si lo atenderán a tiempo antes de desplazarse. |
| **Personal administrativo y recepción** | Proporciona y actualiza los datos de ocupación y disponibilidad. | Que actualizar la información no le represente una carga extra. |
| **Directivos y administradores de hospitales** | Autorizan compartir la información y toman decisiones sobre la demanda. | Distribuir mejor la demanda sin exponer información que no deba ser pública. |
| **Equipo que mantiene la plataforma** | Mantiene y corrige la solución. | Detectar a tiempo datos desactualizados o fallas de integración. |
| **Instituciones y normas de protección de datos** | Establecen las reglas sobre qué información se puede manejar. | Que el sistema cumpla con la privacidad y la confidencialidad. |

---

## 3. Propuesta de valor

Para los pacientes y familiares que buscan atención médica, que actualmente enfrentan la falta de información centralizada sobre la ocupación y los tiempos de espera de los centros de salud, nuestro sistema permitirá decidir a qué centro acudir antes de salir de casa mediante una plataforma web que muestra la saturación, la disponibilidad y el tiempo estimado de traslado de cada centro.

La mejora se comprobará mediante la comparación entre el tiempo de espera que muestra la plataforma y el tiempo real que espera el paciente en el centro de salud.

**Lo que no prometemos:**
- Eliminar por completo las esperas en los centros de salud.
- Que la información sea exacta en todo momento, porque depende de que cada centro la comparta y la actualice.
- Reemplazar el registro o la atención que ya hace cada institución.

---

## 4. Suposiciones por comprobar

> **Nota:** Esto todavía no lo hemos comprobado, por eso lo registramos como suposición.

- Que los hospitales y clínicas estarán dispuestos a compartir sus datos de ocupación.
- Que los datos se podrán actualizar con la frecuencia necesaria para que sean útiles.
- Que se podrá integrar la información de centros que usan sistemas internos distintos.
- Que se pueden cumplir los requisitos legales de privacidad con los datos que se muestren.

---

## 5. Proceso Actual (AS-IS)

En la situación actual, el paciente no tiene una herramienta unificada, por lo que el proceso suele ser el siguiente:

| Paso | Responsable en el proceso actual | Actividad y documento/datos que utiliza |
| :---: | :--- | :--- |
| **1** | Paciente o familiar | Busca información en internet o pregunta a conocidos sobre centros de salud. |
| **2** | Paciente o familiar | Llama por teléfono al centro de salud para preguntar disponibilidad. |
| **3** | Paciente o familiar | Se desplaza al centro de salud sin saber si hay saturación o disponibilidad. |
| **4** | Personal de recepción | Recibe al paciente, verifica la disponibilidad en su sistema interno y le informa. |
| **5** | Paciente o familiar | Espera su turno en el centro de salud. |

**Decisión y Regla del proceso actual:**
- **Condición que se comprueba:** ¿Hay disponibilidad en el centro de salud?
- **Si se cumple:** El paciente espera su turno (Paso 5).
- **Si no se cumple:** El paciente debe buscar otro centro y reiniciar el proceso.
- **Regla:** Solo se puede atender a un paciente si el centro tiene un turno disponible en ese momento.

**Consultas pendientes:** 
- No sabemos con certeza qué porcentaje de centros de salud usan sistemas digitales para registrar su ocupación actualmente.

---

## 6. Mejora Propuesta (TO-BE)

**Descripción de la mejora:** 
El sistema centraliza la información de los centros de salud. En lugar de que el paciente llame o se desplace a ciegas, la plataforma web muestra en tiempo real la saturación, el tiempo estimado de espera y el tiempo de traslado. El paciente decide desde su casa y solicita su turno o cita en línea.

<p align="center">
  <img src="![alt text](image.png)" alt="Diagrama TO-BE del proceso de citas médicas" width="80%">
  <br>
  <em>Figura 1: Diagrama de actividades UML del proceso TO-BE con carriles de responsabilidad (Paciente y Sistema).</em>
</p>

**Requisito:** 
El sistema debe permitir visualizar el nivel de saturación y el tiempo estimado de traslado de los centros de salud más cercanos a la ubicación ingresada por el paciente antes de solicitar un turno.

**Prueba propuesta:** 
Ingresar la ubicación "Centro de la ciudad" y la especialidad "Medicina General". El sistema debe mostrar una lista con al menos 3 centros de salud, su nivel de saturación (Bajo, Medio, Alto) y un tiempo estimado de traslado. Al seleccionar uno con disponibilidad, debe permitir generar la solicitud de turno y mostrar un mensaje de confirmación.

---

## 7. Preguntas para responder sin leer

1. **¿Qué proceso estudia?** La consulta de disponibilidad y la reserva de un turno en un centro de salud.
2. **¿Dónde comienza y termina?** Comienza cuando el usuario busca un centro y termina cuando recibe su turno o decide ir a otro lado.
3. **¿Quién lo utiliza?** Pacientes y familiares.
4. **¿Quién más resulta interesado o afectado?** El personal y los directivos de los centros de salud, y el equipo que mantiene la plataforma.
5. **¿Qué problema existe?** No hay información unificada en tiempo real, y el usuario se desplaza sin saber si lo atenderán a tiempo.
6. **¿Qué valor aportaría el software?** Permitir decidir a dónde ir antes de salir, con menos desplazamientos innecesarios.
7. **¿Cómo se comprobaría la mejora?** Comparando el tiempo de espera mostrado con el tiempo real.

---

## 8. Verificación del avance (Parte D)

- **Contenido:** El alcance del proceso, el problema y el indicador coinciden en todas las secciones (A y B).
- **Diagramas:** Se revisó el diagrama TO-BE con el equipo, asegurando que las acciones tengan responsables claros y las decisiones tengan sus condiciones.
- **Correcciones:** Se revisaron las dudas sobre la integración de los sistemas de los hospitales, quedando registradas como supuestos en la sección 4.
- **Publicación:** Archivo integrado en la carpeta `U2-E01` y publicado en la rama `main` por el equipo de Documentación.

---
*Documento generado para la materia de Ingeniería de Software - Equipo Webtons.*