# Challenge_Alaya

Challenge for data scientist with alaya digital solutions
  
## Installation guide

Please read [install.md](install.md) for details on how to set up this project.

## Project Organization

    ├── LICENSE
    ├── tasks.py           <- Invoke with commands like `notebook`.
    ├── README.md          <- The top-level README for developers using this project.
    ├── install.md         <- Detailed instructions to set up this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries.
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures         <- Generated graphics and figures to be used in reporting.
    │
    ├── environment.yml    <- The requirements file for reproducing the analysis environment.
    │
    ├── .here              <- File that will stop the search if none of the other criteria
    │                         apply when searching head of project.
    │
    ├── setup.py           <- Makes project pip installable (pip install -e .)
    │                         so challenge_alaya can be imported.
    │
    └── challenge_alaya               <- Source code for use in this project.
        ├── __init__.py    <- Makes challenge_alaya a Python module.
        │
        ├── data           <- Scripts to download or generate data.
        │   └── make_dataset.py
        │
        ├── features       <- Scripts to turn raw data into features for modeling.
        │   └── build_features.py
        │
        ├── models         <- Scripts to train models and then use trained models to make
        │   │                 predictions.
        │   ├── predict_model.py
        │   └── train_model.py
        │
        ├── utils          <- Scripts to help with common tasks.
            └── paths.py   <- Helper functions to relative file referencing across project.
        │
        └── visualization  <- Scripts to create exploratory and results oriented visualizations.
            └── visualize.py

