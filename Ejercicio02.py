#Escribir un programa que pregunte al usuario su nombre, edad, dirección y
#teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el
#mensaje “<nombre> tiene <edad> años, vive en <dirección> y su número de
#teléfono es <teléfono>”.
nom = input('Cual es tu nombre: ')
años = input('Dime tu edad: ')
direc = input('Dame tu direccion: ')
tlfn = input('Cual es tu numero de telefono: ')
datos = {'Nombre':nom, 'Edad':años, 'Direccion':direc, 'Telefono':tlfn}
print(f'{nom} tiene {años} años, vive en {direc} y su numero de telefono es 
      {tlfn}')