#Registro de notas
#Ingresar la nota

menu = '''
  ###############################################
  |     1 - Introducir nota                     |
  |     2 - Mostrar promedio y cantidad de notas|
  |     3 - Salir                               |
  ############################################### '''

print(menu)
opcion = int(input("Ingrse la opcIón seleccionada: "))

from calculadora import sum

if opcion == 1:
    cantidadDeNotas=float(input("ingrese el número de notas que desea ingresar: "))
    for i in range(cantidadDeNotas):
        nota= float(input("Ingrese la nota: "))
#Almacenar en una lista y verificar que la nota sea este entre 0 y 10
notas=[]
while True:
    if nota > 0 and nota < 11:
        notas.append(nota)
    elif nota < 0 or nota > 11:
        print("Error: la nota no es válida")
        print(menu)
#Calcular el promedio
def promedio():
    promedio = sum(notas) / cantidadDeNotas
    return promedio
if opcion == 2:
    promedio()
    print (f"De {cantidadDeNotas} el promedio es {promedio}")

if opcion == 3:
     


#Mostrar el promedio y si aprobo o no