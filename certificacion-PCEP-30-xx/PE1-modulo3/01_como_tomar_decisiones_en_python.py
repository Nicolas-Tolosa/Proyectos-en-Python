# Preguntas y Respuestas

# Un programador escribe un programa y el programa hace preguntas. Una computadora ejecuta el programa y proporciona las respuesta. El programa debe ser capaz de reaccionar de acuerdo con las respuestas recibidas.


# Afortunadamente las computadoras soloconoces dos tipos de respuestas: Si, es verdadero ; No, esto es falso

# Para hacer preguntas, Python utiliza un conjunto de operadores muy especiales. Revisemos uno tras otro, ilustrando sus efectos en algunos ejemplos simples.

# Comparacion: operador de igualdad

# Pregunta: ¿son dos valores iguales?. Para hacer esta pregunta se utiliza el operador == (igual igual). Hay que diferenciar el operador de asignacion = , del operador de comparación ==

2 == 2  # El resultado es True
2 == 2. # El resultado es True, ya que convierte el valor entero en su equivalente real (2 a 2.0)
1 == 2  # El resultado es False

# Operadores

# Desigualdad: el operador no es igual a (!=)

# El operador != es lo contrario a ==, si ambos valores son iguales, el resultado de la comparación es False. Si no son iguales, el resultado de la comparación es True.

var = 0
print (var != 0) # El resultado es False

var = 1
print(var != 0) # El resultado es True

# Mayor que, mayor o igual que, menor que, menor o igual que

ovejas_negras = 40
ovejas_blancas = 20
ovejas_rosadas = 20

print(ovejas_negras > ovejas_blancas)  # El resultado es True
print(ovejas_negras >= ovejas_blancas) # El resultado es True
print(ovejas_negras < ovejas_blancas)  # El resultado es False

# Haciendo uso de las respuestas

# Existen al menos dos posibilidades: primero, puedes memorizarlo (almacenarlo en una variable) y utilizarlo más tarde. ¿Cómo haces eso? Bueno, utilizarías una variable arbitraria como esta:

# answer = number_of_lions >= number_of_lionseas # En este caso la variable es la respuesta a la pregunta

# La segunda posibilidad es mpás conveniente y mucho más común: puedes utilizar la respuesta que obtengas para tomar una decisión sobre el futuro del programa.

########################################
# LAB Variables - preguntas y respuestas
########################################

# Escenario

# Usando uno de los operadores de comparación en Python, escribe un programa simple de dos líneas que tome el parámetro n como entrada, que es un entero, e imprime False si n es menor que 100, y True if n es mayor o igual que 100.

# No debes crear ningún bloque if (hablaremos de ellos muy pronto). Prueba tu código usando los datos que te proporcionamos.

# Respuesta
# n = int(input())
# print("¿El valor que ingresaste es mayor que 100?:", n >= 100)

# Condiciones y ejecución condicional

# Para tomar decisiones, Python ofrece una instrucción especial. Debido a su naturaleza y su aplicaci´pn, se denomina instrucción condicional. Existen varias variantes de la misma. Comenzaremos con la mas simple.

# La primera forma de una sentencia condicional, que puede ver a continuacion, está escrita de manera muy informal pero figurada:

# if true_or_not:
#     do_this_if_true

# Si la expresion true_or_not representa la verdad, entonces las sentencias con indentacion se ejecutaran.
# Si la expresion true_or_not NO representa la verdad, entonces las sentencias con indentacion se omitiran, y la siguiente instruccion ejecutada será la siguiente al nivel de la sangria original.

# La sentencia if-else

# En simples palabras, si se cumplen las condiciones se ejecutará el plan A, sin embargo, si las cosas no salen como queremos (no se cumplen las condiciones) se ejecutará el plan B

# if true_or_false_condition:
#     perfom_if_condition_true
# else:
#     perform_if_condition_false

# Sentencias if-else anidadas

# Muchas veces dentro de un plan A tenemos ciertas decisiones internas que tomar. Ejemplo plan A: si hay un buen clima saldremos a caminar, si encontramos un buen restaurante almorzaremos ahi, de lo contrario vamos a comer un sandwich.

# Ejemplo plan B: si hay mal clima iremos al cine, si está la pelicula que quiero ver iremos a verla, de lo contrario iremos a comprar al centro comercial.

# if the_weather_is_good:
#     if nice_restaurant_is_found:
#         have_lunch()
#     else:
#         eat_a_sandwich()
# else:
#     if movie_is_available:
#         go_to_the_cinema()
#     else:
#         go_shopping()

# La sentencia elif

# Se parece a la anidación, pero en este caso la expresion busca reemplazar la etapa "de lo contrario". Se utiliza para verificar varias condiciones, cuando la primera es falsa pasa a la siguiente sentencia elif.

# if the_weather_is_good:
#     go_for_walk()
# elif movie_is_available:
#     go_to_the_cinema()
# elif table_is_available:
#     go_for_lunch()
# else:
#     play_chess_at_home()

# Esta forma de anidar sentencias if-elif se le denomina cascada. Además no se debe usar un else sin un if precedente, tambien es importante que el else es la ultima rama de la cascada. El else es opcional y puede omitirse.

# number1 = int(input("Ingresa un numero"))
# number2 = int(input("Ingresa un numero"))

# if number1 > number2: larger_number = number1
# else: larger_number = number2

# Pseudocodigo e introduccion a los bucles

# Por ahora ignoraremos los requisitos de la sintaxis de Python e intentaremos analizar el problema sin pensar en la programación real. En otras palabras, intentaremos escribir el algoritmo, y cuando estemos contentos con él, lo implementaremos.

