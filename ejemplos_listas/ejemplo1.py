
lista= [10,20,30,40]
# append
# insert
lista.insert(2, [10,20,30])
print(lista)
print(len(lista))

lista1= [1,2,3,4,5,6,7,8]
lista2= [5,6,7,8]
lista3 = lista1 + lista2
lista1.extend(lista2)
print(lista3)
print(lista1)