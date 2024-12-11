# Bucles en tu codigo con while

# Los bucles tienen la siguiente estructura:

# mientras haya algo que hacer:
#   hazlo

# Existe una similitud sintactica con la estructura If, sin embargo, tienen una gran diferencia semantica. La estructura If se repite SOLO UNA VEZ cuando la condicion evaluada es True, en cambio, los bucles se repiten TANTAS VECES como la condicion evaluada sea True

# Un problema frecuente cuando se está aprendiendo acerca de bucles es estar atrapado en un bucle infinito. Los bucles infinitos se crean ya que la condicion evaluada nunca deja de ser True, por lo tanto, el codigo se ejecuta infinitas veces

##############################
# Ejemplo de un bucle infinito
##############################

# while True:
#   print("Estoy atrapado en un bucle infinito")

# Ejemplo de un bucle en python que cuenta los numeros pares e impares

# numero_par = 0
# numero_impar = 0

# numero = int(input("Ingresa un numero para evaluar si es PAR o IMPAR. Escribe 0 para salir del programa: "))

# while numero != 0:
#     print("Estas en el bucle")
#     if numero % 2 == 1:
#         numero_impar += 1
#         print("Números pares: ", numero_par)
#         print("Números impartes: ", numero_impar)

#     else:
#         numero_par +=1
#         print("Números pares: ", numero_par)
#         print("Números impartes: ", numero_impar)

#     numero = int(input("Ingresa un numero para evaluar si es PAR o IMPAR. Escribe 0 para salir del programa: "))
# print("Saliste del bucle")

# Existen casos donde el bucle necesita recorrer un determinado numero de veces, para esto la estructura básica de cualquier bucle es definir: Un inicio, la condición y un incremento

# Ejemplo de un bucle limitado

# inicio = 0 # Este es el punto inicial del bucle
# while inicio < 10: # Esta es la condicion a cumplir del bucle, donde se limita el numero de veces que se va a recorrer a 10
#     inicio += 1 # Este es el incremento del contador, en este caso el contador es inicio, ya que si no se especifica el incremento el bucle será infinito
#     print(inicio)
# print("Saliste del bucle")

################################
# LAB: Adivina el numero secreto
################################

# Escenario

# Un mago junior ha elegido un número secreto. Lo ha escondido en una variable llamada secret_number. Quiere que todos los que ejecutan su programa jueguen el juego Adivina el número secreto, y adivina qué número ha elegido para ellos. ¡Quiénes no adivinen el número quedarán atrapados en un bucle sin fin para siempre! Desafortunadamente, él no sabe cómo completar el código.

# Tu tarea es ayudar al mago a completar el código en el editor de tal manera que el código:

# 1. pedirá al usuario que ingrese un número entero;
# 2. utilizará un bucle while;
# 3. comprobará si el número ingresado por el usuario es el mismo que el número escogido por el mago. Si el número elegido por el usuario es diferente al número secreto del mago, el usuario debería ver el mensaje "¡Ja, ja! ¡Estás atrapado en mi bucle!" y se le solicitará que ingrese un número nuevamente. Si el número ingresado por el usuario coincide con el número escogido por el mago, el número debe imprimirse en la pantalla, y el mago debe decir las siguientes palabras: "¡Bien hecho, muggle! Eres libre ahora."

# Codigo:

# secret_number = 777

# print(
# """
# +================================+
# | ¡Bienvenido a mi juego, muggle!|
# | Introduce un número entero     |
# | y adivina qué número he        |
# | elegido para ti.               |
# |¿Cuál es el número secreto?     |
# +================================+
# """)

# numero_secreto_introducido = int(input("Ingresa el numero secreto correcto ó entraras en un bucle: "))

# while numero_secreto_introducido != secret_number:
#     print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
#     numero_secreto_introducido = int(input("Ingresa el numero secreto correcto ó entraras en un bucle: "))
# print("¡Lograste escapar del bucle!")

# Bucles en tu codigo con For

