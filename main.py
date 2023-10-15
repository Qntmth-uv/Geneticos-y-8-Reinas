from remplazo_y_seleccion import *
from matplotlib import pyplot as plt

def eigthQueenProblemV2(populationSize: int, iter: int, selecctionNumber: int, remplaceSeleccion: bool):
    """Algoritmo solución al problema de las ocho reinas
    Se inicia con una población inicial, y un numero de iteraciones dadas por el usuario. Posteriormente se realizaran
     el numero de iteraciones el remplazo de la población, se gruarda su fitness maximo para un grafico y
     así sucesivamente, si encuentra un tablero perfecto entonces corta el cilo. Finalmente se calculan los fitness
     de la ultima población y se devuelven los mejores fitness en cada iteracion, la poblacion original, la
     poblacion final, y el mejor tablero de la poblacion final

     :parameter populationSize --- Tamaño de la población a generar
     :parameter iter --- Numero de iteraciones a realizar en la población
     :parameter selecctionNumber --- Numero de individuos que se seleccionaran en el torneo (mayor que cero y menor que el
     tamaño de la población)
     :parameter remplaceSeleccion --- Da la opción de pedir que en torneo no se repitan individuos.

     :returns MaxFitPerIter --- Fitness maximo en cada iteración
     :returns ancientPop --- Población orignal
     :returns newPop --- Poblacion final
     :returns bestBoard --- Mejor tablero de la población final"""
    maxFitPerIter =[]
    newPop= []
    setMediansPerIter = []
    popIni = createPopulation(populationSize)
    ancientPop = popIni
    for i in range(0, iter, 1):
        selected = selectionParentsRuleta(popIni, selecctionNumber, remplaceSeleccion)
        newPop = remplacementV2(popIni, selected[1])
        popIni = newPop
        maxFitPerIter.append(selected[2])
        setMediansPerIter.append(selected[4])
        if 1 in maxFitPerIter:
            break
    fitneSet = [fitness(i) for i in popIni]
    maxmimumEndFitness = max(fitneSet)
    bestBoard = popIni[fitneSet.index(maxmimumEndFitness)]
    return maxFitPerIter, ancientPop, newPop, bestBoard, setMediansPerIter


#TESTEO
testing1 = eigthQueenProblemV2(30,50,7,False)
# print(testing1[0])
# print(testing1[3])
# print(testing1[4])

#SOLUTIONS FINDED
#print(fitness([1, 6, 2, 5, 7, 4, 0, 3]))
#print(fitness([4, 2, 0, 5, 7, 1, 3, 6]))
#print(fitness([2, 0, 6, 4, 7, 1, 3, 5]))


#GRAFICA
# x_axis = np.arange(len(testing1[0]), dtype=int)
#
# plt.plot(x_axis, testing1[0], marker = 'o', label="Máximo")
# plt.plot(x_axis, testing1[4], 'o', label="Media")
#
# plt.title("Fitness por iteración")
# plt.xlabel("Iteración n.")
# plt.ylabel("Fitness")
# minimutboud = min(testing1[4])
# plt.ylim(bottom = minimutboud-0.05, top= 1)
# plt.grid(color = 'grey', linestyle = '--', linewidth = 1, alpha=0.45)
# plt.legend(loc = "lower right", title = "Variables")
# plt.show()

