from inicializacion import initTab


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
    son = [0 for i in range(0, len(entity1), 1)]
    for k in genEntity1List:
        son[k] = entity1[k]
    for j in genEntity2List:
        son[j] = entity2[j]
    return son


def biSonSex(entity1: list, entity2: list):
    son1 = sexCyclic(entity1, entity2)
    son2 = sexCyclic(entity2, entity1)
    return son1, son2


#TESTING
#padrino_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
#madrina_1 = [8, 2, 6, 7, 1, 5, 4, 0, 3]
#print(cyclicV3(initTab(), initTab()))
#print(sexCyclic(padrino_1, madrina_1))
#print(biSonSex(initTab(), initTab()))

