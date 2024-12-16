# Logica de compuradoras

# Hasta ahora hemos utilizado condiciones bastante primitivas, "Si tenemos tiempo libre, y el clima es bueno, saldremos a caminar". Hemos utilizado la conjunción and (y), lo que significa que salir a caminar depende del cumplimiento simultáneo de estas dos condiciones. En el lenguaje de la lógica, tal conexión de condiciones se denomina conjunción. Y ahora otro ejemplo:

# Si tu estás en el centro comercial o yo estoy en el centro comercial, uno de nosotros le comprará un regalo a mamá. La aparición de la palabra or (o) significa que la compra depende de al menos una de estas condiciones. En lógica, este compuesto se llama una disyunción.

# Logica de computadoras

# El operador and, or y not

# Los operadores and, or y not en Python son operadores lógicos utilizados para evaluar expresiones booleanas. Se usan principalmente en condiciones y control de flujo, permitiendo combinar o invertir valores booleanos.

# Operadores logicos vs operaciones de bit

# Las operaciones lógicas en Python trabajan con valores booleanos (True y False) y se utilizan para evaluar expresiones de lógica booleana. Los operadores principales son and (y lógico), or (o lógico) y not (negación).

x = True and False # Resultado: False

# Operaciones de bits: Las operaciones de bits manipulan los valores a nivel binario (bits) y se aplican a números enteros. Los operadores principales incluyen & (AND), | (OR), ^ (XOR), ~ (complemento), y los desplazamientos de bits << (desplazamiento a la izquierda) y >> (desplazamiento a la derecha).

x = 5 & 3 # 5 (101) AND 3 (011) = 1 (001)

# Continuemos operando con bits

i = 15
j = 224

log = i and j

# Estamos tratando con una conjunción lógica aquí. Vamos a trazar el curso de los cálculos. Ambas variables i y j no son ceros, por lo que se considerará que representan a True. Al consultar la tabla de verdad para el operador and, podemos ver que el resultado será True. No se realizan otras operaciones.

# Ahora la operación a nivel de bits - aquí está:

bit = i & j

# El operador & operará con cada par de bits correspondientes por separado, produciendo los valores de los bits relevantes del resultado. Por lo tanto, el resultado será el siguiente:

#           i = 000000000000000000000000000_01111
#           j = 000000000000000000000000000_10110
# bit = i & j = 000000000000000000000000000_00110 = 6

# Veamos ahora los operadores de negación. Primero el lógico:

logneg = not i # La variable logneg se establecerá en False - no es necesario hacer nada más.

# La negación a nivel de bits es así:
bitneg = ~i
# Puede ser un poco sorprendente: el valor de la variable bitneg es -16. Esto puede parecer extraño, pero no lo es en absoluto. Si deseas obtener más información, debes consultar el sistema de números binarios y las reglas que rigen los números de complemento de dos.

#           i = 00000000000000000000000000001111
# bitneg = ~i = 11111111111111111111111111110000

# Cada uno de estos operadores de dos argumentos se puede utilizar en forma abreviada. Estos son los ejemplos de sus notaciones equivalentes:

# x = x & y            x &= y
# x = x | y            x |= y
# x = x ^ y            x ^= y

# Como tratar con bits individuales

# Ahora te mostraremos para que puedes usar los operadores de bit a bit. Imagina que eres un desarrollador obligado a escribir una pieza importante de un sistema operativo. Se te ha dicho que puedes usar una variable asignada de la siguiente forma:

# flag_register = 0x1234

# La variable almacena la información sobre varios aspectos de la operación del sistema. Cada bit de la variable almacena un valor de si/no. También se te ha dicho que solo uno de estos bits es tuyo - el tercero (recuerda que los bits se numeran desde cero y el número de bits cero es el más bajo, mientras que el más alto es el número 31). Los bits restantes no pueden cambiar, porque están destinados a almacenar otros datos. Aquí está tu bit marcado con la letra x:

# flag_register = 0000000000000000000000000000x000