# En este caso, utilizaremos un tipo de notación que no es un lenguaje de programación real (no se puede compilar ni ejecutar), pero está formalizado, es conciso y se puede leer. Se llama pseudocódigo.

# largest_number = -999_999_999
# number = int(input())
# if number == -1:
#     print(largest_number)
#     exit()
# if number > largest_number:
#     largest_number = number

#######################################################
# LAB Operadores de comparación y ejecución condicional
#######################################################

# Escenario

# Espatifilo, más comúnmente conocida como la planta de Cuna de Moisés o flor de la paz, es una de las plantas para interiores más populares que filtra las toxinas dañinas del aire. Algunas de las toxinas que neutraliza incluyen benceno, formaldehído y amoníaco.

# Imagina que tu programa de computadora ama estas plantas. Cada vez que recibe una entrada en forma de la palabra Espatifilo, grite involuntariamente a la consola la siguiente cadena: "¡Espatifilo es la mejor planta de todas!"

#Escribe un programa que utilice el concepto de ejecución condicional, tome una cadena como entrada y que:

# 1. imprima el enunciado "Si - ¡El Espatifilo! es la mejor planta de todos los tiempos!" en la pantalla si la cadena ingresada es "ESPATIFILIO" (mayúsculas)
# 2. imprima "No, ¡quiero un gran Espatifilo!" si la cadena ingresada es "espatifilo" (minúsculas)
# 3. imprima "¡Espatifilo!, ¡No [entrada]!" de lo contrario. Nota: [entrada] es la cadena que se toma como entrada.

# espatifilo = input("Prueba escribir ESPATIFILO, espatifilo, o alguna otra cosa: ")
# if espatifilo == "ESPATIFILO":
#     print("Si, ¡El Espatifilo! es la mejor planta de todos los tiempos!")
# elif espatifilo == "espatifilo":
#     print("No, ¡quiero un gran Espatifilo!")
# else:
#     print("¡Espatifilo!, ¡No {}!".format(espatifilo))

#########################################
# LAB Fundamentos de la sentencia if-else
#########################################

# Escenario

# Érase una vez una tierra de leche y miel - habitada por gente feliz y próspera. La gente pagaba impuestos, por supuesto - su felicidad tenía límites. El impuesto más importante, denominado Impuesto Personal de Ingresos (IPI, para abreviar) tenía que pagarse una vez al año y se evaluó utilizando la siguiente regla:

# si el ingreso del ciudadano no era superior a 85,528 pesos, el impuesto era igual al 18% del ingreso menos 556 pesos y 2 centavos (esta fue la llamada exención fiscal).
# si el ingreso era superior a esta cantidad, el impuesto era igual a 14,839 pesos y 2 centavos, más el 32% del excedente sobre 85,528 pesos.
# Tu tarea es escribir una calculadora de impuestos.

# 1. Debe aceptar un valor de punto flotante: el ingreso.
# 2. A continuación, debe imprimir el impuesto calculado, redondeado a pesos totales. Hay una función llamada round() que hará el redondeo por ti - la encontrarás en el código de esqueleto del editor.
# Nota: este país feliz nunca devuelve dinero a sus ciudadanos. Si el impuesto calculado es menor que cero, solo significa que no hay impuesto (el impuesto es igual a cero). Ten esto en cuenta durante tus cálculos.

# Observa el código en el editor - solo lee un valor de entrada y genera un resultado, por lo que debes completarlo con algunos cálculos inteligentes.

salary = float(input("Escribe tus ingresos para calcular tus impuestos: "))

if salary >= 85_528:
    tax = 14839.2 + ((salary-85_528)*0.32)
    print("El impuesto es: {} pesos".format(round(tax)))
elif salary < 0:
    tax = 0
    print("El impuesto es: {} pesos".format(round(tax)))
else:
    tax = (salary*0.18) - 556.2
    print("El impuesto es: {} pesos".format(round(tax)))

##############################################
# LAB Fundamentos de la sentencia if-elif-else
##############################################

# Escenario

# Como seguramente sabrás, debido a algunas razones astronómicas, el año puede ser bisiesto o común. Los primeros tienen una duración de 366 días, mientras que los últimos tienen una duración de 365 días.

# Desde la introducción del calendario Gregoriano (en 1582), se utiliza la siguiente regla para determinar el tipo de año:

# 1. si el número del año no es divisible entre cuatro, es un año común.
# 2. de lo contrario, si el número del año no es divisible entre 100, es un año bisiesto.
# 3. de lo contrario, si el número del año no es divisible entre 400, es un año común.
# 4. de lo contrario, es un año bisiesto.

# Observa el código en el editor - solo lee un número de año y debe completarse con las instrucciones que implementan la prueba que acabamos de describir.


# El código debe mostrar uno de los dos mensajes posibles, que son Año Bisiesto o Año Común, según el valor ingresado.

# Sería bueno verificar si el año ingresado cae en la era Gregoriana y emitir una advertencia de lo contrario: No dentro del período del calendario Gregoriano. Consejo: utiliza los operadores != y %.

# CODIGO 

# year = int(input("Introduce un año: "))

# if year < 1582:
# 	print("No esta dentro del período del calendario Gregoriano")
# else:
#     #  Escribe el bloque if-elif-elif-else aquí.

# Respuesta

year = int(input("Introduce un año: "))

if year < 1582:
	print("No esta dentro del período del calendario Gregoriano")
else:
    if (year % 4) != 0:
         print("Año común")
    elif (year % 100) != 0:
         print("Año bisiesto")
    elif (year % 400) != 0:
         print("Año común")
    else:
         print("Año bisiesto")
	