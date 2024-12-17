import numpy as np
from facteur_de_forme import *

# Ce fichier permet de calculer la résistance de conduction dun sol selon le facteur de forme de sol en appelant
# les fonctions du fichier facteur_de_forme.py. Les deux équations suivantes permettent de calculer le facteur de forme en conduction
# pour un tuyau de longueur L et de diamètre D enfoui dans le sol à une profondeur de z
# celles-ci sont valides pour L >> z, ce qui est toujours le cas pour le contexte. On peut alors calculer 
# la résistance à l'aide de la conductivité thermique du sol.

# NOTE: Tous les paramètres doivent être spécifiés dans le système d'unité international SAUF la température en ˚C (et non K)


def R_pas_profond(L, z, D, k):
    S = S_pas_profond(L, z, D)

    return 1/(S * k)

def R_profond(L, z, D, k):
    S = S_profond(L, z, D)

    return 1/(S * k)
