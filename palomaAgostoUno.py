#Registro de notas
#Ingresar la nota

#def menu():

 # menuInicio = '''
  #########################################
  #|     1 - Suma                          |
  #|     2 - Resta                         |
  #|     3 - División                      |
  #|     4 - Multiplicación                |
  #|     5 - Salir                         |
  ######################################### '''

  #print(menuInicio)
  #opcion = int(input("Ingrse la opcón seleccionada: "))
  #return opcion 

#from calculadora import sum

#if opcion == 1:
 #   cantidadDeNotas=float(input("ingrese el número de notas que desea ingresar: "))
 #   for i in range(cantidadDeNotas):
 #       nota= float(input("Ingrese la nota: "))
#Almacenar en una lista y verificar que la nota sea este entre 0 y 10
#notas=[]
#while True:
 #   if nota > 0 and nota < 11:
 #       notas.append(nota)
 #   elif nota < 0 or nota > 11:
 #       print("Error: la nota no es válida")
 #       print(menu)
#Calcular el promedio
#def promedio():
 #   promedio = sum(notas) / cantidadDeNotas
 #   return promedio
#if opcion == 2:
 #   promedio()
 #   print (f"De {cantidadDeNotas} el promedio es {promedio}")

#if opcion == 3:
     
#Mostrar el promedio y si aprobo o no

# Programa para registrar y calcular el promedio de notas de un estudiante

# Función para mostrar el menú de opciones
def menu():
    menuInicio = '''
    #########################################
    |     1 - Ingresar notas                |
    |     2 - Calcular promedio             |
    |     3 - Verificar si aprobó           |
    |     4 - Salir                         |
    ######################################### '''
    print(menuInicio)

# Función para ingresar las notas
def ingresar_notas():
    notas = []  # Lista donde se almacenarán las notas
    while True:
        try:
            # Se intenta convertir la entrada del usuario a un número decimal (float)
            nota = float(input("Ingrese una nota (entre 0 y 10) o -1 para finalizar: "))
            if nota == -1:  # Condición para salir del ciclo
                break
            if 0 <= nota <= 10:  # Verificar que la nota esté en el rango permitido
                notas.append(nota)  # Agregar la nota a la lista
            else:
                print("Error: la nota debe estar entre 0 y 10.")
        except ValueError:
            # ValueError ocurre si el usuario ingresa un dato que no es numérico (por ejemplo, letras)
            print("Error: Debe ingresar un número válido.")
    return notas  # Retorna la lista de notas

# Función para calcular el promedio de las notas
def calcular_promedio(notas):
    if len(notas) > 0:  # len() devuelve la cantidad de elementos en la lista 'notas'
        promedio = sum(notas) / len(notas)  # Sumar todas las notas y dividir por la cantidad
        return promedio
    else:
        return 0  # Si no hay notas, el promedio es 0

# Función para verificar si el estudiante aprobó
def verificar_aprobacion(promedio):
    if promedio >= 7:
        print(f"El promedio es {promedio:.2f}. El estudiante ha aprobado.")
    else:
        print(f"El promedio es {promedio:.2f}. El estudiante no ha aprobado.")

# Programa principal
def main():
    notas = []
    while True:
        menu()  # Mostrar el menú de opciones
        try:
            # Se intenta convertir la entrada del usuario a un número entero (int)
            opcion = int(input("Ingrese la opción seleccionada: "))
        except ValueError:
            # ValueError ocurre si el usuario ingresa un dato que no es numérico (por ejemplo, letras)
            print("Error: Debe ingresar un número entero válido.")
            continue

        if opcion == 1:
            notas = ingresar_notas()  # Ingresar notas
            print(f"Notas ingresadas: {notas}")
        elif opcion == 2:
            if notas:
                promedio = calcular_promedio(notas)  # Calcular promedio
                print(f"El promedio de las notas es: {promedio:.2f}")
            else:
                print("No hay notas registradas.")
        elif opcion == 3:
            if notas:
                promedio = calcular_promedio(notas)  # Calcular promedio
                verificar_aprobacion(promedio)  # Verificar si aprobó o no
            else:
                print("No hay notas registradas.")
        elif opcion == 4:
            print("Saliendo del programa. ¡Hasta luego!")
            break  # Salir del ciclo y finalizar el programa
        else:
            print("Opción no válida. Intente nuevamente.")

# Llamamos a la función principal para ejecutar el programa
main()
