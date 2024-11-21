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

print("hola", "mundo", "estos son", "muchos argumentos")  # Es importante destacar qu sario escribir un espacio " " al final de cada palabra para que aparezcan separadas.

# ARGUMENTOS DE PALABRA CLAVE

# Cualquier argumento de palabra clave debe colocarse después del último argumento posicional (esto es muy importante)
# El comportamiento predeterminado de "end" refleja la situación en la que el argumento de palabra clave end se usa implícitamente de la siguiente manera: end="\n".

#########################################
# LAB La función print() y sus argumentos

# ESCENARIO

# Modifica la primera línea de código en el editor, usando las palabras claves reservadas sep y end, para que se obtenga la salida esperada. Emplea dos funciones print() en el editor.
# No cambies nada en la segunda invocación del print().

print("Programming","Essentials","in")
print("Python")

# Respuesta 1: Salida esperada => Programming***Essentials***in...Python
print("Programming","Essentials","in",sep="***",end="...")
print("Python")

# LAB Dando formato a la salida

# ESCENARIO

# Te recomendamos encarecidamente que juegues con el código que hemos escrito para y realiza algunos (quizás incluso destructivos) cambios. Siéntete libre de modificar cualquier parte del código, pero hay una condición - aprende de tus errores y saca tus propias conclusiones.

# Intenta:

# 1. minimizar el número de invocaciones de la función print() insertando \n en las cadenas;
# 2. hacer que la flecha sea el doble de grande (pero mantener las proporciones)
# 3. duplica la flecha, colocando ambas flechas una al lado de la otra; nota: una cadena se puede multiplicar usando el siguiente truco: "string" * 2 producirá "stringstring" (pronto contaremos más al respecto)
# 4. elimina cualquiera de las comillas y observe detenidamente la respuesta de Python; presta atención a dónde Python ve un error - ¿es este el lugar donde realmente existe el error?
# 5. haz lo mismo con algunos de los paréntesis;
# 6. cambia cualquiera de las palabras print por otra cosa, que difiera solo en mayúsculas y minúsculas (por ejemplo, Print) - qué sucede ahora?
# 7. reemplaza algunas de las comillas con apóstrofes; observa lo que sucede con cuidado.

# Codigo: 



print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")

# Respuesta 1
print("    *","   * *","  *   *"," *     *","***   ***","  *   *","  *   *","  *****",sep="\n")

# Respuesta 2
print("        *")
print("       * *")
print("      *   *")
print("     *     *")
print("    *       *")
print("   *         *")
print("  *           *")
print(" *             *")
print("******     ******")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *******")

# Respuesta 3
print("    *     "*2)
print("   * *    "*2)
print("  *   *   "*2)
print(" *     *  "*2)
print("***   *** "*2)
print("  *   *   "*2)
print("  *   *   "*2)
print("  *****   "*2)

# Respuesta 4
# print("    *)
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")

# El error que aparece "statements must be separated by colon or semicolon" significa que la sintaxis para separar bloques de codigo o declaraciones es incorrecta

# Respuesta 5
# Print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")

# El error "is not defined" significa que la variable "Print" no está definida

# Respuesta 6
print('    *')
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")

# No hay ningun error al cambiar las doble comillas "" por apostrofes ''

print('Greg\'s book.')
print("'Greg's book.'")
print('"Greg\'s book."')
print("Greg\'s book.")