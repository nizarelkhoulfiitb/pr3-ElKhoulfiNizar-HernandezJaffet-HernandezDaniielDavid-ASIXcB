"""Daniel David ,Nizar El Khoulfi, Jaffet Hernandez

8/11/23

Programa que demana l'import d'una factura, amb iva inclòs. Calcula l'import amb descompte,
en cas de tenir la targeta de client, tenint en compte els següents criteris:

Si l'import de la factura, és igual o superior a 100 €, se li aplica un descompte
del 21%, en cas contrari no se li aplica cap descompte. El descompte es calcula al preu final,
i no a la “base imponible”. I després si li aplica l’IVA . Precio total = Base imponible * Tipo de IVA

"""
factura = float(input("Dime el valor de la factura con IVA incluido "))
targeta = float(input("Si tienes tajeta pon un 1 si no, pon 0 ?"))

if factura >= 100 and targeta == 1 :
    descuento = factura * 0.79
    final = round(descuento * 1.21,2)
    print ("El precio final es de ", final,"€")
else:
    print("No tienes descuento, el precio final es de,",factura,"€")
