import numpy as np

def del_tlm_saison(saison, t_in,t_out):
    delta_sortant = saison[0] - t_out
    delta_entrant = saison[0] - t_in
    
    return (delta_sortant - delta_entrant)/(np.log(delta_sortant/delta_entrant))

def calculer_pertes_saisons(r_tot, delta_tlm):
    return  1/r_tot * delta_tlm

def calculer_reynolds_saison(densite, saison, diametre, viscosite):
    return (densite * saison[1] * diametre)/viscosite