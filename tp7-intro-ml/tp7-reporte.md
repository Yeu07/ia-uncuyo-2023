# Proveer las respuestas a los puntos 1,2,5,6,7 de la sección 2.4 (página 52 del ISLRv2).


## Ejericio 1

### 1. For each of parts (a) through (d), indicate whether we would generally expect the performance of a flexible statistical learning method to be better or worse than an inflexible method. Justify your answer.

    (a) The sample size n is extremely large, and the number of predictors p is small.

        Con un tamaño de muestra grande y un número de predictores P pequeño, lo más recomendable un método felxible, ya que hay suficientes datos sobre los cuales aprender y quizás tengamos relaciones más complejas para analizar.
    

    (b) The number of predictors p is extremely large, and the number of observations n is small.

        En este caso, es mucho más recomendable usar un método inflexible, ya que es mucho más fácil aproximar linealmente, ya que mientras más predictores tengo, menos influye cada uno en la función f.

    (c) The relationship between the predictors and response is highly non-linear.

        Es recomendable usar métodos flexibles, ya que estos podrían capturar patrones más complejos en los datos.

    (d) The variance of the error terms, i.e. σ2 = Var(ϵ), is extremely high.

        Cuando el error tiene una varianza demasiado alta, puede ser difícil modelar los datos de manera precisa debido a la gran variabilidad del error. En estos casos es mucho mejor usar métodos inflexibles, ya que los métodos flexibles podrían llevar a un sobre ajuste excesivo


## Ejericio 2

### 2. Explain whether each scenario is a classification or regression problem, and indicate whether we are most interested in inference or prediction. Finally, provide n and p.

    (a) We collect a set of data on the top 500 firms in the US. For each firm we record profit, number of employees, industry and the CEO salary. We are interested in understanding which factors affect CEO salary.

        n: 500 empresas
        p: Ganancias, numero de empleados, industria, salario director ejecutivo

        Es un método de regresión, ya que nos interesa saber qué factores afectan el salario del CEO. Estamos principalmente interesados en la inferencia, ya que queremos comprender estos datos y no tan interesados en predecir datos futuros.


    (b) We are considering launching a new product and wish to know whether it will be a success or a failure. We collect data on 20 similar products that were previously launched. For each product we have recorded whether it was a success or failure, price charged for the product, marketing budget, competition price, and ten other variables.

        n: 20 productos similares
        p: exito o fracaso, precio cobrado del producto, presupuesto de marketing, precio de la competencia y 10 variables más.

        Este es un caso de clasificación, ya que queremos predecir si un producto es un éxito o un fracaso (clasificación = éxito o fracaso). Estamos más interesados en la predicción, ya que queremos saber si nuestro futuro producto (no fue analizado previamente) va a ser exitoso o no.

    (c) We are interested in predicting the % change in the USD/Euro exchange rate in relation to the weekly changes in the world stock markets. Hence we collect weekly data for all of 2012. For each week we record the % change in the USD/Euro, the % change in the US market, the % change in the British market, and the % change in the German market.

        n: Datos semanales de todo 2012
        p: % de cambio en el USD/Euro, el % de cambio en el mercado estadounidense, el % de cambio en el mercado británico y el % de cambio en el mercado alemán.
    
        Este es un problema de regresión, ya que queremos predecir una variable continua. Nos interesa la predicción ya que basándonos en datos antiguos, queremos pronosticar cambios en función de los datos semanales del mercado.


## Ejercicio 5

### 5. What are the advantages and disadvantages of a very flexible (versus a less flexible) approach for regression or classification? Under what circumstances might a more flexible approach be preferred to a less flexible approach? When might a less flexible approach be preferred?

### Clasificación

    - Ventajas de Flexibilidad en Clasificación:

        - Puede capturar relaciones no lineales y altamente complejas entre las caracteristicas y clases de interes.

        - Proporciona mayor precision a la hora de clasificar datos ya que ajusta mejor los datos de entrenamiento

    - Desventajas de Flexibilidad en Clasificación:

        - Podrian memorizar conjunto de entrenamiento y no generalizar bien los nuevos datos (sobre ajuste).

        - Podrian ser muy dificiles de interpretar.

### Regresión

    - Ventajas de Flexibilidad en Regresión:

        - Proporcionan mayor precisión predictiva trabajando con datos con alta variabilidad de error y relaciones complejas entre las variables predictoras y la respuesta.

    - Desventajas de Flexibilidad en Regresión:

        - Riesgo de sobre ajuste trabajando con pequeños grupos de datos.

        - Complejos y dificiles de interpretar.

