import numpy as np


def cruza_ciclica(vatter: list, mutter: list):
    index_init_v = [i for i in range(0, len(vatter), 1)]
    index_init_m = index_init_v.copy()
    valor_asociado_p = []
    valor_asociado_m = []
    i = 0
    while i in index_init_v:
        asociado_p = vatter[i]
        asociado_m = mutter[i]
        valor_asociado_p.append(asociado_p)
        valor_asociado_m.append(asociado_m)
        index_asociado = vatter.index(asociado_m)
        vatter.remove(asociado_p)
        mutter.remove(asociado_m)
        index_init_v.remove(i)
        i = index_asociado
    return valor_asociado_p

padrino_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
madrina_1 = [9, 3, 7, 8, 2, 6, 5, 1, 4]

print(cruza_ciclica(padrino_1,madrina_1))