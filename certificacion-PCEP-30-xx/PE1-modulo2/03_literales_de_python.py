# Un literal se refiere a datos cuyos valores están determinados por el literal mismo. 123 es un literal y c no lo es.
print("2")
print(2)
# Tienen la misma salida, pero internamente se almacenan totalmente diferentes en la memoria. La cadena se almacena como una serie de letras, mientras que el numero entero se almacena como una serie de bits.

# Enteros
# Todos los numeros manejados por computadoras son de dos tipos principalmente: Enteros y de punto flotante (floats) los cuales contienen una parte fraccionaria.
# En python los numeros no pueden ser separados por puntos, comas ó espacios, sin embargo desde Python 3.6 pueden separarse con _ para darle mayor legibilidad.

print(11_111_111_111_111) # El numero es mucho más legible que 11111111111111

# Numeros octales y hexadecimales

# Los numeros octales estan precedidos por el codigo 0o (cero-o), esto significa que el numero debe contenerse en digitos en el rango del [0..7]
# La funcion print() realiza la conversion de numeros octales automaticamente
print(0o123) # El numero equivalente es 83

# La segunda convencion nos permite utilizar numeros en hezadecimal. Dichos numeros deben ser precedidos por el prefijo 0x (cero-x)
# 0x123 es un numero hexadecimal con un valor igual a 291. La funcion print() puede manejar estos valores tambien.
print(0x123) # El numero equivalente es 291

# Flotantes
# Son numeros que tienen (o pueden tener) una parte fraccionaria despues del punto decimal.
2.5 
-0.4
# En este caso MI PYTHON no acepta como separador la coma (,) depende de la configuracion de python.
.4 # 0.4
4. # 4.0

# Notacion cientifica
# Para escribir numeros muy grandes o muy pequeños podemos utilizar notacion cientifica de la siguiente manera
3e8 # La letra e significa exponente

# Es importante saber que el resultado de Python, siempre será la presentacion mas corta del  numero, por ejemplo 1e-22 = 0.0000000000000000000001

# Cadenas
# Hay que recordar el uso de caracteres de escape para ciertas situaciones en las cadenas, por ejemplo

print("I\'am Monty Python")

# Valores Booleanos
# Se emplean para representar un valor muy abstracto "la veracidad", el nombre proviene de George Boole, el autor de "Las Leyes del Pensamiento", las cuales definen el algebra booleana

# LAB Literals de Python - Cadenas

#Escenario 
# Escriba un fragmento de código de una línea, utilizando la función print(), asi como los caracteres de nuevalinea y de escape, para que concida con el resultado esperado que muestra en la salida.

# Respuesta
print("\"Estoy\"\n\"\"aprendiendo\"\"\n\"\"\"Python\"\"\"")

# Extra
# Existe un literal adicional especial que es utilizado en Python, el literal es None, este literal es llamado un objeto de NoneType y puede ser utilizado para representar la ausencia de un valor

print(0b1011)