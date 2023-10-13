#from inicializacion import initTab


def cyclicV3(entity1: list, entity2: list):
    """Genera conjuntos de indices de un par de lista de una manera deseada
    Dados dos listas, se calcula su longitud, además por construcción ambas listas deben de
    contener los mismos valores, en distintos ordenes. Posteriormente se genera un conjunto de entradas
    que no han sido tocadas por el algoritmo. Luego se genera una lista de listas llamada setOfTouchedIndex
    que nos dice cuales indices fueron tocados por el algoritmo. Luego, mientras la lista de indices no este
    vacia significara que no ha acabado el algortimo principal, y caad vez que corramos el algoritmo generamos
    un conjunto de indices que nos dira cuales fueron tocados por el algoritmo. Empezamos el algoritmo con el
    primer elemento del conjunto de indices, busca es valor asociado a ese indice en la segunda lista, posteriormente,
    se consigue el indice en la primera lista que contiene ese valor, se guarda ese valor en los indices tocados,
    mientras que se elimina del conjunto de indices disponibles. Cambiamos el indice sobre el cual se volverá a repertir
    el algoritmo. Así hasta que el indice asignado no este en el conjunto de indices. Así acaba una iteración de
    algoritmo. Posteriormente guardamos el conjunto de indices y repetimos. Una vez acabo el proceso regresa el conjunto
    de indices tocados en cada iteración.


    :argument entity1 --- Lista (permutacion), entity2 --- Lista (permutación)

    :return setsOfTouchedIndex --- Lista de listas con los indices tocados por el algoritmo ciclico.
    """
    notouchedIndex = [i for i in range(0, len(entity1), 1)]
    setOfToucedIndex = []
    i = 0
    while notouchedIndex != []:
        touchedIndex = []
        i = notouchedIndex[0]
        while i in notouchedIndex:
            associatedValueInEntt2 = entity2[i]
            indexAsocciatedEntt1 = entity1.index(associatedValueInEntt2)
            touchedIndex.append(i)
            notouchedIndex.remove(i)
            i = indexAsocciatedEntt1
        setOfToucedIndex.append(touchedIndex)
    return setOfToucedIndex


def sexCyclic(entity1: list, entity2: list):
    """Genera un hijo apartir de CyclicV3
    Obtenemos los valores de los indices tocados por la función CyclicV3, haciendo pares
    se obtienen listas de indices que corresponden a la lista padre y a la lista madre. Luego
    se crea un hijo que tendrá los elementos que esten en la lista de genes de los progenitores, asignando
    en dicho indice dicho valor.


    :argument entity1 --- Lista (permutacion), entity2 --- Lista (permutación)

    :return son --- Lista (permutación)
    """

    setofIndex = cyclicV3(entity1, entity2)
    genEntity1 = [setofIndex[i] for i in range(0, len(setofIndex), 1) if (i % 2 == 0)]
    genEntity2 = [setofIndex[i] for i in range(0, len(setofIndex), 1) if (i % 2 == 1)]
    genEntity1List = []
    genEntity2List = []
    for i in genEntity1:
        genEntity1List.extend(i)
    for i in genEntity2:
        genEntity2List.extend(i)
    son = [0 for i in range(0, len(entity1), 1)]
    for k in genEntity1List:
        son[k] = entity1[k]
    for j in genEntity2List:
        son[j] = entity2[j]
    return son


def biSonSex(entity1: list, entity2: list):
    """Genera dos hijos a partir de dos listas usando sexCyclic
    Usa la función sexCyclic solo que alternando las listas para generar dos listas en general diferentes.

    :argument entity1 --- Lista (permutacion), entity2 --- Lista (permutación)

    :returns son1 --- Lista (permutación), son2 ---  Lista (permutación)
    """
    son1 = sexCyclic(entity1, entity2)
    son2 = sexCyclic(entity2, entity1)
    return son1, son2


#TESTING
#padrino_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
#madrina_1 = [8, 2, 6, 7, 1, 5, 4, 0, 3]
#print(cyclicV3(initTab(), initTab()))
#print(sexCyclic(padrino_1, madrina_1))
#print(biSonSex(initTab(), initTab()))

