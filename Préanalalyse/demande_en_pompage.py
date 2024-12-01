def perte_de_charge(reynolds, longueur, diametre, densite, vitesse):
    f = 64/reynolds

    return f * longueur/diametre * densite * vitesse**2 * 1/2

def puissance_pompage(perte_charge, debit_massique, densite):
    return perte_charge * debit_massique/densite