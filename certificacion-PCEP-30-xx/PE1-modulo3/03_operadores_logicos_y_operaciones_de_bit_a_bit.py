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

# ¿Qué queremos hacer?
# Queremos saber si nuestro bit (el tercer bit, contando desde 0) está en 1 o en 0, sin preocuparnos por los otros bits de la variable.

# ¿Cómo lo hacemos?
# Usamos una máscara de bits: un número que tiene un 1 solo en la posición del bit que nos interesa y 0 en todas las demás posiciones. En este caso, la máscara es 0b1000 (en binario), que equivale a 8 en decimal.

# Operador AND (&): Comparamos la variable flag_register con la máscara. Solo el bit que nos interesa puede afectar el resultado:

# Si el bit está en 1, el resultado será 8 (la máscara).
# Si el bit está en 0, el resultado será 0.
# python
# Copiar
# Editar
# the_mask = 8  # Máscara para el tercer bit
# if flag_register & the_mask:  # Usamos AND con la máscara
#     print("El tercer bit está en 1")
# else:
#     print("El tercer bit está en 0")
# 2. Reiniciar tu bit
# ¿Qué queremos hacer?
# Queremos poner el tercer bit en 0, dejando todos los demás bits intactos.

# ¿Cómo lo hacemos?
# Usamos el operador AND (&) con una máscara que tiene 0 en la posición del bit que queremos cambiar, y 1 en todas las demás posiciones.

# La máscara se crea negando la máscara original:

# Máscara original: 0b1000 (tercer bit en 1).
# Máscara negada: ~0b1000 = 0b11110111 (tercer bit en 0, los demás en 1).
# Cómo funciona AND (&):

# Si un bit en la máscara es 0, el resultado será 0 para ese bit.
# Si un bit en la máscara es 1, el resultado será el mismo que el bit original.
# python
# Copiar
# Editar
# flag_register &= ~the_mask  # Reinicia el tercer bit
# 3. Establecer tu bit
# ¿Qué queremos hacer?
# Queremos poner el tercer bit en 1, dejando todos los demás bits como están.

# ¿Cómo lo hacemos?
# Usamos el operador OR (|) con una máscara que tiene 1 solo en la posición del bit que queremos cambiar.

# Cómo funciona OR (|):

# Si un bit en la máscara es 1, el resultado será 1 para ese bit.
# Si un bit en la máscara es 0, el resultado será el mismo que el bit original.
# python
# Copiar
# Editar
# flag_register |= the_mask  # Establece el tercer bit
# 4. Negar tu bit
# ¿Qué queremos hacer?
# Queremos alternar el valor del tercer bit:

# Si es 1, lo ponemos en 0.
# Si es 0, lo ponemos en 1.
# ¿Cómo lo hacemos?
# Usamos el operador XOR (^) con una máscara que tiene 1 solo en la posición del bit que queremos cambiar.

# Cómo funciona XOR (^):

# Si un bit en la máscara es 1, el resultado será el opuesto del bit original.
# Si un bit en la máscara es 0, el resultado será igual al bit original.
# python
# Copiar
# Editar
# flag_register ^= the_mask  # Niega el tercer bit

# Desplazamiento binario a la izquierda y desplazamiento binario a la derecha

# Python ofrece otra operación relacionada con los bits individuales: shifting. Esto se aplica solo a los valores de número entero, y no debe usar flotantes como argumentos para ello.

# Ya aplicas esta operación muy a menudo y muy inconscientemente. ¿Cómo multiplicas cualquier número por diez? Echa un vistazo:

# 12345 × 10 = 123450

# Como puede ver, multiplicar por diez es de hecho un desplazamiento de todos los dígitos a la izquierda y llenar el vacío resultante con cero.

# ¿División entre diez? Echa un vistazo:

# 12340 ÷ 10 = 1234

# Dividir entre diez no es más que desplazar los dígitos a la derecha.

# La computadora realiza el mismo tipo de operación, pero con una diferencia: como dos es la base para los números binarios (no 10), desplazar un valor un bit a la izquierda corresponde a multiplicarlo por dos; respectivamente, desplazar un bit a la derecha es como dividir entre dos (observa que se pierde el bit más a la derecha).

# Los operadores de cambio en Python son un par de dígrafos: < < y > >, sugiriendo claramente en qué dirección actuará el cambio.

# valor << bits
# valor >> bits

# El argumento izquierdo de estos operadores es un valor entero cuyos bits se desplazan. El argumento correcto determina el tamaño del desplazamiento.

# Esto demuestra que esta operación ciertamente no es conmutativa

# La prioridad de estos operadores es muy alta. Los verás en la tabla de prioridades actualizada, que te mostraremos al final de esta sección.

# Echa un vistazo a los turnos en la ventana del editor.

# 17 >> 1 → 17 // 2 (17 dividido entre 2 a la potencia de 1) → 8 (desplazarse hacia la derecha en un bit equivale a la división entera entre dos)
# 17 << 2 → 17 * 4 (17 multiplicado por 2 a la potencia de 2) → 68 (desplazarse hacia la izquierda dos bits es lo mismo que multiplicar números enteros por cuatro)

