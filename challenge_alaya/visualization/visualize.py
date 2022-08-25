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