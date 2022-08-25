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