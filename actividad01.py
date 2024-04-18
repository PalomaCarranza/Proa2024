#Paloma

import random
numAleatorio = random.randint(1,10)

while True:
 numJugador = int(input("Adivine el número del 1 al 10: "))

 if numJugador == numAleatorio:
  print(f"¡Adivinaste! El número es {numAleatorio}")
  break
 elif numJugador < numAleatorio:
  print("Le falta")
 else:
  print("Se paso")
print("Fin del juego")