from inicializacion import *
from mutacion import mutacion_uniparental
from Cruza import biSonSex


#TEST SHOT1
#shot1 = createPopulation(10)
# print(shot1)
# process = selectionParents(shot1)
# print(process[0])


def selectionParentsRuleta(population: list, pick: int, remplace: bool):
    """Seleccion de Padres por ruleta de aptitud
    Selecciona los un numero especifico de listas en la población a traves de un sorteo aleatorio.

    :parameter population --- Lista de listas
    :parameter pick --- entero positivo
    :parameter remplace --- No repetición de las listas en el torneo (bool)

    :return ChoicenOnes --- Lista de las listas que fueron seleccionadas en el sorteo
    :return IndexChoicen --- Lista de indeces de las listas que fueron seleccionadas en el sorteo con respecto
    a la lista de la población en general
    :return max(fitneSet) --- valor flotante con el maximo fitness de algun elemento de la poblacion
    """
    if pick <= 0 or pick >= len(population):
        return population
    fitneSet = [fitness(i) for i in population]
    normFitset = [i - max(fitneSet) for i in fitneSet]
    probBeingChoice = [i / (sum(normFitset)) for i in normFitset]
    '#EXISTE UN PEQUEÑO BUG CUANDO LA POBLACIÓN ES BAJA, YA QUE PUEDE SUCEDER QUE TODOS TENGAN EL MISMO FITNESS,'
    'LUEGO EN probBeingChoice SE DIVIDIRÁ SOBRE DANDO UN ERROR DE DIVISIÓN SOBRE 0'
    acumProbChoice = [sum(probBeingChoice[0:i+1]) for i in range(0, len(probBeingChoice), 1)]
    indexChoicen = []
    while len(indexChoicen) < pick:
        boundToBeChoice = float(np.random.uniform(0, 1, size=1)[0])
        k: int = 0
        while acumProbChoice[k] <= boundToBeChoice:
            k += 1
        if remplace is False:
            if k in indexChoicen:
                k = 0
            else:
                indexChoicen.append(k)
        else:
            indexChoicen.append(k)
    ChoicenOnes = [population[j] for j in indexChoicen]
    '# POR NATURALIZA ESTADISTICA PUEDE EXISTIR UN CASO DONDE LOS ELEMENTOS EN ELEGIDOS SE REPITAN, ESO NO ES DESABLE'
    'POR TANTO SE IMPLEMENTO UN PARAMETRO QUE PERMITE PEDIR QUE LOS ELEMENTOS NO SE REPITAN EN ChoicenOnes'
    return ChoicenOnes, indexChoicen, max(fitneSet), fitneSet.index(max(fitneSet))


def remplacementV2(popuation: list, indexChoicenOnes: list):
    """Intercambia de manera generacional a los padres con los hijos en la población
    Ingresa los valores de la población actual junto con los indices de los elegidos en la ruleta sexual
    posteriormente si el numero de elegidos es impar se quita uno y posteriormente se cruzan esos elementos
    selccionados a pares, si no es impar todos se cruzan. Una vez que todos se han cruzado, mutamos a todos esos
    nuevos hijos y también  los reemplazamos en la población. Regresando como valor una lista de lista distinta a la
    ingresada originalmente.

    :argument popuation --- Población actual
    :argument indexChoicenOnes --- Indices de los elementos seleccionados en el torneo con respecto a la población actual

    :return modiPop --- Población modifica despues de haber sido cruzada y mutada (unicamente los elementos que fueron
    seleccionados)"""
    modifPop = popuation.copy()
    if (len(indexChoicenOnes) % 2) == 1:
        for i in range(0, len(indexChoicenOnes)-1, 2):
            desendencia = biSonSex(popuation[indexChoicenOnes[i]], popuation[indexChoicenOnes[i+1]])
            modifPop[indexChoicenOnes[i]] = desendencia[0]
            modifPop[indexChoicenOnes[i+1]] = desendencia[1]
    else:
        for i in range(0, len(indexChoicenOnes), 2):
            desendencia = biSonSex(popuation[indexChoicenOnes[i]], popuation[indexChoicenOnes[i+1]])
            modifPop[indexChoicenOnes[i]] = desendencia[0]
            modifPop[indexChoicenOnes[i+1]] = desendencia[1]
    muta = [mutacion_uniparental(modifPop[i]) for i in indexChoicenOnes]
    for j, k in zip(indexChoicenOnes, range(0, len(indexChoicenOnes), 1)):
        modifPop[j] = muta[k]
    return modifPop


#TEST SHOT1 (CONT)
# process = selectionParentsRuleta(shot1, 5, remplace=False)
# print(process[1])
# print(remplacementV2(shot1, process[1]))
# print(shot1)
