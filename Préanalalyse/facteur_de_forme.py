import numpy as np

def S_pas_profond(L, z, D):
    return 2 * np.pi * L / np.arccosh(2 * z / D)

def S_profond(L, z, D):
    return 2 * np.pi * L / np.log(4 * z / D)
