import numpy as np


def mutation(vatter: list, mutter: list, interchange: bool):
    #np.random.seed(19209)
    if (type(vatter) != list) or (type(mutter) != list):
        return "type error"
    if len(vatter) != len(mutter):
        return "list do not have the same size!"
    else:
        if len(vatter) == 2:
            return "the list is not length enougth, the len of the list must be 3 or bigger"
        index_numbers = np.random.choice(range(0, len(vatter)), size=2, replace=False)
        if interchange == True:
            mc = mutter.copy()
            for i in index_numbers:
                mc[i] = vatter[i]
            return mc, index_numbers
        else:
            range_index = [i for i in range(sorted(index_numbers)[1], sorted(index_numbers)[0])]
            #Indices de los valores a modificar en el hijo
            range_list = [i for i in range(0, len(vatter), 1)]
            #Indices en total del jefe
            sohn_1 = [0 for i in range(0, len(vatter), 1)]
            sohn_2 = sohn_1.copy()
            for i in range_list:
                sohn_1[i] = mutter[i]
                sohn_2[i] = vatter[i]
            for j in range_index:
                sohn_1[j] = vatter[j]
                sohn_2[j] = mutter[j]
            return sohn_1, sohn_2, range_index


a1 = np.random.randint(0, 100, size=10).tolist()
a2 = np.random.randint(0, 2, size=10).tolist()
print(mutation(a1, a2, True))
