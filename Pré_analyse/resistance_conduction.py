import numpy as np

# Ce fichier permet d'implémenter l'équation de la résistance du conduction dans un cylindre (recueil p. 6). Cette
# équation est utile pour la résistance de conduction dans le tuyau et dans l'isolant selon le diamètre
# intérieur D_int, l'épaisseur, la longueur du tuyau L_tuyau et la conductivité thermique k du matériau.

# NOTE: Tous les paramètres doivent être spécifiés dans le système d'unité international SAUF la température en ˚C (et non K)

def calculer_Rconduction_cylindre(D_int, epaisseur, L_tuyau, k):
    Ratio = (D_int + (2*epaisseur))/D_int

    R = np.log(Ratio)/(2*np.pi*L_tuyau*k)
    
    return(R)