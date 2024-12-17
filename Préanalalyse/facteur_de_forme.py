import numpy as np

# Les deux équations suivantes permettent de calculer le facteur de forme en conduction
# pour un tuyau de longueur L et de diamètre D enfoui dans le sol à une profondeur de z
# celles-ci sont valides pour L >> z, ce qui est toujours le cas pour le contexte

# NOTE: Tous les paramètres doivent être spécifiés dans le système d'unité international SAUF la température en ˚C (et non K)

def S_pas_profond(L, z, D):
    # facteur de forme pour toute profondeur
    return 2 * np.pi * L / np.arccosh(2 * z / D)

def S_profond(L, z, D):
    # facteur de forme pour une profondeur z > 3D/2
    # cette équation sera toujours utilisée pour les calculs, car la condition sera toujours remplie pour les 
    # profondeurs de tuyau envisagées
    return 2 * np.pi * L / np.log(4 * z / D)
