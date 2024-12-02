import numpy as np

def perte_de_charge(reynolds, longueur, diametre, densite, vitesse):
    f = (0.790 * np.log(reynolds) - 1.64)**(-2)

    return f * (longueur/(2*diametre)) * densite * vitesse**2 

def puissance_pompage(perte_charge, debit_massique, densite):
    return perte_charge * debit_massique/densite