#Escribir un programa que cree un diccionario vacío y lo vaya llenado con
#información sobre una persona (por ejemplo nombre, edad, sexo, teléfono,
#correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un
#nuevo dato debe imprimirse el contenido del diccionario.
diccionario = {}
parar = ''
while parar != 'parar':
    clave = input('Dame un dato a añadir: ')
    valor = input('Dame el valor del dato: ')
    diccionario[clave] = valor
    print(diccionario)
    parar = input('Esribir "parar" cuando no haya mas datos o pulsar enter '
                  'para continuar: ')