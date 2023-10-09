from remplazo_y_seleccion import *


def eigthQueensProblem(populationSize: int, iter: int):
    maxFitPerIter = []
    pop_init = createPopulation(populationSize)
    for i in range(0, iter, 1):
        sel = selectionParents(pop_init)
        if sel[1] == 0:
            print(sel[0])
        else:
            maxFitPerIter.append(sel[1])
            new_pop = remplacement(pop_init, sel[0], sel[2])
            pop_init = new_pop
    return maxFitPerIter

print(eigthQueensProblem(10, 30))

