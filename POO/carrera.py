from Personaje_clase import Personaje

# nombre, altura, velocidad, recistencia, fuerza
cantidad_personaje = 0
personajes = []
while True:

  menuInicio = '''
  #########################################
  |     1 - Crear personaje               |
  |     2 - Jugar                         |
  |     3 - Salir                         |
  ######################################### '''

  print(menuInicio)
  opcion = int(input("Ingrese la opción seleccionada: "))
  
  if opcion == 1: # El usuario ingresa todos los atributos del personaje
    
    nombre = input("Ingrese el nombre del personaje: ")
    altura = int(input("Ingrese la altura del personaje (en cm): "))
    velocidad = int(input("Ingrese la velocidad del personaje: "))
    resistencia = int(input("Ingrese la resistencia del personaje: "))
    fuerza = int(input("Ingrese la fuerza del personaje: "))

    nuevo_personaje = Personaje (nombre, altura, velocidad, resistencia, fuerza)
    personajes.append (nuevo_personaje) # Guarda el personaje en la lista personajes

    cantidad_personaje += 1 # Se suma uno a cantidad_personaje
    print(f"El personaje {nuevo_personaje.nombre} ha sido creado con éxito.")
    print(f"Cantidad de personajes creados: {cantidad_personaje}")

  elif opcion == 2:
    if cantidad_personaje == 0:
      print("No hay personajes creados para jugar.")
    else:
      print("Iniciando la carrera con los siguientes personajes: ")
      for personaje in personajes:
        print(f" {personaje.nombre}")

    continue
   

  elif opcion == 3: # Sale del programa
    print("Saliendo del programa.")
    break

  

