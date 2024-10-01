# Aprendizaje automatico para textos: Clasificación de reseñas de IMBd

"Desarrollar un sistema para filtrar y categorizar reseñas de películas entrenando un modelo de clasificación."

En este proyecto se trabaja con un dataset de reseñas de IMBd, a este dataset se le realiza una limpieza, corrección de datos, un analisis exploratorio y posteriormente se genera un *corpus* de las  reseñas; este *corpus* es procesado con herramientas de lenguaje natural, como **SpaCy** y **NLTK**, posteriormente se vectoriza con **TF-IDF, Word2Vec o BERT** para finalmente alimentar once modelos de machine learning, con la finalidad de clasificar y predecir reseñas de peliculas.

En resumen se obtiene la siguiente relación:
|N°| Pre-Procesamiento | Vectorización  | Modelo de ML                       | F1>0.85          |
|-------------------|-------------------|----------------|------------------------------------|-------------------|
|0| -                 | -              | Dummy                              |x
|1| NLTK              | TF-IDF         | Regresión logística                |$\checkmark$ |
|2| NLTK              | TF-IDF         | Potenciación de gradiente (LightGBM)|$\checkmark$ |
|3| Spacy             | TF-IDF         | Regresión logística                 |$\checkmark$ |
|4| Spacy             | TF-IDF         | Potenciación de gradiente (LightGBM)|$\checkmark$ |
|5| NLTK              | TF-IDF         | Bosque aleatorio                    |$\checkmark$ |
|6| Spacy             | TF-IDF         | Bosque aleatorio                   |$\checkmark$ |
|7| NLTK              | Word2Vec| Potenciación de gradiente (LightGBM)|x|
|8| Spacy             | Word2Vec| Potenciación de gradiente (LightGBM)|x|
|9| NLTK              | BERT           | Potenciación de gradiente (LightGBM)|x|
|10| NLTK              | BERT           | Regresión logística                 |x|

## Skills:
<div align='center'>
  <img width="70" alt="Fundamentos de ML" src="https://github.com/user-attachments/assets/4e575dc9-04df-47c2-ad4d-f82837d006ab">
  <img width="70" alt="ML avanzado" src="https://github.com/user-attachments/assets/64c66a60-e738-40b0-b89c-c1840ff9ba80">
  </div>
  <div align='center'>
<img width="70" alt="Modelos de clasificación" src="https://github.com/user-attachments/assets/0dc993b9-1eab-4b79-ae55-c8732fd0940f">
<img width="70" alt="Procesamiento de lenguajes naturales" src="https://github.com/user-attachments/assets/77b95847-80e4-4d06-ac2f-b550d1a4f0dd">

</div>

## Descripción del proyecto
Film Junky Union, una nueva comunidad vanguardista para los aficionados de las películas clásicas, está desarrollando un sistema para filtrar y categorizar reseñas de películas. Tu objetivo es entrenar un modelo para detectar las críticas negativas de forma automática. Para lograrlo, utilizarás un conjunto de datos de reseñas de películas de IMDB con etiquetado para construir un modelo que clasifique las reseñas como positivas y negativas. Este deberá alcanzar un valor F1 de al menos 0.85.

## Descripción de los datos
Los datos se almacenan en el archivo imdb_reviews.tsv.

Los datos fueron proporcionados por *Andrew L. Maas, Raymond E. Daly, Peter T. Pham, Dan Huang, Andrew Y. Ng, y Christopher Potts. (2011). Learning Word Vectors for Sentiment Analysis. La Reunión Anual 49 de la Asociación de Lingüística Computacional (ACL 2011).*

### Aquí se describen los campos seleccionados:

- -review: el texto de la reseña
- -pos: el objetivo, '0' para negativo y '1' para positivo
- -ds_part: 'entrenamiento'/'prueba' para la parte de entrenamiento/prueba del conjunto de datos, respectivamente
