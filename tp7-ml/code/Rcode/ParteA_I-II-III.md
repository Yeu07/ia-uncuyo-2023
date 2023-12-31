
# TP7 - IA

# PARTE A

## 1. Bajar el archivo  arbolado-mendoza-dataset.csv, el mismo se encuentra en formato CSV (comma separated values). 

### a. Seleccionar de manera uniformemente aleatoria el 20% del conjunto de datos y crear un nuevo archivo con el nombre de arbolado-mendoza-dataset-validation.csv y el 80% restante con el nombre de arbolado-mendoza-dataset-train.csv

```{r}

library(dplyr)
library(ggplot2)

data <- read.csv("data/arbolado-mza-dataset.csv")

data_train <- data %>% sample_frac(0.8)

data_test <- data %>% anti_join(data_train, by = "id")

write.csv(data_train, "data/arbolado-mendoza-dataset-train.csv", row.names = FALSE)
write.csv(data_test, "data/arbolado-mendoza-dataset-validation.csv", row.names = FALSE)


```

## 2. A partir del archivo arbolado-mendoza-dataset-train.csv responder las siguientes preguntas:

### a. ¿Cual es la distribución de las clase inclinacion_peligrosa?


```{r}  

gg <- ggplot(data_train, aes(x = inclinacion_peligrosa)) +
geom_bar() + 
labs(title = "Distribución de las clases de inclinación peligrosa",
x = "Inclinación peligrosa",
y = "Cantidad de árboles")

ggsave("plots/DsitributionClass.png", gg, width = 10, height = 10, units = "cm")


```
En el gráfico podemos observar que la clase inclinación peligrosa tiene una distribución desbalanceada, ya que la clase 0 tiene una cantidad de árboles mucho mayor que la clase 1.


### b. ¿Se puede considerar alguna sección más peligrosa que otra?

```{r}

gg <- ggplot(data_train, aes(x = nombre_seccion)) +
geom_bar() +
labs(title = "Distribución de las clases de sección",
x = "Sección",
y = "Frecuencia") + 
theme(axis.text.x = element_text(angle = 90, hjust = 1))

ggsave("plots/DsitributionSection.png", gg, width = 10, height = 10, units = "cm")

```
Podemos observar como Residencial Norte y Residencial Sur tienen una cantidad de árboles mucho mayor que el resto de las secciones, por lo que podemos considerar que son las secciones más peligrosas.

### c.¿Se puede considerar alguna especie más peligrosa que otra?

```{r}

gg <- ggplot(data_train, aes(x = especie)) +
geom_bar() +
labs(title = "Distribución de las clases de especie",
x = "Especie",
y = "Frecuencia") +
theme(axis.text.x = element_text(angle = 90, hjust = 1))


ggsave("plots/DsitributionSpecies.png", gg, width = 10, height = 10, units = "cm")
```
Podemos observar como la Morera es la especie que más árboles tiene, por lo que podemos considerar que es la especie más peligrosa.

## 3. A partir del archivo arbolado-mendoza-dataset-train.csv

### a. Generar un histograma de frecuencia para la variable circ_tronco_cm. Probar con diferentes  números de bins.

```{r}

gg <- ggplot(data_train, aes(x = circ_tronco_cm)) +
geom_histogram(bins = 100) +
labs(title = "Histograma 100 bins ",
x = "Circunferencia del tronco en cm",
y = "Frecuencia")

ggsave("plots/HistogramCircTronco100bins.png", gg, width = 10, height = 10, units = "cm")



```

### b. Repetir el punto a) pero separando por la clase de la variable inclinación_peligrosa?

```{r}

ggplot(data_train, aes(x = circ_tronco_cm)) +
  geom_histogram(bins = 20) +
  facet_wrap(~ inclinacion_peligrosa) +
  labs(title = "Histograma de circ_tronco_cm por inclinacion_peligrosa",
       x = "Circunferencia del tronco en cm",
       y = "Frecuencia")



 ```

### c. Crear una nueva variable categórica de nombre circ_tronco_cm_cat a partir circ_tronco_cm, en donde puedan asignarse solo  4 posibles valores [ muy alto, alto, medio, bajo ]. Utilizar la información del punto b. para seleccionar los puntos de corte para cada categoría. Guardar el nuevo dataframe bajo el nombre dearbolado-mendoza-dataset-circ_tronco_cm-train.csv

```{r}

cut <- quantile(data_train$circ_tronco_cm, probs = c(0, 0.25, 0.5, 0.75, 1), na.rm = TRUE)

data_train$circ_tronco_cm_cat <- cut(data_train$circ_tronco_cm, breaks = cut, labels = c("bajo", "medio", "alto", "muy alto"))

write.csv(data_train, "data/arbolado-mendoza-dataset-circ_tronco_cm-train.csv", row.names = FALSE)

```











