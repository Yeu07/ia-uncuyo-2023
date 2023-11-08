# TP7 - IA

# PARTE C

## Resultados sobre la evaluación sobre el dataset Tennis

El dataset fue probado sobre 250 árboles de decisión y esta fue la matriz de confusión y la media calculada:

![Resultados](tp7-ml\plots\Results_PartC.PNG)


## Investigación

Los árboles de decisión suelen ser bastante utilizados, aunque rara vez se utilizan en solitario, se suelen combinar con otras técnicas de machine lerning como por ejemplo: "Random Forest", ya que los árboles de decisión en sí solos suelen ser un poco menos robustos a la hora de entrenar un modelo, ya que podríamos por ejemplo tener clases y etiquetas desbalanceadas, podrimos tener problemas a la hora de seleccionar variables, ya que la complejidad espacial y temporal podría dispararse muy rápidamente y podriamos tener problemas de overfiting.

Para aliviar todos estos problemas de los árboles de decisión se suelen utilizar diferentes estrategias como el uso de criterios de división Para determinar de forma correcta que tan útil es la información que se nos proporciona. Se suelen utilizar una mezcla de criterios como la impureza de Gini, la ganancia de información y el error cuadrático medio.

También a la hora de trabajar con datos reales es muy importante la complejidad espacial y temporal, estos problemas podrían solucionarse utilizando la poda tanto de filas (registros) como de atributos, los cuales no aporten nada, limitando la profundidad del árbol, etc.

Como ya se mencionó antes, una mejora considerable para los árboles de decisión es emplear "Random Forest". Random Forest es una estrategia en la cual creo un bosque con varios árboles de decisión creados de manera distinta en los cuales en cada árbol voy a tomar un subconjunto de mi lista de atributos.

Con todas estas consideraciones y con el hardware y software actual ya es “relativamente” fácil implementar buenos diseños y modelos usando árboles de decisión y datos reales.





