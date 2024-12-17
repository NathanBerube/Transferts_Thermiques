import numpy as np

# Fonctions permettant les calculs liés à la puissance en pompage et à la perte de charge dans le tuyau d'alimentation
# les équations utilisées proviennent du recueil de formule du cours dans le Chapitre 7 - Convection interne

# NOTE: Tous les paramètres doivent être spécifiés dans le système d'unité international SAUF la température en ˚C (et non K)


def perte_de_charge(reynolds, longueur, diametre, densite, vitesse):
    # coefficient de friction f à l'intérieur de la conduite est donnée par l'équation suivante
    # elle est valide pour un écoulement turbulent, entièrement développé et 3000 <= Re_D <= 5 x 10^6 et une conduite lisse
    # ces conditions sont remplies pour les plages de valeurs considérées de l'écoulement dans le tuyau (p.28 recueil)
    f = (0.790 * np.log(reynolds) - 1.64)**(-2)

    # La perte de charge est donnée l'équation pour ∆P (p.28 recueil)
    perte_charge = f * (longueur/(2*diametre)) * densite * vitesse**2 

    return perte_charge

def puissance_pompage(perte_charge, debit_massique, densite):
    # L'équation suivante permet de calculer la puissance en pompage (p.28 recueil)
    puissance_pomp = perte_charge * debit_massique/densite
    return puissance_pomp