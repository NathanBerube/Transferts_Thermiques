import numpy as np
def calculer_Rconduction_cylindre(D_int, epaisseur, L_tuyau, C_thermique):
    Ratio = (D_int + (2*epaisseur))/D_int

    R = np.log(Ratio)/(2*np.pi*L_tuyau*C_thermique)
    
    return(R)