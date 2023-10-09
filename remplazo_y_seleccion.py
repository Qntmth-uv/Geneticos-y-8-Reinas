from inicializacion import *
from mutacion import mutacion_uniparental
from Cruza import cruza_ciclica


def selectionParents(population: list):
    """Selección de padres.
    Toma una población, calcula su fitness individual, normaliza los fitness, luego usando el fitness normalizado
    hacemos probabilidad de un elemento de la población sea elegido, posteriomente se genera un numero aleatorio entre
    0 y 1, y se toman todos los elementos de la población que son mejores o iguales que ese valor. Pueden salir
    valores sumamente grandes, por ello hemos creado un while que garantiza que almenos dos elementos serán regresados
    (NO FUNCIONA XD)


    Input: population --- Lista de listas


    Output: choicenOnes --- lista de listas"""
    fitneSet = [fitness(i) for i in population]
    if 1 in fitneSet:
        return population[fitneSet.index(1)], 1, 0
    normFitset = [i - max(fitneSet) for i in fitneSet]
    probBeingChoice = [(i/sum(normFitset)) for i in normFitset]
    acumProbChoice = [sum(probBeingChoice[0:i+1]) for i in range(0, len(probBeingChoice), 1)]
    boundToBeChoice = float(np.random.uniform(0.01, 1, 1)[0])
    choicenOnes = [population[i] for i in range(0, len(population)) if boundToBeChoice <= acumProbChoice[i]]
    indexOfChoicesInPop = [population.index(choicenOnes[i]) for i in range(0, len(choicenOnes), 1)]
    # while len(choicenOnes) <= 1 and (boundToBeChoice <= 0.5):
    #     boundToBeChoice = float(np.random.uniform(0, 1, 1)[0])
    #     choicenOnes = [population[i] for i in range(0, len(population)) if boundToBeChoice <= probBeingChoice[i]]
    return choicenOnes, max(fitneSet), indexOfChoicesInPop

#TEST SHOT1
# shot1 = createPopulation(10)
# print(shot1)
# process = selectionParents(shot1)
# print(process[0])


def remplacement(population: list, choicenOnes: list, indexChoicenOnes: list):
    """Remplazamiento
    Toma la población actual y los elementos elegidos. Para luego encontrar los indices de estos elementos elegidos en
    la población actual, si el numero de listas en los choicenOnes es par, entonces se puede aplicar la cruza,
    de esta forma cruzamos todos los elmentos a pares, retornamos la población actualizada con las nuevas cruzas.
    De otra forma, si el numero de las listas en los choincenOnes es impar, entonces aplicamos una mutación a cada
    uno de ellos y los remplazamos en la población.


    Inputs: population --- Listas de listas (población actual)
            choicenOnes --- Lista de los elementos que serán transformados a través de alguna acción.


    Outputs: population --- Listas de listas (poblacion actualizada)
    """
    if choicenOnes == []:
        return population
    if (len(choicenOnes) % 2) == 0:
        for i in range(0, len(choicenOnes), 2):
            cruza = cruza_ciclica(choicenOnes[i], choicenOnes[i+1])
            population[indexChoicenOnes[i]] = cruza[0]
            population[indexChoicenOnes[i+1]] = cruza[1]
    else:
        muta = [mutacion_uniparental(choicenOnes[i]) for i in range(0, len(choicenOnes), 1)]
        for j, k in zip(indexChoicenOnes, range(0, len(choicenOnes), 1)):
            population[j] = muta[k]
    return population


#TEST SHOT1 (CONT)
#print(remplacement(shot1, process[0]))
