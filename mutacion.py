import numpy as np


def mutacion_inversion(vatter: list, mutter: list):
    index_numbers = np.random.choice(range(0, len(vatter)), size=2, replace=False)
    range_index = [i for i in range(sorted(index_numbers)[0], sorted(index_numbers)[1], 1)]
    range_index_invers = sorted(range_index, reverse=True)
    range_init = [i for i in range(0, sorted(index_numbers)[0], 1)]
    range_end = [i for i in range(sorted(index_numbers)[1], len(mutter), 1)]
    range_init.extend(range_end)
    if 0 in index_numbers and 0 in range_init:
        range_index.remove(0)
    sohn_1 = [0 for i in range(0, len(vatter), 1)]
    sohn_2 = sohn_1.copy()
    for j in range_init:
        sohn_1[j] = mutter[j]
        sohn_2[j] = vatter[j]
    for (i, j) in zip(range_index, range_index_invers):
        sohn_1[i] = vatter[j]
        sohn_2[i] = mutter[j]
    return sohn_1, sohn_2


#Ejemplos
a1 = np.random.randint(0, 2, size=10).tolist()
a2 = np.random.randint(0, 2, size=10).tolist()
print(a1, "\n", a2)
print(mutacion_inversion(a1, a2))