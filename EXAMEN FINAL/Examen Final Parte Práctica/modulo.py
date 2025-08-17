def almacenar(x):
    lista=[]
    for i in range(0,x):
        y=int(input("Ingrese un número de la lista: "))
        lista.append(y)
    print(lista)
    print(" ")
    no_repetidos(lista)
    may_men(lista)

def no_repetidos(lista):
    lista4=list(set(lista))
    print("La lista sin elementos repetidos es: {}".format(lista4))
    return lista4

def may_men(lista4):
    lista2=sorted(lista4)
    lista3=sorted(lista4,reverse=True)
    print("La lista ordenada de menor a mayor es: {}".format(lista2))
    print(" ")
    print("La lista ordenada de mayor a menor es: {}".format(lista3))
    return lista2,lista3

def mayor_num_par(lista):
    lista_par=[]
    for i in lista:
        if i%2==0:
            lista_par_nueva=[]
            lista_par_nueva=lista_par.append(i)
        z=max(lista_par_nueva)
    print(z)

almacenar(5)
