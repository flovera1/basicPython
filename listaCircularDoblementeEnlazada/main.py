'''
Lista circular doblemente enlazada

En una lista enlazada doblemente circular, cada nodo tiene dos enlaces,
similares a los de la lista doblemente enlazada, excepto que el enlace anterior
del primer nodo apunta al ultimo y el el enlace siguiente del utlimo nodo 
apunta al primero.
'''
from lista_circular_doblemente_enlazada import ListaCircularDobleEnlazada
from os import system
#system("clear")

lista = ListaCircularDobleEnlazada()


lista.agregar_final(12)
lista.agregar_final(45)
lista.agregar_final(18)
lista.agregar_final(36)
lista.agregar_final(10)
lista.eliminar_ultimo()
lista.eliminar_inicio()
lista.recorrer_inicio_a_fin()

#print("*"*25)

#lista.recorrer_fin_a_inicio()
#print(lista.primero.dato)
#print(lista.ultimo.dato)
#lista.eliminar_ultimo()

print(lista.buscar(12))
print(lista.buscar(122))




