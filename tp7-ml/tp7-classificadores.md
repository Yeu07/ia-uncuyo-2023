## 4. Clasificador aleatório:

### a. Implementar una función que dado un conjunto de observaciones (data.frame) genere una nueva columna de nombre prediction_prob con un valor aleatorio entre 0 y 1.

```{r}
# Funcion para agregar columna de predicciones aleatorias

aleatory_predictions <- function(data) {
  data$prediction_prob <- runif(nrow(data), min = 0, max = 1)
  return(data)
}
```

### b. Implementar una función de nombre random_classifier, que reciba como parámetro  el dataframe generado con anterioridad y a partir de la columna predictions_prob genere una nueva columna prediction_class bajo el siguiente criterio:                    If predictions_prob > 0.5 then prediction_class=1 else prediction_class=0                                               La función deberá devolver el dataframe original junto a la nueva columna generada.

```{r}
# Funcion para clasificar basada en la columna "prediction_prob"

random_classifier <- function(data) {
  data$prediction_class <- ifelse(data$prediction_prob > 0.5, 1, 0)
  return(data)
}

```
### c. Cargar el archivo arbolado-mendoza-dataset-validation.csv como un data.frame y aplicarle la función random_classifier

```{r}
# Cargar el archivo arbolado-mendoza-dataset-validation.csv como un data.frame

data_validation <- read.csv("data/arbolado-mendoza-dataset-validation.csv")

data_validation <- aleatory_predictions(data_validation)

data_validation <- random_classifier(data_validation)

```
### d. A partir de la columna recientemente generada y la columna con la clase (inclinación peligrosa) calcular utilizando lenguaje R (dplyr) el número de:

#### i. Número de árboles CON inclinación peligrosa que fueron correctamente predicho como peligrosos por el modelo/algoritmo. (True Positive)

#### ii. Número de árboles SIN inclinación peligrosa  que fueron correctamente predicho como no peligrosos por el modelo. (True Negative)


#### iii. Número de árboles SIN inclinación peligrosa que fueron incorrectamente predicho como peligrosos según el modelo. (False Positives)

#### iv. Número de árboles CON inclinación peligrosa que fueron incorrectamente predicho como no peligrosos según el modelo. (False Negatives)


```{r}

confusion_matrix <- table(data_validation$inclinacion_peligrosa, data_validation$prediction_class)


print(confusion_matrix)



```

    
## 5. Clasificador por clase mayoritaria:

### a. Implementar una función de nombre biggerclass_classifier, que reciba como parámetro  el dataframe generado con anterioridad y genere una nueva columna de nombre prediction_class en donde se asigne siempre de la clase mayoritaria. La función deberá devolver el dataframe original junto a la nueva columna generada.

```{r}

biggerclass_classifier <- function(data) {
  majority_class <- as.integer(as.character(as.numeric(names(sort(table(data$inclinacion_peligrosa), decreasing = TRUE))[1])))
  data$prediction_class <- majority_class
  return(data)
}


```

### b. Repetir los puntos 4.c y 4.d pero aplicando la nueva función biggerclass_classifier

```{r}

data_validation2 <- read.csv("data/arbolado-mendoza-dataset-validation.csv")

data_validation2 <- biggerclass_classifier(data_validation)


tp <- sum(data_validation2$inclinacion_peligrosa == 1 & data_validation2$prediction_class == 1)


tn <- sum(data_validation2$inclinacion_peligrosa == 0 & data_validation2$prediction_class == 0)


fp <- sum(data_validation2$inclinacion_peligrosa == 0 & data_validation2$prediction_class == 1)


fn <- sum(data_validation2$inclinacion_peligrosa == 1 & data_validation2$prediction_class == 0)


confusion_matrix2 <- matrix(c(tn, fp, fn, tp), nrow = 2, byrow = TRUE)
colnames(confusion_matrix) <- rownames(confusion_matrix) <- c("0", "1")


print(confusion_matrix2)
```
## 6. A partir de una matriz de confusión es posible calcular distintas métricas que nos permiten determinar la calidad del modelo de clasificación. Utilizar la siguiente imagen como guía crear funciones para calcular: Accuracy, Precision, Sensitivity, Specificity y calcularlas para las matrices de confusión generadas en los puntos 4 y 5.

```{r}

library(caret)

data_validation$prediction_class <- as.factor(data_validation$prediction_class)
data_validation$inclinacion_peligrosa <- as.factor(data_validation$inclinacion_peligrosa)

# Asegúrate de que ambas columnas tengan los mismos niveles
levels(data_validation$prediction_class) <- levels(data_validation$inclinacion_peligrosa)

# Luego, puedes calcular la matriz de confusión y métricas
confusion4 <- confusionMatrix(data = data_validation$prediction_class, reference = data_validation$inclinacion_peligrosa)

print(confusion4)

data_validation2$prediction_class <- as.factor(data_validation2$prediction_class)
data_validation2$inclinacion_peligrosa <- as.factor(data_validation2$inclinacion_peligrosa)

# Asegúrate de que ambas columnas tengan los mismos niveles
levels(data_validation2$prediction_class) <- levels(data_validation2$inclinacion_peligrosa)

# Luego, puedes calcular la matriz de confusión y métricas
confusion5 <- confusionMatrix(data = data_validation2$prediction_class, reference = data_validation2$inclinacion_peligrosa)

print(confusion5)


```
