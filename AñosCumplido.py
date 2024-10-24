# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 20:19:44 2024

@author: ASUS
"""
import os
from datetime import datetime
import calendar

os.system("cls")
nombre = input("Cual es su nombre: \n")

# Solicitar al usuario que ingrese su fecha de nacimiento
fecha_nacimiento_str = input(f"{nombre} Por favor, seguidamente ingresa tu fecha de nacimiento" \
                            " (formato: DD/MM/AAAA): ")

# Convertir la cadena de texto ingresada en un objeto de tipo datetime

try:
    fecha_nacimiento = datetime.strptime(fecha_nacimiento_str, "%d/%m/%Y")
    print(f"{nombre} Tu fecha de nacimiento es: {fecha_nacimiento.date()}")
except ValueError:
    print("El formato de la fecha ingresada es incorrecto. Asegúrate de usar el formato DD/MM/AAAA.")

# Obtener la fecha actual para validar
fecha_actual = datetime.now()

# Comparar la fecha ingresada  de nacimiento con la fecha actual
if fecha_nacimiento < fecha_actual:

    # Guardar la fecha actual en la variable FechaActual
    FechaActual = datetime.today().date()

    # Calcular la edad exacta en años
    edad = FechaActual.year - fecha_nacimiento.year - ((FechaActual.month, FechaActual.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    print(f"{nombre} Tienes {edad} años cumplidos.")

    dias = FechaActual.day

    meses = 11 + (FechaActual.month - fecha_nacimiento.month)

    DifmesfechaNac = FechaActual.month - fecha_nacimiento.month - ((FechaActual.day) < (fecha_nacimiento.day))

    DifdiasfechaNac = FechaActual.day - fecha_nacimiento.day

    if DifmesfechaNac < 0 and DifdiasfechaNac == 0:
        print(f"mas exactamente tienes {edad} años, con {meses+1} meses y cero dias")
    elif DifmesfechaNac == 0 and DifdiasfechaNac < 0:
        # Obtener el último día del mes de la fecha de nacimiento
        ultimo_dia_mes = calendar.monthrange(fecha_nacimiento.year, fecha_nacimiento.month)[1]
        # Calcular los días restantes hasta el fin del mes
        dias_rest = ultimo_dia_mes - fecha_nacimiento.day
        print(f"mas exactamente tienes {edad} años, con cero meses y {dias+dias_rest} dias")
    elif DifmesfechaNac < 0:
        print(f"mas exactamente tienes {edad} años, con {meses} meses y {dias} dias")
    elif DifdiasfechaNac < 0:
        print(f"mas exactamente tienes {edad} años, con {DifmesfechaNac} meses y {dias} dias")
    else:
        print(f"mas exactamente tienes {edad} años, con {DifmesfechaNac} meses y {DifdiasfechaNac} dias")
else:
    print("LO SIENTO LA FECHA DE NACIMIENTO DEBE SER MENOR A LA FECHA DE HOY")