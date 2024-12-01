import math
def calculer_Rconduction_cylindre(D_int, epaisseur, L_tuyau, C_thermique):
    Ratio = (D_int + epaisseur)/D_int

    R = math.log(Ratio)/(2*math.pi*L_tuyau*C_thermique)
    
    return(R)