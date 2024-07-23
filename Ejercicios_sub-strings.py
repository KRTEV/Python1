# 1) Extrae la primera palabra de la siguiente frase utilizando slicing,
#  y muestrala en pantalla: 
Texto = "Controlar la complejidad es la esencia de la programación"
Extraccion= Texto[0:10]
print(Extraccion)

# 2) Toma cada tercer caracter empezando desde el noveno hastra el final de la frase,
# e imprime el resultado

Texto2= "Nunca confies en un ordenador que no puedas lanzar por una ventana"
Extraccion2= Texto2[9:65:3] #se puede dejar asi Extraccion2= Texto2[9::3] y toma el texto total
print(Extraccion2) 


# 3 ) Invierte la posicion de todos los caracteres de la siguiente frase y muestra
# el resultado en pantalla:

Texto3= "Es genial trabajar con ordenadores, No discuten, lo recuerdan todo y no beben tu cerveza"
Extraccion3= Texto3[::-1]
print(Extraccion3)