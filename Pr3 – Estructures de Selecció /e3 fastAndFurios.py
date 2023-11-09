"""Daniel David,Nizar El Khoulfi, Jaffet Hernandez
8/11/23

Volem un programa que calculi la velocitat instantània i la velocitat mitjana.
Cal demanar velocitat inicial (m/s), l'acceleració (m/s2) i el temps. Si la velocitat
instantània és inferior o igual a 0, has d'indicar que està parat i no pots calcular la velocitat mitjana.

velocitat instantània = velocitat inicial + acceleració * temps
velocitat mitjana = (velocitat inicial + velocitat instantània)/2
424.567 23.367 24.2
"""
inicial = float(input("Dime la velocitat inicial en m/s: "))
aceleracion = float(input("Dime la aceleracion en m/s²: "))
temps = float(input("Dime el tiempo: "))

instantania = round(inicial + (aceleracion * temps),2)

if instantania <= 0:
    print("Esta parat, no e spor calcular la velocitat mitjana")
else:
    mitjana =round((inicial + instantania)/2,2)
    print("La velocitat instantania es,", instantania, "y la mitjana es,", mitjana)