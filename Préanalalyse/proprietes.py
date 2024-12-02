import numpy as np

def load_data_meteo(path):
    pass

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
    temp_k = temp + 273
    if 300 < temp_k < 340:
        pente = (855 * 10**6 - 420 * 10**6)/(300 - 340)
        b = 577 * 10**6 - (pente * 320)

    elif 340 <= temp_k < 390:
        pente = (420 * 10**6 - 237 * 10**6)/(340 - 390)
        b = 289 * 10**6 - (pente * 370)
    
    else:
        raise Exception("temperature pas de l'intervalle acceptable")
    
    return pente*(temp_k) + b

def calculer_prandtl_air(temp):
    # interpolation linéaire du nombre de prandtl à partir de la table
    # pour la plage de température utilisée
    pente = (0.707 - 0.720)/(50)
    b = 0.720 - pente*250

    return pente*(temp+273) + b

def calculer_viscosite_air(temp):
    # interpolation linéaire du nombre de la viscosité dynamique de l'eau à partir de la table
    # pour la plage de température utilisée
    pente = (18.46 * 10**-6 - 15.96 * 10**-6)/(50)
    b = 15.96 * 10**-6 - pente*250

    return pente*(temp+273) + b
