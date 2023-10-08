import numpy as np
from mutacion import mutacion_uniparental


def initTab() -> list:
    """Creation of a random permutation of the list [0:8]


    input: empty


    output: tab --- A list of random permutation of the list [0:8]"""
    tab = np.random.choice(range(0, 8, 1), size=8, replace=False).tolist()
    return tab


def createPopulation(size: int):
    """Creation of the initial population of the problem of 8 queens.


    Inputs: size --- size of the population, it must be a positive integer number


    Outputs: population --- A list of list that contains random permutations of the list [0:8]
    """
    if type(size) != int:
        return "size must be a integer number"
    if size < 0:
        return "size must be a positive integer number"
    else:
        population = [initTab() for i in range(0, size, 1)]
        return population


initialPop = createPopulation(5)
print(initialPop)
mutedlist = [mutacion_uniparental(initialPop[i]) for i in range(0, len(initialPop),1 )]
print(mutedlist)

