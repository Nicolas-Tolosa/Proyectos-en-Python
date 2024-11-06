# ESCENARIO

# El comando print(), el cual es una de las directivas más sencillas de Python, simplemente imprime una línea de texto en la pantalla.



# En tu primer laboratorio:

# 1. Utiliza la función print() para imprimir la linea ¡Hola, Mundo! en la pantalla. Usa comillas dobles alrededor de la cadena.

# 2. Habiendo hecho eso, usa la función print() nuevamente, pero esta vez imprime tu nombre.

# 3. Elimina las comillas dobles y ejecuta tu código. Mira la reacción de Python. ¿Qué tipo de error arroja?

# 4. Luego, elimina los paréntesis, vuelve a colocar las comillas dobles y ejecuta tu código nuevamente. ¿Qué tipo de error arroja esta vez?

# 5. Experimenta todo lo que puedas. Cambia las comillas dobles a comillas simples, usa múltiples funciones print() en la misma línea, y luego en diferentes líneas. Mira qué pasa.

# Respuestas

# Respuesta 1
print("¡Hola, Mundo!")

# Respuesta 2
print("nicolas")

# Respuesta 3
# print(nicolas) el error "nicolas is not defined" significa que la variable nicolas no está definida

# Respuesta 4
# print"nicolas" el error que aparece "statements must be separated by colon or semicolon" significa que la sintaxis para separar bloques de codigo o declaraciones es incorrecta

# Respuesta 5
print('hola mundo')
# print('hola mundo') print('hola mundo') ; ocurre el error "statements must be saparated by colon or semicolon" al no estar separados correctamente los bloques de codigo

# CARACTERES DE ESCAPE Y NUEVA LINEA

# Para representar un salto de linea se puede representar de dos formas, una utilizando la funcion print() sin argumentos ó utilizando "caracteres de escape".
# Existe una lista de caracteres de escape y se utilizan en muchos lenguajes de programacion, concretamente para el salto de linea se utiliza "\n". De esta forma el texto seguido de \n aparecerá en una nueva linea.
# La letra n viene de la palabra newline

print("hola\nmundo")
print("hola mundo \\") # Se utiliza \\ para poder representar en pantalla un solo \

# MULTIPLES ARGUMENTOS

print("hola", "mundo", "estos son", "muchos argumentos")  # Es importante destacar que no es necesario escribir un espacio " " al final de cada palabra para que aparezcan separadas.