from Personaje_clase import Personaje

# nombre, altura, velocidad, recistencia, fuerza
cantidadPersonaje = 0
while True:

  menuInicio = '''
  #########################################
  |     1 - Crear personaje               |
  |     2 - Carrera                       |
  |     3 - Salir                         |
  ######################################### '''

  print(menuInicio)
  opcion = int(input("Ingrse la opcón seleccionada: "))
  
  if opcion == 1:
   cantidadPersonaje = cantidadPersonaje + 1
     

  elif opcion == 2:
    print("En proceso")
    continue

  elif opcion == 3:
      break

p1 = Personaje ("Batman", 180, 80, 90, 70)
print (f"el personaje se llama {p1}")