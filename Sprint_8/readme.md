# Proyecto del Sprint 8: Introducción al machine learning
"Crear un modelo de clasificacion que escogerá el plan adecuado para la clientela de un operador de telefonía móvil."

Este es mi primer acercamiento formal al machine learning, usando distintos tipos de modelos y ajustando sus hiperparametros de forma estructurada para encontrar aquel modelo que funcione de la mejor manera.
El mejor modelo para esta tarea fue un bosque aleatorio de clasificación.

## Skills:

<div align='center'>
<img width="68" alt="Procesamiento de datos" src="https://github.com/user-attachments/assets/8b350c4b-1041-4153-b794-0f6bdb4af648">
<img width="68" alt="Fundamentos de ML" src="https://github.com/user-attachments/assets/4a5b35f2-6b91-48b6-9fe6-89ddb5fe852e">
<img width="64" alt="Modelos de clasificación" src="https://github.com/user-attachments/assets/8bc11e58-85d2-4900-abaf-3fa113664a66">


</div>

# Descripción del proyecto
La compañía móvil Megaline no está satisfecha al ver que muchos de sus clientes utilizan planes heredados. Quieren desarrollar un modelo que pueda analizar el comportamiento de los clientes y recomendar uno de los nuevos planes de Megaline: Smart o Ultra.

Tienes acceso a los datos de comportamiento de los suscriptores que ya se han cambiado a los planes nuevos (del proyecto del sprint de Análisis estadístico de datos). Para esta tarea de clasificación debes crear un modelo que escoja el plan correcto. Como ya hiciste el paso de procesar los datos, puedes lanzarte directo a crear el modelo.

Desarrolla un modelo con la mayor exactitud posible. En este proyecto, el umbral de exactitud es $0.75$. Usa el dataset para comprobar la exactitud.

## Instrucciones del proyecto.

1. Abre y examina el archivo de datos. Dirección al archivo:datasets/users_behavior.csv Descarga el dataset
2. Segmenta los datos fuente en un conjunto de entrenamiento, uno de validación y uno de prueba.
2. Investiga la calidad de diferentes modelos cambiando los hiperparámetros. Describe brevemente los hallazgos del estudio.
3. Comprueba la calidad del modelo usando el conjunto de prueba.
- Tarea adicional: haz una prueba de cordura al modelo. Estos datos son más complejos que los que habías usado antes así que no será una tarea fácil. Más adelante lo veremos con más detalle.
## Descripción de datos
Cada observación en el dataset contiene información del comportamiento mensual sobre un usuario. La información dada es la siguiente:

- -`сalls` — número de llamadas,
- -`minutes` — duración total de la llamada en minutos,
- -`messages` — número de mensajes de texto,
- -`mb_used` — Tráfico de Internet utilizado en MB,
- -`is_ultra` — plan para el mes actual (Ultra - 1, Smart - 0).