# A veces es más importante contar los "giros o vueltas" del bucle que verificar las condiciones. Como vimos anteriormente en un bucle While, para realizar esto debiamos tener un contador e incrementarlo para contar cuantas veces se repite el bucle.

# Imagina que el cuerpo de un bucle debe ejecutarse exactamente cien veces. Si deseas utilizar el bucle while para hacerlo, puede tener este aspecto:

# i = 0
# while 0 < 100:
#     # Haz algo
#     i += 1

# # El bucle For si bien está diseñado para tareas más complicadas, puede "explorar" grandes colecciones de datos elemento por elemento. El mismo bucle de arriba se hace de la siguiente forma con un bucle For

# for i in range(100):
#     # Haz algo
#     pass

# Cualquier variable despues de la palabra reservada For es lo que se conoce como "variable de control del bucle", esta variable cuenta los iteraciones del bucle automaticamente
# La palabra in describe el rango de valores posibles que se asignan a la variable de control, es decir la variable de control i almacena 100 iteraciones
# La función range() es responsable de generar todos los valores deseados de la varaible de control, iniciando desde el 0
# Finalmente la palabra pass no hace nada en absoluto, es una "instrucción vacía". Su proposito es debido a que la sintaxis del bucle For exige al menos una instrucción dentro del cuerpo (al igual que las estructuras condicionales if, elif, else, while)

# Más acerca del bucle For y la funcion range()

# for i in range(2, 8, 3): # Los parametros de la funcion range en orden son: El limite inferior (incluido), el intervalo superior (no incluido) y el incremento, lo que en realidad es la diferencia entre los numeros generados por la funcion. La diferencia entre el resultado1 y el resultado2 es 3
#     print("El valor de i es", i)

# El resultado de este bucle es:
# El valor de i es 2
# El valor de i es 5

# Es importante saber que el conjunto generado por range() debe ordenarse de forma ascendente. Esto significa que el segundo argumento debe ser mayor que el primero

#####################################################################
# LAB Fundamentos del bucle for – contando lentamente (mississippily)
#####################################################################

# Escenario

# ¿Sabes lo que es Mississippi? Bueno, es el nombre de uno de los estados y ríos en los Estados Unidos. El río Mississippi tiene aproximadamente 2,340 millas de largo, lo que lo convierte en el segundo río más largo de los Estados Unidos (el más largo es el río Missouri). ¡Es tan largo que una sola gota de agua necesita 90 días para recorrer toda su longitud!

# La palabra Mississippi también se usa para un propósito ligeramente diferente: para contar mississippily (mississippimente).

# Si no estás familiarizado con la frase, estamos aquí para explicarte lo que significa: se utiliza para contar segundos.

# La idea detrás de esto es que agregar la palabra Mississippi a un número al contar los segundos en voz alta hace que suene más cercano al reloj, y por lo tanto "un Mississippi, dos Mississippi, tres Mississippi" tomará aproximadamente unos tres segundos reales de tiempo. A menudo lo usan los niños que juegan al escondite para asegurarse de que el buscador haga un conteo honesto.

# Tu tarea es muy simple aquí: escribe un programa que use un bucle for para "contar de forma mississippi" hasta cinco. Habiendo contado hasta cinco, el programa debería imprimir en la pantalla el mensaje final "¡Listos o no, ahí voy!"

# Utiliza el esqueleto que hemos proporcionado en el editor.

# import time

# Escribe un bucle for que cuente hasta cinco.
    # Cuerpo del bucle: imprime el número de iteración del bucle y la palabra "Mississippi".
    # Cuerpo del bucle, emplea : time.sleep(1)

# Escribe una función print con el mensaje final.



# Informacion extra

# Ten en cuenta que el código en el editor contiene dos elementos que pueden no ser del todo claros en este momento: la sentencia import time y el método sleep(). Vamos a hablar de ellos pronto.

# Por el momento, nos gustaría que supieras que hemos importado el módulo time y hemos utilizado el método sleep() para suspender la ejecución de cada función posterior de print() dentro del bucle for durante un segundo, de modo que el mensaje enviado a la consola se parezca a un conteo real. No te preocupes - pronto aprenderás más sobre módulos y métodos.

