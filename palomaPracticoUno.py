#Lista de números pares
numeros = []

for i in range(10):
    numero = int(input(f"Ingrese un número: "))
    numeros.append(numero)

numeros_pares = []

for numero in numeros:
    if numero % 2 == 0:
        numeros_pares.append(numero)

print("Los números pares ingresados son:", numeros_pares)






