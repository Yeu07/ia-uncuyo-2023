
## 7. Validación cruzada (Cross validation) (k-folds): La validación cruzada es una técnica para estimar el error de generalización de un algoritmo/modelo de machine learning. La técnica consiste en (previo realizar una mezcla aleatoria) separar el conjunto de datos en k partes (normalmente denominadas folds). Luego en la primera iteración se utilizan k-1 partes para entrenar E1  y se utiliza la restante  para test. El proceso se repite por k iteraciones utilizando en cada una diferentes conjuntos de entrenamiento y test. (Ver figura)

### a. Crear una función de nombre create_folds() que reciba como parámetro un dataframe y la cantidad de folds y devuelva una lista de R con la siguiente estructura: list(Fold1=c(...), Fold2=c(..),... Fold10=c()) Donde Fold1 va a contender los índices del dataframe que fueron seleccionados para el primer fold, y así con los demás

```{r}
library(rpart)

# Función para crear los folds
create_folds <- function(dataframe, k) {
  n <- nrow(dataframe)
  indices <- sample(1:n)
  fold_size <- n %/% k
  folds <- list()
  
  for (i in 1:k) {
    start_idx <- (i - 1) * fold_size + 1
    end_idx <- ifelse(i < k, i * fold_size, n)
    folds[[paste0("Fold", i)]] <- indices[start_idx:end_idx]
  }
  
  return(folds)
}

```



### b. Crear una función de nombre cross_validation() que reciba como parámetro un data frame y un número de folds y entrene un modelo de árbol de decisión (utilizar paquete rpart) para cada uno de los posibles conjuntos de entrenamiento  y calcule las métricas: Accuracy, Precision, Sensitivity, Specificity  para cada uno de los  posibles conjuntos de tests. Devolver media y desviación estándar


```{r}
library(caret)
library(rpart)

cross_validation <- function(dataframe, k) {
  set.seed(123)  # Para reproducibilidad

  # Crear un modelo de control para la validación cruzada
  ctrl <- trainControl(method = "cv", number = k, classProbs = TRUE)


  # Definir la fórmula
  train_formula<-formula(inclinacion_peligrosa~ .)

  # Entrenar el modelo usando rpart con el control definido
  tree_model<-rpart(train_formula, data=dataframe, method='class')
  
  # Calcular las predicciones en la validación cruzada
  predictions <- predict(tree_model, newdata = dataframe, type = "class")
  
  # Calcular métricas
  confusion_matrix <- confusionMatrix(predictions, dataframe$inclinacion_peligrosa)
  
}

data <- read.csv("arbolado-mza-dataset.csv")

data$inclinacion_peligrosa <- as.factor(data$inclinacion_peligrosa)
print(levels(data$inclinacion_peligrosa))

# Realizar validación cruzada
result <- cross_validation(data, 4)
print(result)







```

