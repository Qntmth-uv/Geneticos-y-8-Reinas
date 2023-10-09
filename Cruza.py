import numpy as np
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

# padrino_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# madrina_1 = [9, 3, 7, 8, 2, 6, 5, 1, 4]

#print(cruza_ciclica(padrino_1,madrina_1))


def ciclic(lista_1: list, lista_2: list):
    setTouchedIndex = []
    while lista_1 != []:
        i = 0
        touchedIndex = []
        while i not in touchedIndex:
            index = i
            indexValueList1 = lista_1[index]
            indexValueList2 = lista_2[index]
            SearchedIndexInList1 = lista_1.index(indexValueList2)
            i = SearchedIndexInList1
            touchedIndex.append(index)
        for i in sorted(touchedIndex, reverse=True):
            lista_1.pop(i)
            lista_2.pop(i)
        setTouchedIndex.append(touchedIndex)
    return setTouchedIndex


#print(ciclic(padrino_1,madrina_1))