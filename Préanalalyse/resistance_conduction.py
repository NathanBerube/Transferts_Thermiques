import math
def calculer_Rconduction_cylindre(diametre_ext, diametre_int, longueur_tuyau, conductivité_thermique ):
    R = (math.log(diametre_ext-diametre_int))/(2*math.pi*longueur_tuyau*conductivité_thermique)
    return(R)