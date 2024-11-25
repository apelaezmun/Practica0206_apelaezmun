#Escribir un programa que guarde en un diccionario los precios de los artículos
#de la tabla, pregunte al usuario por un artículo, un número de unidades y
#muestre por pantalla el precio de esa cantidad de producto. Si el producto no
#está en el diccionario debe mostrar un mensaje informando de ello.
precios = {'Pan':1.40, 'Huevos':2.30, 'Cebolla':0.85, 'Aceite':4.35}
articulo = input('Que articulo desea: ').capitalize()
cantidad = float(input(f'¿Cuanto quiere de {articulo}?: '))
if articulo in precios:
    precio = precios[articulo] * cantidad
    print(f'El precio de {articulo} es de {precio :.2f}€')
else:
    print('No tenemos ese producto')