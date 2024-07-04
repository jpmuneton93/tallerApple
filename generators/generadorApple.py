import random

def generarDatos():
    productos=['Musica', 'TV', 'Aplicaciones', 'PC', 'Celulares', 'Tablets', 'Accesorios']
    datos=[]
    for producto in productos:
        categoria=random.choice(['Plus', 'Mega', 'Basic'])
        productosArreglo=[producto, categoria]
        datos.append(productosArreglo)
    return datos

print(generarDatos())
