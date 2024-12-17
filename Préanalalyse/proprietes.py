import numpy as np

# Ce fichier permet de calculer toutes les propriétés des écoulements qui dépendent de d'autres paramètres
# comme la température, la vitesse ou de la géométrie.

# NOTE: Tous les paramètres doivent être spécifiés dans le système d'unité international SAUF la température en ˚C (et non K)


def calculer_reynolds(densite, vitesse, diametre, viscosite):
    # Équation qui permet de calculer le nombre de reynolds pour un diamètre en fonction
    # des paramètres d'un écoulement selon la définition (p.24 du recueil)
    return (densite * vitesse * diametre)/viscosite


def calculer_prandtl_air(temp):
    #nterpolation linéaire du nombre de la viscosité dynamique de l'eau à partir de la table B.1 du recueil
    # pour la plage de température utilisée
    pente = (0.707 - 0.720)/(50)
    b = 0.720 - pente*250

    return pente*(temp+273) + b

def calculer_viscosite_air(temp):
    # interpolation linéaire du nombre de la viscosité dynamique de l'eau à partir de la table B.1
    # pour la plage de température utilisée
    pente = (18.46 * 10**-6 - 15.96 * 10**-6)/(50)
    b = 15.96 * 10**-6 - pente*250

    return pente*(temp+273) + b
