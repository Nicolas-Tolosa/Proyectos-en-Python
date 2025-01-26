# La vida al interior de las listas

list_1 = [1] # Se crea una lista llamada list_1 que contiene un elemento: el número 1. En la memoria, se reserva un espacio para esta lista y list_1 apunta a ese espacio.

list_2 = list_1 # Aquí, no se crea una nueva copia de la lista. En lugar de eso, list_2 apunta al mismo lugar en la memoria que list_1. Ambas variables (list_1 y list_2) ahora están conectadas al mismo contenido.

list_1[0] = 2 # Cambias el valor del primer elemento de la lista usando list_1. Como list_1 y list_2 apuntan al mismo lugar, ese cambio también se refleja en list_2.

print(list_2) # Muestra [2] porque list_2 sigue apuntando al mismo contenido que list_1.

# Rebanadas poderosas (Slice)

# Una rebanada es un elemento de la sintaxis de Python que permite hacer una copia nueva de una lista, o partes de una lista.

# En realidad, copia el contenido de la lista, no el nombre de la lista.




 
