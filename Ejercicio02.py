#Escribir un programa que pregunte al usuario su nombre, edad, dirección y
#teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el
#mensaje “<nombre> tiene <edad> años, vive en <dirección> y su número de
#teléfono es <teléfono>”.
nom = input('Cual es tu nombre: ')
anos = input('Dime tu edad: ')
direc = input('Dame tu direccion: ')
tlfn = input('Cual es tu numero de telefono: ')
datos = {'Nombre':nom, 'Edad':anos, 'Direccion':direc, 'Telefono':tlfn}
print(datos['Nombre'], 'tiene', datos['Edad'], 'años, vive en',
      datos['Direccion'], 'y su numero de telefono es', datos['Telefono'])