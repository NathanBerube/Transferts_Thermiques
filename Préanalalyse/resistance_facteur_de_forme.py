import numpy as np
from facteur_de_forme import *

def R_pas_profond(L, z, D, k):
    S = S_pas_profond(L, z, D)

    return 1/(S * k)

def R_profond(L, z, D, k):
    S = S_profond(L, z, D)

    return 1/(S * k)
