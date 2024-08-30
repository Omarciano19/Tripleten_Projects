# Proyecto del Sprint 11: Álgebra lineal

"Crear un modelo que ayude a una compañía de seguros a trabajar mejor con su base de datos de clientes y proteja sus datos personales."


En este proyecto se hace uso de librerias de algebra lineal para manipular datos, agrupar a través de KNN, generar modelos de regresión lineal y ofuscar datos a través de multiplicación de matrices.
Tambien se hacen analisís analiticos del funcionamiento de la ofuscación.

- Se hace un analisis exploratorio de los datos
- se aplica KNN con y sin escalado de datos para demostrar su importancia en dicho algoritmo
  - Con esto se encuentran clientes similares.
- Se evidencia el efecto de distintas metricas en el algoritmo KNN
- Se creó un modelo de regresión lineal para determinar los beneficiós resultantes del seguro.
  - se demostró como el escalado de datos no tiene influencia en la regresión lineal.
- Se demostró de forma practica y analitica, como una ofuscación de datos a través de una matriz aleatoria $P$, no afecta en ningun sentido practico las predicciónes de un modelo de regresión lineal y que la ofuscación de deshace con el uso de la matriz llave $P^{-1}$

## Descripción del proyecto

La compañía de seguros Sure Tomorrow quiere resolver varias tareas con la ayuda de machine learning y te pide que evalúes esa posibilidad.

- Tarea 1: encontrar clientes que sean similares a un cliente determinado. Esto ayudará a los agentes de la compañía con el marketing.
- Tarea 2: predecir si es probable que un nuevo cliente reciba un beneficio de seguro. ¿Puede un modelo de predicción entrenado funcionar mejor que un modelo dummy no entrenado? ¿Puede funcionar peor? Explica tu respuesta.
- Tarea 3: predecir la cantidad de beneficios de seguro que probablemente recibirá un nuevo cliente utilizando un modelo de regresión lineal.
- Tarea 4: proteger los datos personales de los clientes sin romper el modelo de la tarea anterior.

Es necesario desarrollar un algoritmo de transformación de datos que dificulte la recuperación de la información personal si los datos caen en manos equivocadas. Esto se denomina enmascaramiento de datos u ofuscación de datos. Pero los datos deben protegerse de tal manera que la calidad de los modelos de machine learning no se vea afectada. No es necesario elegir el mejor modelo, basta con demostrar que el algoritmo funciona correctamente.

### Instrucciones del proyecto

1. Carga los datos.
2. Verifica que los datos no tengan problemas: no faltan datos, no hay valores extremos, etc.
3. Trabaja en cada tarea y responde las preguntas planteadas en la plantilla del proyecto.
4. Saca conclusiones basadas en tu experiencia trabajando en el proyecto.


### Descripción de datos
El dataset se almacena en el archivo /datasets/insurance_us.csv.

- **-Características**: sexo, edad, salario y número de familiares de la persona asegurada.
- **-Objetivo**: número de beneficios de seguro recibidos por una persona asegurada en los últimos cinco años.
