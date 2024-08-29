# Proyecto del Sprint 3

Preparar un informe con visualizaciones que brinde información sobre los hábitos de compra de los clientes de una plataforma de entrega de comestibles.

## Diccionario de Datos

Hay cinco tablas en el conjunto de datos, y tendrás que usarlas todas para hacer el preprocesamiento de datos y el análisis exploratorio de datos. A continuación se muestra un diccionario de datos que enumera las columnas de cada tabla y describe los datos que contienen.

### instacart_orders.csv
Cada fila corresponde a un pedido en la aplicación Instacart.
- `order_id`: número de ID que identifica de manera única cada pedido.
- `user_id`: número de ID que identifica de manera única la cuenta de cada cliente.
- `order_number`: el número de veces que este cliente ha hecho un pedido.
- `order_dow`: día de la semana en que se hizo un pedido (0 si es domingo).
- `order_hour_of_day`: hora del día en que se hizo el pedido.
- `days_since_prior_order`: número de días transcurridos desde que este cliente hizo su pedido anterior.

### products.csv
Cada fila corresponde a un producto único que pueden comprar los clientes.
- `product_id`: número ID que identifica de manera única cada producto.
- `product_name`: nombre del producto.
- `aisle_id`: número ID que identifica de manera única cada categoría de pasillo de víveres.
- `department_id`: número ID que identifica de manera única cada departamento de víveres.

### order_products.csv
Cada fila corresponde a un artículo pedido en un pedido.
- `order_id`: número de ID que identifica de manera única cada pedido.
- `product_id`: número ID que identifica de manera única cada producto.
- `add_to_cart_order`: el orden secuencial en el que se añadió cada artículo en el carrito.
- `reordered`: 0 si el cliente nunca ha pedido este producto antes, 1 si lo ha pedido.

### aisles.csv
- `aisle_id`: número ID que identifica de manera única cada categoría de pasillo de víveres.
- `aisle`: nombre del pasillo.

### departments.csv
- `department_id`: número ID que identifica de manera única cada departamento de víveres.
- `department`: nombre del departamento.

## Instrucciones para Completar el Proyecto

## Paso 1: Exploración Inicial de los Datos

Abre los archivos de datos (`/datasets/instacart_orders.csv`, `/datasets/products.csv`, `/datasets/aisles.csv`, `/datasets/departments.csv` y `/datasets/order_products.csv`) y echa un vistazo al contenido general de cada tabla.

Observa que los archivos tienen un formato no estándar, así que vas a necesitar establecer ciertos argumentos en `pd.read_csv()` para leer los datos correctamente. Mira los archivos CSV para tener una idea de cuáles deberían ser esos argumentos.

Ten en cuenta que `order_products.csv` contiene muchas filas de datos. Cuando un DataFrame tiene demasiadas filas, `info()` no imprimirá los recuentos no nulos por defecto. Si quieres imprimir los recuentos no nulos, incluye `show_counts=True` cuando llames a `info()`.

## Paso 2: Preprocesamiento de Datos

Preprocesa los datos de la siguiente manera:

1. **Verifica y Corrige los Tipos de Datos**:
   - Asegúrate de que las columnas de ID sean números enteros.

2. **Identifica y Completa los Valores Ausentes**:
   - Identifica los valores ausentes y decide cómo completarlos.

3. **Identifica y Elimina los Valores Duplicados**:
   - Identifica los valores duplicados y elimínalos.

Asegúrate de explicar qué tipos de valores ausentes y duplicados encontraste, cómo los completaste o eliminaste y por qué usaste esos métodos. ¿Por qué crees que estos valores ausentes y duplicados pueden haber estado presentes en el conjunto de datos?

## Paso 3: Análisis de Datos

### [A] (deben completarse todos para aprobar)

1. Verifica que los valores en las columnas `order_hour_of_day` y `order_dow` de la tabla `orders` sean razonables (o sea, `order_hour_of_day` va de 0 a 23 y `order_dow` va de 0 a 6).
2. Crea un gráfico que muestre el número de personas que hacen pedidos dependiendo de la hora del día.
3. Crea un gráfico que muestre qué día de la semana la gente hace sus compras.
4. Crea un gráfico que muestre el tiempo que la gente espera hasta hacer su próximo pedido, y comenta los valores mínimos y máximos.

### [B] (deben completarse todos para aprobar)

1. ¿Hay alguna diferencia en las distribuciones de `order_hour_of_day` en miércoles y sábados? Traza los histogramas de ambos días en el mismo gráfico y describe las diferencias que observes.
2. Traza la distribución del número de pedidos que hacen los clientes y las clientas (por ejemplo, cuántos clientes hicieron un solo pedido, cuántos hicieron solo dos, cuántos solo tres, etc.).
3. ¿Cuáles son los 20 principales productos que se piden con más frecuencia (muestra su identificación y nombre)?

### [C] (deben completarse todos para aprobar)

1. ¿Cuántos artículos compra la gente por lo general en un pedido? ¿Cómo es la distribución?
2. ¿Cuáles son los 20 principales artículos que se vuelven a pedir con más frecuencia (muestra sus nombres e identificaciones de producto)?
3. Para cada producto, ¿qué proporción de sus pedidos se vuelven a pedir (crea una tabla con columnas para el ID del producto, el nombre del producto y la proporción en que se ha vuelto a comprar)?
4. ¿Cuál es la proporción de productos pedidos que se vuelven a pedir para cada cliente?
5. ¿Cuáles son los 20 principales artículos que la gente pone en sus carritos primero (muestra las identificaciones de los productos, los nombres de los productos y el número de veces que fueron el primer artículo añadido al carrito)?

