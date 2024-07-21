x = 10
y = 5
suma = x + y 
# Con cadenas format
print("Mis numeros son {} y {}".format(x,y))
print("Mis numeros son {} y {}".format(y,x))
print("La suma de los numeros {} y {} es igual a {}".format(x,y,suma))

#Con cadenas literales (f-strings)
print(f"Mis numeros son {x} y {y}")
print(f"Mis numeros son {y} y {x}")
print(f"La suma de los numeros {x} y {y} es igual a {suma}")


#Ejemplo 3
color = "Azul"
matricula= "75445"
print(f"El auto de color {color} tiene la matricula {matricula}")