import numpy as np

def churchill_bernstein(reynolds, prandtl):
    premier_terme = (0.62 * reynolds**(1/2) * prandtl**(1/3))/(1 + (0.4/prandtl)**(2/3))**(1/4)
    deuxieme_terme = (1 + (reynolds/282000)**(5/8))**(4/5)

    return 0.3 + premier_terme*deuxieme_terme

def calculer_reynolds(densite, vitesse, diametre, viscosite):
    return (densite * vitesse * diametre)/viscosite

def calculer_prandtl_eau(temp):
    # interpolation linéaire du nombre de prandtl à partir de la table
    # pour la plage de température utilisée
    pente = (5.83 - 1.87)/(300 - 390)
    b = 2.66 - (pente * 340)

    return pente*(temp + 273) + b

def calculer_viscosite_eau(temp):
    # interpolation linéaire du nombre de la viscosité dynamique de l'eau à partir de la table
    # pour la plage de température utilisée
    temp = temp + 273
    if 300 < temp < 340:
        pente = (855 * 10**6 - 420 * 10**6)/(300 - 340)
        b = 577 * 10**6 - (pente * 320)

    elif 340 <= temp < 390:
        pente = (420 * 10**6 - 237 * 10**6)/(340 - 390)
        b = 289 * 10**6 - (pente * 370)
    
    else:
        raise Exception("temperature pas de l'intervalle acceptable")
    
    return pente*(temp) + b

def résistance_convection_externe(rho, V, D, k, L, T):
    viscosite = calculer_viscosite_eau(T)
    reynolds = calculer_reynolds(rho, V, D, viscosite)
    prandtl = calculer_prandtl_eau(T)
    Nu = churchill_bernstein(reynolds, prandtl)
    h = Nu * k / L
    A = L * np.pi * D / 4

    return 1/(h*A)