### Enfoque más flexible

Tratamos de usar un enfoque más flexible cuando los datos son complejos y consideramos que no se pueden aproximar linealmente. También los enfoques felxibles son utiles cuando el grado de precisión sea fundamental, hay que tener en cuenta que estos cuentan con un mayor costo computacional.

### Enfoque menos flexible

Tratamos de usar enfoques más inflexibles cuando nuestro conjunto de datos (n) es pequeño. También un enfoque más inflexible es util cuando la interpretabilidad del modelo es fundamental. Es util cuando contamos con recursos computacionales basttante limitados.


## Ejercicio 6

### 6. Describe the differences between a parametric and a non-parametric statistical learning approach. What are the advantages of a parametric approach to regression or classification (as opposed to a non parametric approach)? What are its disadvantages?

    Un enfoque estadístico paramétrico reduce el problema de estimar f a la estimación de un conjunto de parámetros. Asumir una forma paramétrica para f simplifica el problema de estimar f porque generalmente es mucho más fácil estimar un conjunto de parámetros, como β0 , β1 , . . . βp en el modelo lineal, que ajustar una función f totalmente arbitraria.
    Mientras que un enfoque no paramétrico no hace suposiciones específicas sobre la forma funcional de la relación entre las variables predictoras y la respuesta.

    Los métodos no paramétricos no hacen suposiciones explícitas sobre la forma funcional de f . En su lugar, buscan una estimación de f que se acerque lo más posible a los puntos de datos sin ser demasiado aproximada o imprecisa.

    Ventajas de enfoques no paramétricos:

        - Al evitar la suposición de una forma funcional particular para f , tienen el potencial de ajustarse con precisión a una gama más amplia de formas posibles para f 

    Desventajas de enfoques no paramétricos:

        - como no reducen el problema de estimar f a un pequeño número de parámetros, se necesita un gran número de observaciones (muchas más de las que suele necesitar un enfoque paramétrico) para obtener una estimación precisa de f .

## Ejercicio 7

### 7. The table below provides a training data set containing six observations, three predictors, and one qualitative response variable.


| Obs. |  X1  |  X2  |  X3  |  Y   |
|:----:|:---:|:---:|:---:|:---:|
|  1   |  0   |  3   |  0   | Red   |
|  2   |  2   |  0   |  0   | Red   |
|  3   |  0   |  1   |  3   | Red   |
|  4   |  0   |  1   |  2   | Green |
|  5   | -1   |  0   |  1   | Green |
|  6   |  1   |  1   |  1   | Red   |



### Suppose we wish to use this data set to make a prediction for Y when X1 = X2 = X3 = 0 using K-nearest neighbors.

    (a) Compute the Euclidean distance between each observation and the test point, X1 = X2 = X3 = 0.

        - 1. √9 = 3

        - 2. √4 = 2

        - 3. √10 = 3.16

        - 4. √5 = 2.24

        - 5. √2 = 1.41

        - 6. √3 = 1.73


    (b) What is our prediction with K = 1? Why?

        El vecino mas cercano es la observación 5 con la etiqueta "Green". Cuando ordeno el punto a) de menor a mayor, la distancia K=1 es la observación 5. Por lo tanto, la predicción para Y cuando K = 1 es "Green". 

    (c) What is our prediction with K = 3? Why?

        Los tres vecinos más cercanos:

        Observación 5 con una distancia de aproximadamente 1.41 (Green - Verde).
        Observación 2 con una distancia de 2 (Red - Rojo).
        Observación 4 con una distancia de aproximadamente 2.24 (Green - Verde).

        De los tres vecinos más cercanos, dos son de la clase "Green" y uno es de la clase "Red" . Por lo tanto, la predicción para Y cuando K = 3 es "Green". Cuando ordeno el punto a) de menor a mayor, la distancia K=3 son las observaciones 5, 2 y 4. Por lo tanto, la predicción para Y cuando K = 3 es "Green".

    (d) If the Bayes decision boundary in this problem is highly non- linear, then would we expect the best value for K to be large or small? Why?

        Esperamos que el valor para K sea pequeño. Un valor más pequeño de K da más peso a los puntos de datos locales, lo que hace que la frontera de decisión sea más flexible y capaz de capturar relaciones complejas y no lineales en los datos. A medida que K aumenta, la frontera de decisión se vuelve más suave y es posible que no se ajuste bien a patrones no lineales complejos.