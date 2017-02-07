'''
Arbol binario es una estructura 
de datos en la cual cada nodo puede
tener un hijo izquierdo y un hijo 
derecho, no pueden tener mas de dos hijos.
reglas:
-siempre hay una raiz
-todos los datos menores van a la izq
 todos los datos mayores van a la der
Recorrer: preorden, postorden
'''
from binarySearchTree import BinarySearchTree

tree = BinarySearchTree()

tree.add(8)
tree.add(10)
tree.add(3)
tree.add(14)
tree.add(13)
tree.add(1)
tree.add(6)
tree.add(4)
tree.add(7)
'''
tree.show_in_order(tree.root)
print("*"*5)
tree.show_pos_order(tree.root)
print("*"*5)
tree.show_pre_order(tree.root)
'''

print(tree.search(tree.root, 8).value)


"""

En orden
izquierda-raiz-derecho
1,3,4,5,7,8,10,13,14

En Pos orden
izquierda-derecha-raiz
1,4,7,6,3,13,14,10,8

En Pre orden
raiz-izquierda-derecha
8,3,1,6,4,7,10,14,13

 """

