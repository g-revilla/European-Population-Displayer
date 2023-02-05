#para ejecutar el script necesitas tener la libreria pandas y numpy
import pandas as pd
import numpy as np

#en este script simplemente cargamos los datos en un DataFrame y imprimimos en pantalla estos datos
df_poblacion = pd.read_excel("./datos_poblacion.xlsx", sheet_name="Sheet 1", header=7, nrows=55, index_col=0)
df_poblacion = df_poblacion.drop("GEO (Labels)")
df_poblacion = df_poblacion.drop(columns=["Unnamed: 2", "Unnamed: 4", "Unnamed: 6", "Unnamed: 8", "Unnamed: 10", "Unnamed: 12", "Unnamed: 14", "Unnamed: 16", "Unnamed: 18", "Unnamed: 20", "Unnamed: 22", "Unnamed: 24"])
df_poblacion = df_poblacion.replace(to_replace=':', value=np.nan)
df_poblacion = df_poblacion.astype('Int64')

print(df_poblacion)