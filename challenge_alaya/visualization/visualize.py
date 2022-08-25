import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def plot_work_by_motor(df: pd.DataFrame):
    """
        Función que me permite graficar la cantidad de trabajo por motores
    """
    sns.set(rc = {'figure.figsize':(30,15)})
    sns.barplot(
        x=df['unit_nr'].unique(),
        y=df['unit_nr'].value_counts(), 
        data=df)
    plt.title('Cantidad de trabajo por motores')
    plt.show()

def plot_correlation_heatmap(df: pd.DataFrame):
    """
        Función que permite crear la matriz de correlación del dataframe
    """
    plt.figure(figsize=(30, 15))
    heatmap = sns.heatmap(
        df.corr(), 
        vmin=-1, 
        vmax=1, 
        annot=True, 
        cmap='BrBG')
    heatmap.set_title('Correlation Heatmap', fontdict={'fontsize':18}, pad=12);
    plt.show()

def plot_elbow_method(inercia):
    """
        Se traza la curva de la suma de errores cuadráticos
    """
    plt.figure(figsize=[10,6])
    plt.title('Método del Codo')
    plt.xlabel('Nº. de clusters')
    plt.ylabel('Inercia')
    plt.plot(list(range(1,20)), inercia, marker='o')
    plt.show()

def plot_result(pca, centroides_pca, modelo_pca, etiquetas, df: pd.DataFrame):
    """
        GRAFICAR LOS DATOS JUNTO A LOS RESULTADOS
    """
    # Se define los colores de cada clúster
    colores = ['blue', 'red', 'green', 'orange']

    # Se asignan los colores a cada clúster 
    colores_cluster = [colores[etiquetas[i]] for i in range(len(pca))]

    #Se grafica los componentes PCA
    plt.scatter(pca[:, 0], pca[:, 1], c = colores_cluster, marker = 'o',alpha = 0.4)

    #Se grafican los centroides
    plt.scatter(centroides_pca[:, 0], centroides_pca[:, 1], marker = 'x', s = 100, linewidths = 3, c = colores)

    #Se guadan los datos en una variable para que sea fácil escribir el código
    xvector = modelo_pca.components_[0] * max(pca[:,0])
    yvector = modelo_pca.components_[1] * max(pca[:,1])
    columnas = df.columns

    #Se grafican los nombres de los clústeres con la distancia del vector
    for i in range(len(columnas)):
        #Se grafican los vectores
        plt.arrow(0, 0, xvector[i], yvector[i], color = 'black', width = 0.0005, head_width = 0.02, alpha = 0.75)
        #Se colocan los nombres
        plt.text(xvector[i], yvector[i], list(columnas)[i], color='black', alpha=0.75)
        
    plt.show()