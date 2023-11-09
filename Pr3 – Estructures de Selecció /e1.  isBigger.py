"""Daniel David, Nizar El Khoulfi, Jaffet Hernandez.

8/11/23

Programa que demana dos números si el primer és més gran o igual que el segon els intercanvia.
I torna a mostrar els valors per pantalla
"""
numeros = input("Dime dos numeros")

numero1, numero2 = map(float, numeros.split())

if numero1 >= numero2:
    comparacion = numero1, numero2 = numero2, numero1
    print(comparacion)
else:
    print(numeros)
