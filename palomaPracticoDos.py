#Contar vocales en una frase
frase = input("Ingrese una frase: ")
vocales = "aeiouAEIOU"

numeroVocales = sum(1 for letra in frase if letra in vocales)
print(f"Número de vocales de la frase: {numeroVocales}")