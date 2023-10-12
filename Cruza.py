from inicializacion import initTab

def cruza_ciclica(vatter: list, mutter: list):
    # if len(vatter) != len(mutter):
    #     return "the list do not have the same size"
    # index_init_v = [i for i in range(0, len(vatter), 1)]
    # index_init_m = index_init_v.copy()
    # valor_asociado_p = []
    # valor_asociado_m = []
    # indices_tocados = []
    # i = 0
    # while i in indices_tocados:
    #     asociado_p = vatter[i]
    #     asociado_m = mutter[i]
    #     valor_asociado_p.append(asociado_p)
    #     valor_asociado_m.append(asociado_m)
    #     index_asociado = vatter.index(asociado_m)
    #     indices_tocados.append(i)
    #     i = index_asociado
    return initTab(), initTab()

padrino_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
madrina_1 = [8, 2, 6, 7, 1, 5, 4, 0, 3]

#print(cruza_ciclica(padrino_1,madrina_1))


# def ciclic(lista_1: list, lista_2: list):
#     setTouchedIndex = []
#     while lista_1 != []:
#         i = 0
#         touchedIndex = []
#         while i not in touchedIndex:
#             index = i
#             indexValueList1 = lista_1[index]
#             indexValueList2 = lista_2[index]
#             SearchedIndexInList1 = lista_1.index(indexValueList2)
#             i = SearchedIndexInList1
#             touchedIndex.append(index)
#         for i in sorted(touchedIndex, reverse=True):
#             lista_1.pop(i)
#             lista_2.pop(i)
#         setTouchedIndex.append(touchedIndex)
#     return setTouchedIndex


#print(ciclic(padrino_1,madrina_1))


def cyclicV3(entity1: list, entity2: list):
    if len(entity1) != len(entity2):
        return "sizes do not match!"
    notouchedIndex = [i for i in range(0, len(entity1), 1)]
    setOfToucedIndex = []
    i = 0
    while len(notouchedIndex) != 0:
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
    setofIndex = cyclicV3(entity1, entity2)
    genEntity1 = [setofIndex[i] for i in range(0,len(setofIndex), 1) if (i % 2 == 0)]
    genEntity2 = [setofIndex[i] for i in range(0, len(setofIndex), 1) if (i % 2 == 1)]
    genEntity1List = []
    genEntity2List = []
    for i in genEntity1:
        genEntity1List.extend(i)
    for i in genEntity2:
        genEntity2List.extend(i)
    return genEntity1List, genEntity2List


print(sexCyclic(padrino_1, madrina_1))
#print(cyclicV3(initTab(), initTab()))
