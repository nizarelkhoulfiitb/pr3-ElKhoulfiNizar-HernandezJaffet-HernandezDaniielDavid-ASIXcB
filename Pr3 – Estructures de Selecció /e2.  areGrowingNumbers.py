"""Daniel David ,Nizar El Khoulfi, Jaffet Hernandez
8/11/23
Programa que detecta si tres números demanats
han estat introduïts en ordre creixent.
"""
numero1 = input("Dime un numero")
numero2 = input("Dime otro numero")
numeor3 = input("Dime otro numero")

if numero1 <= numero2 and numero2 <= numeor3:
    print("Los numeros stan en orden")
else:
    print("Los nuemeros no estan en orden")