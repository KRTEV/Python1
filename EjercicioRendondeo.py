#EJERCICIO 2
# Nombre del vendedor
Nombre_vendedor = input("Escribe tu nombre completo: ")

#cantidad de ingresos generados en el mes por el vendedor 

Venta_Total= float(input(f"\n{Nombre_vendedor} \n¿Cuantos ingresos has generado en el mes?: "))

# multiplicar los ingresos del usuario por 13 y dividirlo por 100, es decir, mirar el 13% de estos y dejarlos hasta 2 decimales

Comision= round(Venta_Total*13/100 , 2)

#Resultado

print(f"\nVendedor: {Nombre_vendedor}\nVenta total: ${Venta_Total}\nComision: ${Comision}") 