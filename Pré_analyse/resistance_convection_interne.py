import numpy as np

# Ce fichier permet de calculer tout ce qui est en lien avec la convection interne dans le tuyau

# NOTE: Tous les paramètres doivent être spécifiés dans le système d'unité international SAUF la température en ˚C (et non K)

def correlation_nusselt_interne(Re, Pr):
    # Corrélation du recueil (p.32) pour le calcul du nombre de Nusselt pour un écoulement turbulent,
    # entièrement développé, 0.6<Pr<160, Re_D > 10000, L/D>10. La puissance vient du fait que la surface du tuyau
    # est plus chaude que la température moyenne du fluide

    return 0.023 * Re**(4/5) * (Pr)**0.3

def résistance_convection_interne(D, k, L, Re, Pr):
    # Le nombre de Nusselt (3.66) pour un écoulement interne dans un tuyau a été approximé comme constant 
    # selon les équations du recueil (p.32). Le coefficient de convection et la résistance
    Nu = correlation_nusselt_interne(Re, Pr)
    h = Nu * k / D
    A = L * np.pi * D

    return 1/(h * A)