import time

# for count in range(1, 6):
#     print(count, " Mississippi")
#     time.sleep(1)
# print("Lista o no, aquí vengo!")

# Las sentencias break y continue

# Como desarrollador a veces nos enfrentamos a dos situaciones diferentes:

# 1. no es necesario continuar el bucle en su totalidad; se debe abstener de seguir ejecutando el cuerpo del bucle e ir más allá;
# 2. se necesita comenzar el siguiente giro del bucle sin completar la ejecución del turno actual.

# Break: sale del bucle inmediatamente, e incondicionalmente termina la operación del bucle; el programa comienza a ejecutar la instrucción más cercana después del cuerpo del bucle.

# Continue: se comporta como si el programa hubiera llegado repentinamente al final del cuerpo; el siguiente turno se inicia y la expresión de condición se prueba de inmediato.

# Estas adiciones que solo simplifican el trabajo del desarrollador se les denomina "Syntax sugar" lo que se traduce como dulce sintactico

###############################################
# LAB La sentencia break - atrapado en un bucle
###############################################

# Escenario

# La instrucción break se implementa para salir/terminar un bucle.

# Diseña un programa que use un bucle while y le pida continuamente al usuario que ingrese una palabra a menos que ingrese "chupacabra" como la palabra de output secreta, en cuyo caso el mensaje "Has dejado el bucle con éxito." debe imprimirse en la pantalla y el bucle debe terminar.

# No imprimas ninguna de las palabras ingresadas por el usuario. Utiliza el concepto de ejecución condicional y la sentencia break.

# chupacabra = input("Ingresa una palabra para entrar en el bucle o escribe chupacabra para salir. ")

# while chupacabra != "chupacabra":
#     if chupacabra == "chupacabra":
#         break
#     else:
#         chupacabra = input("Ingresa una palabra para entrar en el bucle o escribe chupacabra para salir. ")
# print("Has dejado el bucle con éxito")


#########################################################
# LAB La sentencia continue – el Feo Devorador de Vocales
#########################################################

# Escenario

# La sentencia continue se usa para omitir el bloque actual y avanzar a la siguiente iteración, sin ejecutar las sentencias dentro del bucle.

# Se puede usar tanto con bucles while y for.

# Tu tarea aquí es muy especial: ¡Debes diseñar un devorador de vocales! Escribe un programa que use:

# un bucle for;
# el concepto de ejecución condicional (if-elif-else).
# la sentencia continue.
# Tu programa debe:

# 1. pedir al usuario que ingrese una palabra.
# 2. utiliza user_word = user_word.upper() para convertir la palabra ingresada por el usuario a mayúsculas; hablaremos sobre los llamados métodos de cadena y el método upper() muy pronto, no te preocupes
# 3. utiliza la ejecución condicional y la instrucción continue para "devorar" las siguientes vocales A, E, I, O, U de la palabra ingresada.
# 4. imprime las letras no consumidas en la pantalla, cada una de ellas en una línea separada
# 5. Prueba tu programa con los datos que le proporcionamos.

# Datos de entrada: Gregory
# Salida esperada:
# G
# R
# G
# R
# Y 

# user_word = input("¡Ingresa una palabra para devorar sus vocales!: ")
# user_word = user_word.upper()

# for letter in user_word:
#     if letter == "A" or letter == "E" or letter == "I" or letter == "O" or letter == "U":
#         continue
#     else:
#         print(letter)
#         time.sleep(1)
# print("Has salido del devorador de vocales")

###########################################################
# LAB La sentencia continue – el Lindo Devorador de Vocales
###########################################################

# Escenario

# Tu tarea aquí es aún más especial que antes: ¡Debes rediseñar el devorador de vocales (feo) del laboratorio anterior y crear un mejor devorador de vocales (lindo) mejorado! Escribe un programa que use:

# un bucle for.
# el concepto de ejecución condicional (if-elif-else).
# la instrucción continue.
# Tu programa debe:

