import numpy as np
from queue import PriorityQueue

def fitness(individuo):
    return "valor_de_ataques_sobre_8"

##ESTE EJEMPLO MUESTRA QUE LOS DICCIONARIOS NO SE GENERAN DE MANERA DISTINTA
diccionario = {"board" : np.random.randint(0, 2, size=(8, 8)), "fitness_d" : 0}
diccionario["fitness_d"] = fitness(diccionario["board"])
diccionario_de_diccionarios = [diccionario for i in range(0,10,1)]
print(diccionario_de_diccionarios)
diccionario["board"] = "hola mundo"
print(diccionario_de_diccionarios)

# class board:
#     def __init__(self):
#         self.queenBoard = np.random.randint(0,2, size=(8,8))
#
#     def getFit(self):
#         Bfit = fitness(self.queenBoard)
#         return Bfit
#
#     def getBoard(self):
#         return self.queenBoard


# q = PriorityQueue()
# poblacion = [board() for i in range(0,10,1)]
# for i in range(0,10,1):
#     q.put(poblacion[i].queenBoard, board)




def ruleta_aptitud(poblacion: list):
    return 0