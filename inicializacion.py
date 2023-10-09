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


def diagAttack(entity: list):
    """Calcula los ataques de una matriz de posiciones de reinas, para que una reina
    pueda atacar a la otra se necesita que esten en la misma diagonal, esto es que si formamos
    un cuadrado con las reinas como vertices, entonces la otra reina debe de estar necesarimente
    en el otro otro vertice del cuadrado, es decir, que las distancias entre los las proyecciones
    de las reinas concidad. Se empieza de atras para adelante y así no se repiten ataques

    Input: Entity --- Una lista

    Output: Flag --- Entero positivo que cuenta los ataques de la lista dada
    """
    flag: int = 0
    for i in range(0, len(entity), 1):
        for j in range(i+1, len(entity), 1):
            if abs(entity[i]-entity[j]) == abs(i-j):
                flag += 1
    return flag


def fitness(entity: list) -> float:
    """Calcula el fitness de una lista dada, usando como parametro la cota superior
    de ataques del tablero, cuando el tablero no tenga ningun ataque nos dara un fitness
    de 1, mientras cuando sea el peor de los casos nos dará un fitness de 0. Además, este fitness
    sirve como medida probabilistica por estar entre 0 y 1.

    Input: entity --- list

    Output: fit --- float"""
    fit = 1-diagAttack(entity)/28
    return fit

# acc = 0
# while acc != 1:
#     test1 = initTab()
#     acc = fitness(test1)
#     print(acc)
#     if acc == 1:
#         print(test1)



