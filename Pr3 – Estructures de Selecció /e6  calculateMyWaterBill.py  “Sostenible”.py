"""Daniel David,Nizar El Khoulfi, Jaffet Hernandez

9/11/23
"""
try:

    hab = input("Introdueix la lletra identificativa del teu tipus d'habitatge: ")
    gastado = float(input("Introdueix el número de m³ d'aigua gastats: "))

    if hab == "A":
        cuotaFija = 2.46
    if hab == "B":
        cuotaFija = 6.40
    if hab == "C":
        cuotaFija = 7.25
    if hab == "D":
        cuotaFija = 11.21
    if hab == "E":
        cuotaFija = 12.10
    if hab == "F":
        cuotaFija = 17.28
    if hab == "G":
        cuotaFija = 28.01
    if hab == "H":
        cuotaFija = 40.50
    if hab == "I":
        cuotaFija = 61.31

    print(cuotaFija)

    if gastado > 0:
        if gastado <= 6:
            precio = cuotaFija + gastado * 0.5849
        elif gastado >= 7 and gastado <= 9:
            precio = cuotaFija + gastado * 1.1699
        elif gastado >= 10 and gastado <= 15:
            precio = cuotaFija + gastado * 1.7548
        elif gastado >= 16 and gastado <= 18:
            precio = cuotaFija + gastado * 2.3397
        elif gastado > 18:
            precio = cuotaFija + gastado * 2.9246
    else:
        print("Introdueix un número vàlid de m³ d'aigua gastats")
        exit()
    print(f"El precio de tu factura es : {precio:.2f}€")

except ValueError:
    print("No has introducido valores validos")