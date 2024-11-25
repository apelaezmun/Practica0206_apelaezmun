#Escribir un programa que guarde en una variable el diccionario {'Euro':'€',
#'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su
#símbolo o un mensaje de aviso si la divisa no está en el diccionario.
moneda = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
divisa = input('Dime una divisa: ')
if divisa in moneda:
    print('El simbolo de', {divisa}, 'es', {moneda[divisa]})
else:
    print('Esta divisa no esta en el diccionario.')