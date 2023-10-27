
```{r}

# Cargar la biblioteca ranger
library(ranger)

data <- read.csv("data/arbolado-mza-dataset.csv")


set.seed(123) 


minority_class <- data[data$inclinacion_peligrosa == 1, ]
oversampled_data <- rbind(data, minority_class)


testing_data <- read.csv("data/arbolado-mza-dataset-test.csv")


model <- ranger(inclinacion_peligrosa ~ ., data = oversampled_data, num.trees = 250)


predictions <- predict(model, data = testing_data)$predictions


results <- data.frame(ID = testing_data$id, inclinacion_peligrosa = predictions)

# write.csv(results, file = "randomForest-250trees-oversampled.csv", row.names = FALSE)