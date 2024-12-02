import numpy as np

def résistance_convection_interne(D, k, L):
    h = 3.66 * k / D
    A = L * np.pi * D

    return 1/(h * A)
