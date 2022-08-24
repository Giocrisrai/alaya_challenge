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
2. Como encontrarías estos estados sin conocer la data, todos los sensores aportan información? con cuales trabajarías?
3. Que tipo de algoritmos no supervisados se adaptan a este problema
4. Es factible el deep learning para descubrir estos estados
5. Es escalable la solución para todos los motores? o debes hacer el análisis por motor?
6. Escribe el código
7. Es escalable tu solución ¿Que dificultades tuvo el modelamiento? ¿Como harías escalable tu solución? 
8. ¿Tus resultados son reproducibles en el tiempo?

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

