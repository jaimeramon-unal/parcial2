##desarrollar un programa que determine si en una lista no existen elementos repetidos


# Función para verificar que elementos de una lista estan contenidos dentro de otra
def lista_repetida(lista1):
    # Verificamos que  elementos de lista1 están en lista2
    for elemento in lista1:
        if elemento not in lista1:
            return False  # Si algún elemento no está, retornamos False

    # Si todos los elementos están, retornamos True
    return True

# Función para ingresar una lista desde el teclado
def ingresar_lista():
    elementos = input("Ingrese los elementos de la lista separados por comas: ")
    # Convertimos la entrada en una lista, eliminamos espacios y luego en una tupla
    return tuple(elemento.strip() for elemento in elementos.split(","))

# Ingresar las tuplas desde el teclado
print("Ingrese la primera tupla:")
lista1 = ingresar_lista()

# Verificamos si tupla1 está contenida en tupla2
resultado = lista_repetida(lista1)

# Imprimimos el resultado
if resultado:
    print("\nLa lista si tiene elementos repetidos")
else:
    print("\nLa lista no tiene elementos repetidos")



