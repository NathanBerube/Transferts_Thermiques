import numpy as np
from fonctions import *

def résistance_convection_externe(rho, V, D, k, L, T):
    viscosite = calculer_viscosite_eau(T)
    reynolds = calculer_reynolds(rho, V, D, viscosite)
    prandtl = calculer_prandtl_eau(T)
    Nu = churchill_bernstein(reynolds, prandtl)
    h = Nu * k / L
    A = L * np.pi * D / 4

    return 1/(h*A)