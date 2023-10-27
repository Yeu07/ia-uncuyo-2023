# TP7 - IA

# PARTE B

## A. Descripción del proceso de preprocesamiento

Al predominar las clases con inclinacion_peligrosa = 0 se decidió implementar la técnica de oversampling para equilibrar las clases

## B. Resultados obtenidos sobre el conjunto de validación

Ya que hay demasiadas filas de resultados, solo voy a colocar 10 al azar:

| ID  | inclinacion_peligrosa |
|-----|-----------------------|
| 244 | 0.267581725339109     |
| 249 | 0.158900458638339     |
| 251 | 0.146224689954004     |
| 254 | 0.0838080586080586    |
| 256 | 0.118779487179487     |
| 264 | 0.167312820512821     |
| 267 | 0.231628388044792     |
| 270 | 0.191329431084446     |
| 273 | 0.432222438672439     |
| 275 | 0.179371691515051     |

## C. Resultados obtenidos en Kaggle

Los resultados obtenidos en kaggle fueron: 0.75045

## D. Descripción detallada del algoritmo propuesto

Se optó por utilizar la biblioteca ranger para utilizar el algoritmo de random forest:

1.  Se comienza haciendo un oversampling de la clase minoritaria para equilibrar las clases

2.  Se toman todos los atributos del data set (incluyendo utlima_modificación e id)

3.  Se crean 250 árboles dentro del bosque

4.  Luego se realizan las predicciones utilizando él data test
