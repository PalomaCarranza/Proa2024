#Registro de notas
#Ingresar la nota

from calculadora import suma


cantidadDeNotas=float(input("ingrese el número de notas que desea ingresar: "))
for i in range(cantidadDeNotas):
    nota= float(input("Ingrese la nota: "))
#Almacenar en una lista
notas=[]
while True:
    if nota>0 and nota<10:
        notas.append(nota)
    elif nota<0:
        print("Error: la nota no es válida")

#Verificar que la nota sea este entre 0 y 10

    
#Calcular el promedio
def promedio():
    suma 
    


#Mostrar el promedio y si aprobo o no