---
Project based on the [cookiecutter personal data science project template](https://github.com/Giocrisrai/cookiecutter-personal).

# FAULT-CLASSIFICATION

### PROBLEMA Y SOLUCIÓN BUSCADA
El contexto: Los datos son una muestra sintetica de data de mantenimiento de motores, los cuales contienen información de settings (parámetros de funcionamiento) y de sensores que monitorean el comportamiento de los motores. Una curva de mantenimiento, muestra la degradación de un activo en función del tiempo, en esta curva identificamos 4 estados

* Estado1: Activo Sano
* Estado2: Desde: Incio de la falla / Hasta: Fallo potencial
* Estado3: Desde: Fallo potencial/ Hasta: Fallo funcional
* Estado4: Activo en mal funcionamiento
Ver imagen:

![estados de un activo](https://github.com/alaya-digital-solutions/challenges/blob/main/fault-classification/images/states.png)


### PREGUNTAS
Peguntas que nos interesan saber ! 

1. De los 4 estados mencionados anteriormente, cuales crees que se encuentran presente en la data
   - Deben estar presente los diferentes estados ya que hay dato de 100 motores dentro de los cuales hay diferentes registros que deben tener diferentes etapas que han podido estar estos motores.
2. Como encontrarías estos estados sin conocer la data, todos los sensores aportan información? con cuales trabajarías?
   - Al hacer referencia a motores dentro de las caracteristicas para saber el estado de un motor es necesario saber la temperatura para poder determinar si esta en los valores que pueden indicar los fabricantes del motor, tener medición de vibraciones para poder tener ese parametro y poder determinar la información de lo medido respecto al datasheet, valores de voltaje y corriente del motor, y sus correspondientes configuraciones si esta trabajando debajo de su valor nominal si esta seteado con algún variador de frecuencia todos esos valores son información valiosa que puede aportar dentro del modelo para determinar un estado en particular, ahora bien con la información proporcionada lo que se puede hacer es una detección de anomalias respeto a cada motor dentro del conjunto de datos e ir detectando comportamientos al unisono de que tanto ha variado en el tiempo.
3. Que tipo de algoritmos no supervisados se adaptan a este problema.
   - Al ser un problema de clasificación por agrupamiento el algorimo que más se adapta el kmeans ya por las caracteristicas que se nos presenta el problema ademas ya tenemos definidas que existen 4 etapas lo que ayuda a poder utilizar ese valor como parametro dentro del algoritmo.
4. Es factible el deep learning para descubrir estos estados
   - Este tipo de problema sin lugar a dudas es para poder resolver de forma clasica con algorimos de clasificación no supervisado tal como se desarrollo en este challenge con el algoritmo k-means, pero con los avances que se han realizado en el campo del deep learning en los últimos años probablemente hay alguna posibilidad de experimentar con alguna arquitectura con la finalidad de poder inferir este tipo de problema y evaluar dicho comportamiento.
5. Es escalable la solución para todos los motores? o debes hacer el análisis por motor?
   - No necesariamente podría ser escalable con todos los motores ya que allí asumiriamos que son de las mismas caracteristicas todo y es algo que se desconoce con este conjunto de datos las caracateristicas de dichos motores como lo es su hp, voltaje, si son monofasicos, si es trifasico, pero nos ayuda en un inicio a poder tener una base de donde partir.
6. Escribe el código
   - El código se estructuro en diferentes jupyter-notebooks para poder prototipar la solución además de ello se hiz apoyo en el recurso de cookiecutter ya que ayuda en el desarrollo de proyectos de ciencia de datos el archivo 1.0-ggodoy-full_with_module.ipynb puede ser traslado a un archivo .py y de este modo poder ejercutar el script por completo.
7. Es escalable tu solución ¿Que dificultades tuvo el modelamiento? ¿Como harías escalable tu solución?
   - Falta generar el main para ejecutar y dejar de usar los notebooks que ayudaron a prototipar, sería muy bueno poder consultar las fuentes de los datos apra recabar mayor información que pueda dar una mayor certeza de la calidad de agrupación que se genero con el cmodelo apra ajustar y llegar a una mayor confiabilidad. Además poder almacenar esto como un modelo el cual podamos generar un relacolección constante de los datos que de igual forma permita darle un valor agregado al negocio no solo en este punto de calsificación para saber el estado de un registro sino que tambien poder ayuda a preveer llegar a punto de fallas de dichos motores que sean de estado 4 y tomar acciones tempranas. Una dificulta sin lugar a duda es no saber que significado tiene cada sensor ya que con eso pudieramos tener mayor capacidad de entendimeinto de los datos saber cual es la temperatura como caso critico dentro de los motores. Seguir generando modularización no solo de las gráficas que permitieron mejorar parate del prototipado. Las dimensionalidades a pesar de haber ocupado dentro de la libreria de scikit-learn para la reduccion de dimensionalidad y así poder plotear la solución generar mayores ajuste para que pueda ser mas claro la identificación de los vectores.
8. ¿Tus resultados son reproducibles en el tiempo?.
   - Al poder generar esta estructura base permite que podamos tener una base en el tiempo que sin lugar a dudas toca reforzar para que sea mucho más optimo los procesos y garantizar una calidad del resultado

### QUE ENTREGAR?

Un .csv con la columna unique_id y estado de la falla con un string de la siguiente forma
estado_{i}, donde i = 1, 2, 3 y 4
ejemplo: unique_id: 504, state: estado_1
ver el archivo ejemplo de resultados y debes dejarlo en 
data/result.csv
dando el link a tu repo de github.

### DICCIONARIO DE DATOS
* unique_id: id único de la fila, con el que serán evaluados tus resultados
* unit_nr: motor con el que se esta trabajando (total de 100)
* setting_{i]: seteo de las máquinas inicial
* s_{i}: sensores de distinta indole, presión, temperatura, caudal, etc.

### ANEXO
Este es un problema más que estudiado en la industria de mantenimiento, siempre podemos encontrar técnicas clásicas para resolver este problema, buscamos que salgas de la caja y ocupes lo más nuevo que conoces. Tampoco esperamos predicciones perfectas dado que el problema es complejo, al no conocer el ciclo del que fue obtenida la data, pero si buscamos formas de aproximarse a encontrar estos 4 estados mencionados, en la data, haciendolo de una manera no supervisada.
pistas: [clustering, reducción de dimensionalidad]

