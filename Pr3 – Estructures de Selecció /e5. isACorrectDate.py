"""Daniel David,Nizar El Khoulfi, Jaffet Hernandez

9/11/23

Programa que comprovi si una data és correcte. El programa ha de demanar una data, dia, mes i any
(en el format DD/MM/AAAA).  Cal recordar que hi ha anys de traspàs.
NO es pot fer servir funcions de calendari com ara datetime de Python.
"""

data = input("Cual es el dia del año, separado por /")
dia, mes, año = (data.split('/'))

if int(mes) >= 1 or int(mes) <=12:
  if int(mes) in (1, 3, 5, 7, 8, 10, 12):
    int(dia) <= 31
  if int(mes) in (4, 6, 9, 11):
      int(dia) <=30


if (int(año) % 4 == 0 and int(año) % 100 !=0) or (int(año) % 400 == 0):
    mes = 2
    int(dia) <=29
else:
    int(dia) <=28

print("La fecha és valida")
