"""
Lista Doblemente enlazada :D
Una lista doblemente enlazada es una lista enlazada
de nodos, donde cada nodo tiene un par de
campos de enlace, uno del nodo siguiente, y otro
al anterior.
Caracteristicas:
1- Recorrer la Estructura en ambos sentidos,
de inicio a fin y de fin a inicio

2- Borrado mas simple de datos
3- Estructura dinamica
"""
from lista_doblemente_enlazada import ListaDoblementeEnlazada
from os import system

system("clear")

lista = ListaDoblementeEnlazada()

lista.agregar_final(12)
lista.agregar_final(56)
lista.agregar_final(21)
lista.agregar_final(10)
lista.agregar_final(11)



lista.eliminar_inicio()
lista.eliminar_inicio()
lista.eliminar_inicio()
lista.eliminar_inicio()
lista.eliminar_inicio()
lista.eliminar_inicio()



lista.recorrer_inicio()


