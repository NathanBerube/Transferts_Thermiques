import numpy as np

def résistance_convection_interne(D, k):
    h = 3.66 * k / D
    A = 1500 * np.pi * D / 4

    return 1/(h * A)

print(résistance_convection_interne(0.2, 569*10**-3))