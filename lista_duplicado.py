##desarrollar un programa que dadas dos listas determine que elementos tiene la primera lista que no tenga la segunda 

# Función para verificar que elementos de una lista estan contenidos dentro de otra
def lista_contenida(lista1,lista2):
    # Verificamos que  elementos de lista1 están en lista2
    for elemento in lista1:
        if elemento not in lista2:
            print("estos son los elementos que tiene la primer lista que no tiene la segunda", elemento)


# Función para ingresar una lista desde el teclado
def ingresar_lista():
    elementos = input("Ingrese los elementos de la lista separados por comas: ")
    # Convertimos la entrada en una lista, eliminamos espacios y luego en una tupla
    return tuple(elemento.strip() for elemento in elementos.split(","))

# Ingresar las lista desde el teclado
print("Ingrese la primera lista:")
lista1 = ingresar_lista()

print("\nIngrese la segunda lista:")
lista2 = ingresar_lista()

# Verificamos que elementos de la lista1 estan contenidos en lista2
resultado = lista_contenida(lista1, lista2)

# Imprimimos el resultado
if resultado:
    print("\n estos son los elementos que tiene la primera lista que no tiene la segunda")
