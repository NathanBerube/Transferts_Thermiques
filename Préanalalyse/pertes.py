import numpy as np

def delta_tlm(t_inf, t_in,t_out):
    delta_sortant = t_inf - t_out
    delta_entrant = t_inf - t_in
    
    return (delta_sortant - delta_entrant)/(np.log(delta_sortant/delta_entrant))


def calculer_pertes(r_tot, delta_tlm):
    return  1/r_tot * delta_tlm