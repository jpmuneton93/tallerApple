from generators.generadorApple import generarDatos
import pandas as pd

def analizarDatosApple():
    datos=generarDatos()
    tabla=pd.DataFrame(datos,columns=['productos', 'categoria'])
    tabla.to_csv("./data/productos.csv",index=False)
analizarDatosApple()