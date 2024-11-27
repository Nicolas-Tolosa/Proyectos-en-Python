# Nombres de variables
# Si se desea nombrar una variable, se deben seguir las siguientes reglas:

# El nombre de la variable debe de estar compuesto por MAYÚSCULAS, minúsculas, dígitos, y el carácter _ (guion bajo)
# El nombre de la variable debe comenzar con una letra;
# El carácter guion bajo es considerado una letra;
# Las mayúsculas y minúsculas se tratan de forma distinta (un poco diferente que en el mundo real - Alicia y ALICIA son el mismo nombre, pero en Python son dos nombres de variable distintos, subsecuentemente, son dos variables diferentes);
# El nombre de las variables no pueden ser igual a alguna de las palabras reservadas de Python (las palabras clave - explicará más de esto pronto).

# El PEP 8 -- Style Guide for Python Code recomienda la siguiente convencion de nomenclatura para variables y funciones en Python: 

# Los nombres de las variables deben estar en minúsculas, con palabras separadas por guiones bajos para mejorar la legibilidad (por ejemplo, var, my_variable)
# Los nombres de las funciones siguen la misma convención que los nombres de las variables (por ejemplo, fun, my_function)
# También es posible usar letras mixtas (por ejemplo, myVariable), pero solo en contextos donde ese ya es el estilo predominante, para mantener la compatibilidad retroactiva con la convención adoptada.

# Como crear una variable
# Una variable se cra cuando se le asigna un valor, a diferencia de otros lenguajes de programacion no es necesario declararla.

numero = "3.8.5" # Se crea una variable ya que se le asigna un valor
print(numero) # Imprime en consola la variable

# No está permitido usar una variable que no exista
cadena = "hola mundo"
# print(cadena2) # Cadena2 no está definida

# Se pueden concatenar variables con cadenas de texto, utilizando el operador +, siempre y cuando la variable sea de tipo string
print("Python version: " + numero)

# Se puede reasignar un valor a una variable ya existente, por ejemplo la variable numero esta definida como "numero = "3.8.5" pero se puede sustituir por otro valor"

numero = "3.9.5"
print("Python version: " + numero)

# LAB variables

# Escenario

# Érase una vez en la Tierra de las Manzanas, Juan tenía tres manzanas, María tenía cinco manzanas, y Adán tenía seis manzanas. Todos eran muy felices y vivieron por muchísimo tiempo. Fin de la Historia.

# 1. Crear las variables: juan, maria, y adan;
# 2. Asignar valores a las variables. El valor debe de ser igual al número de manzanas que cada quien tenía;
# 3. Una vez almacenados los números en las variables, imprimir las variables en una línea, y separar cada una de ellas con una coma;
# 4. Después se debe crear una nueva variable llamada total_apples y se debe igualar a la suma de las tres variables anteriores;
# 5. Imprime el valor almacenado en total_apples en la consola;
# 6. Experimenta con tu código: crea nuevas variables, asigna diferentes valores a ellas, y realiza varias operaciones aritméticas con ellas (por ejemplo, +, -, *, /, //, etc.). Intenta poner una cadena con un entero juntos en la misma línea, por ejemplo, "Número total de manzanas:" y total_apples.

# Respuesta 1 y 2
juan = 3
maria = 5
adan = 6

# Respuesta 3
print(juan, maria, adan)

# Respuesta 4
total_apples = juan + maria + adan

# Respuesta 5
print(total_apples)

# Respuesta 6
print("juan tiene: {} manzanas, maria tiene: {} manzanas y adan tiene: {} manzanas, en total hay {} manzanas".format(juan, maria, adan, total_apples))

print("juan tiene: {2} manzanas, maria tiene: {3} manzanas y adan tiene: {0} manzanas, en total hay {1} manzanas".format(juan, maria, adan, total_apples))

# Operadores abreviados
# Muy seguido, se desea utilizar la misma variable al lado derecho y al lado izquierdo del operador = operator.

# Ejemplos
# x = x * 2
# oveja = oveja + 1

# Python ofrece una manera más corta de escribir operaciones como estas, lo cual se puede codificar de la siguiente manera:

# x *= 2
# oveja += 1

# LAB variables, un convertidor simple

# Escenario

# Millas y kilómetros son unidades de longitud o distancia. Teniendo en mente que 1 milla equivale aproximadamente a 1.61 kilómetros, complementa el programa en el editor para que convierta de:

# Millas a kilómetros;
# Kilómetros a millas.
# No se debe cambiar el código existente. Escribe tu código en los lugares indicados con ###. Prueba tu programa con los datos que han sido provistos en el código fuente.
# Pon mucha atención a lo que esta ocurriendo dentro de la función print(). Analiza como es que se proveen múltiples argumentos para la función, y como es que se muestra el resultado.
# Nota que algunos de los argumentos dentro de la función print() son cadenas (por ejemplo, "millas son", y otros son variables (por ejemplo, miles).

# Codigo: 

# kilometers = 12.25
# miles = 7.38

# miles_to_kilometers = ###
# kilometers_to_miles = ###

# print(miles, "millas son", round(miles_to_kilometers, 2), "kilómetros")
# print(kilometers, "kilómetros son", round(kilometers_to_miles, 2), "millas")

# Salida esperada

# 7.38 millas son 11.88 kilómetros
# 12.25 kilómetros son 7.61 millas

# Respuesta
kilometers = 12.25
miles = 7.38

miles_to_kilometers = 1.61 * miles
kilometers_to_miles = kilometers/1.61

print(miles, "millas son", round(miles_to_kilometers, 2), "kilómetros")
print(kilometers, "kilómetros son", round(kilometers_to_miles, 2), "millas")


# LAB operadores y expresiones

# Escenario

# Observa el código en el editor: lee un valor float, lo coloca en una variable llamada x, e imprime el valor de la variable llamada y. Tu tarea es completar el código para evaluar la siguiente expresión:

# 3x3 - 2x2 + 3x - 1

# El resultado debe ser asignado a y.

# Recuerda que la notación algebraica clásica muy seguido omite el operador de multiplicación, aquí se debe de incluir de manera explicita. Nota como se cambia el tipo de dato para asegurarnos de que x es del tipo float.

# Mantén tu código limpio y legible, y pruébalo utilizando los datos que han sido proporcionados. No te desanimes por no lograrlo en el primer intento. Se persistente y curioso.

# Codigo:

# x =  # Codifica tus datos de prueba aquí.
# x = float(x)
# # Escribe tu código aquí.
# print("y =", y)


# Salida esperada

# x = 0     y = -1.0
# x = 1     y = 3.0
# X = -1    y = -9.0

# Respuesta
x = 0
x = float(x)
y = ((3*x**3) - (2*x**2) + (3*x) - 1)
print("y =", y)

x = 1
x = float(x)
y = ((3*x**3) - (2*x**2) + (3*x) - 1)
print("y =", y)

x = -1
x = float(x)
y = ((3*x**3) - (2*x**2) + (3*x) - 1)
print("y =", y)

a = '1'
b = "1"
print(a+b)

a = 6
b = 3
a = a / 2 * b
print(a)