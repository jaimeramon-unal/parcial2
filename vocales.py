##desarrollar un programa que determine si en una lista se encuentra una cadena de caracteres con dos o mas vocales. Si la cadena existe debe imprimirla, y si no existe debe imprimir no existe 



# Función para verificar que no existan elementos repetidos
def lista_repetida(lista1):
    for elemento in lista1:
        if elemento == ('a,e,i,o,u'):
            print("existe una vocal", elemento)
        else: print("no existe una vocal")

def ingresar_lista():
    elementos = input("Ingrese los elementos de la lista separados por comas: ")
    return tuple(elemento.strip() for elemento in elementos.split(","))


print("Ingrese la lista:")
lista1 = ingresar_lista()