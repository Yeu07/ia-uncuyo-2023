## 2.10 Consider a modified version of the vacuum environment in Exercise 2.8, in which the agent is penalized one point for each movement.

### a. Can a simple reflex agent be perfectly rational for this environment? Explain.

No, un simple agente reflexivo nunca va a poder ser perfectamente racional, ya que al no tener memoria de sus estados previos y solo pensar en su estado actual, no va a recordar si ya cumplió su tarea en algún casillero anterior y existe la posibilidad de que vuelva a ese casillero lo cual sería ineficiente. También podría pasar que haya cumplido toda su tarea en este mundo y al no ser consciente del mundo, seguir ejecutándose infinitamente.

### b. What about a reflex agent with state? Design such an agent.

En este caso, un agente reflexivo con estados ya tiene una visión completa del mundo y puede tomar decisiones basándonos en estados anteriores, por lo tanto, podría maximizar su tarea y terminar cuando no haya más casilleros en los cuales cumplir su tarea. Este agente sí podría ser racional.

### c. How do your answers to a and b change if the agent’s percepts give it the clean/dirty status of every square in the environment?

Al conocer el estado de cada casilla, el agente reflexivo simple podría ser capaz de maximizar sus decisiones y sería capaz de ser un agente mucho más racional, ya que podría desplazarse únicamente a zonas las cuales estén sucias. Mientras que el segundo agente se mantendría igual.

## 2.11 Consider a modified version of the vacuum environment in Exercise 2.8, in which the geography of the environment—its extent, boundaries, and obstacles—is unknown, as is the initial dirt configuration. (The agent can go Up and Down as well as Left and Right.)

### a. Can a simple reflex agent be perfectly rational for this environment? Explain.

Sí, un agente reflexivo simple podría ser racional, ya que en este caso no se estarían descontando puntos por cada movimiento en el cual no se limpie, por lo tanto, este seguiría funcionando de manera infinita, pero estaría maximizando la performance.

### b. Can a simple reflex agent with a randomized agent function outperform a simple reflex agent? Design such an agent and measure its performance on several environments.

Sí, al no conocerse nada acerca del mundo, quizás un agente reflexivo simple con función aleatoria terminaría siguiendo rutas y caminos más beneficiosos que un simple agente reflexivo. Aunque son casos excepcionales

### c. Can you design an environment in which your randomized agent will perform poorly? Show your results.

A medida que el mundo es mas grande y tenemos cada vez menos suciedad, lograr que un agente random maximice se vuelve cada vez mas complicado ya que no hay ningun analisis previo sobre a que casilla desplazarse.

### d. Can a reflex agent with state outperform a simple reflex agent? Design such an agent and measure its performance on several environments. Can you design a rational agent of this type?

En cuestiones de performance, considero que estarían iguales, ya que solo estamos teniendo en cuenta el total de casillas limpiadas, y aunque el agente reflexivo con estados seria capaz de hacerlo más rápido, los dos terminarían por cumplir la tarea y maximizando la performance.