# pedir al usuario que ingrese una palabra.
# utilizar user_word = user_word.upper() para convertir la palabra ingresada por el usuario a mayúsculas; hablaremos sobre los llamados métodos de cadena y el upper() muy pronto, no te preocupes.
# emplea la ejecución condicional y la instrucción continue para "devorar" las siguientes vocales A , E , I , O , U de la palabra ingresada.
# asigna las letras no consumidas a la variable word_without_vowels e imprime la variable en la pantalla.
# Analiza el código en el editor. Hemos creado word_without_vowels y le hemos asignado una cadena vacía. Utiliza la operación de concatenación para pedirle a Python que combine las letras seleccionadas en una cadena más larga durante los siguientes giros de bucle, y asignarlo a la variable word_without_vowels.

# Prueba tu programa con los datos que le proporcionamos.

new_user_word = input("¡Ingresa una palabra para devorar sus vocales!: ")
new_user_word = new_user_word.upper()
word_without_vowels = ""

for letter in new_user_word:
    if letter == "A" or letter == "E" or letter == "I" or letter == "O" or letter == "U":
        continue
    else:
        print(letter, end="")

#################################
# LAB Fundamentos del bucle while
#################################

# Escenario

# Escucha esta historia: Un niño y su padre, un programador de computadoras, juegan con bloques de madera. Están construyendo una pirámide.

# Su pirámide es un poco rara, ya que en realidad es una pared en forma de pirámide - es plana. La pirámide se apila de acuerdo con un principio simple: cada capa inferior contiene un bloque más que la capa superior.

#Tu tarea es escribir un programa que lea la cantidad de bloques que tienen los constructores, y generar la altura de la pirámide que se puede construir utilizando estos bloques.

# Nota: La altura se mide por el número de capas completas - si los constructores no tienen la cantidad suficiente de bloques y no pueden completar la siguiente capa, terminan su trabajo inmediatamente.

# Prueba tu código con los datos que hemos proporcionado.

# blocks = int(input("Ingresa el numero de bloques para la piramide: "))
# height = 0
# remaining_blocks = blocks

# for layer in range (1, blocks + 1):
#     if remaining_blocks < layer:
#         break
#     else:
#         remaining_blocks -= layer
#         height += 1

# print("La altura de la pirámide es: ", height)


# LAB La hipótesis de Collatz

# En 1937, un matemático alemán llamado Lothar Collatz formuló una hipótesis intrigante (aún no se ha comprobado) que se puede describir de la siguiente manera:

# toma cualquier número entero que no sea negativo y que no sea cero y asígnale el nombre c0;
# si es par, evalúa un nuevo c0 como c0 ÷ 2;
# de lo contrario, si es impar, evalúe un nuevo  c0  como 3 × c0 + 1;
# si c0 ≠ 1, salta al punto 2.
# La hipótesis dice que, independientemente del valor inicial de c0, el valor siempre tiende a 1.

# Por supuesto, es una tarea extremadamente compleja usar una computadora para probar la hipótesis de cualquier número natural (incluso puede requerir inteligencia artificial), pero puede usar Python para verificar algunos números individuales. Tal vez incluso encuentres el que refutaría la hipótesis.

# Escribe un programa que lea un número natural y ejecute los pasos anteriores siempre que c0 sea diferente de 1. También queremos que cuente los pasos necesarios para lograr el objetivo. Tu código también debe mostrar todos los valores intermedios de c0.

# Sugerencia: la parte más importante del problema es como transformar la idea de Collatz en un bucle while- esta es la clave del éxito.

# Prueba tu código con los datos que hemos proporcionado.
c0 = int(input("Escribe un numero entero que no sea negativo y que no sea cero: "))
count = 0
while c0 != 1 and c0 > 0:
    count += 1
    if (c0 % 2) == 0:
        c0 = c0 / 2
        print(c0)
    else:
        c0 = 3 * c0 + 1
        print(c0)
print("Pasos = ", count)


for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    print(ch, end="")