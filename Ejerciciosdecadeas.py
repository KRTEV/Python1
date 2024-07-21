# PRACTICA FORMATEAR CADENAS 1  
# Ejercicio 1

nombre_asociado= input("Digite su nombre: ")
numero_asociado= int(input("Ingresa tu numero de asociado: "))

#con .format
print("Estimado/a {}, su numero de asociado es: {}".format(nombre_asociado, numero_asociado))

#con cadena literal (f-strings)
print(f"Estimado/a {nombre_asociado}, su numero de asociado es: {numero_asociado}")

#Ejercicio 2

puntos_actuales = 10
puntos_nuevos = 7
puntos_totales = puntos_actuales+puntos_nuevos

#con .format
print("Has ganado {} puntos! En total, acumulas {} puntos.".format(puntos_nuevos, puntos_totales))

#con cadena literal (f-strings)
print(f"Has ganado {puntos_nuevos} puntos! En total, acumulas {puntos_totales} puntos")


# Ejercicio 3

puntos_actuales2 = 17
puntos_nuevos2= int(input("Puntos nuevos: "))
puntos_totales2= puntos_actuales2+puntos_nuevos2

#con .format()
print("Has ganado {} puntos! En total, acumulas {} puntos.".format(puntos_nuevos2, puntos_totales2))

#con cadena literal (f-strings)
print(f"Has ganado {puntos_nuevos2} puntos! En total, acumulas {puntos_totales2} puntos.")