import numpy as np

# ce fichier contient les équations nécessaires au calcul des pertes de chaleur dans le tuyau d'alimentation
# l'utilisation de l'équation q_pertes = UA ∆T_lm est faite pour le cas d'une différence de température entre T_infini,
# T_sortante et T_entrante. Le facteur UA = 1/R_tot du circuit thermique qui est formée de 4 résistances pour les deux cas
# considérée.
#
# Pour le cas dans le sol: la résistance totale est la somme de la résistance de convection interne, la résistance de conduction
#    dans le tuyau, la résistance de conduction dans l'isolant (s'il y a lieu) et la résistance de conduction dans la sol (facteur de forme)
#    La température à la surface du sol est approximée comme la température de l'air T_infini
#
# Pour le cas hors-sol: la résistance totale est la somme de la résistance de convection interne, la résistance de conduction
#    dans le tuyau, la résistance de conduction dans l'isolant (s'il y a lieu) et la résistance de convection externe


# NOTE: Tous les paramètres doivent être spécifiés dans le système d'unité international SAUF la température en ˚C (et non K)


def del_tlm(t_inf, t_in,t_out):
    # équation du calcul du ∆T_lm entre la température en entrée et sortie du tuyau d'alimentation
    # l'équarion disônible à la p.31 du recueil est utilisée
    delta_sortant = t_inf - t_out
    delta_entrant = t_inf - t_in
    
    return (delta_sortant - delta_entrant)/(np.log(delta_sortant/delta_entrant))


def calculer_pertes(r_tot, delta_tlm):
    # équation qui permet de calculer les pertes correspondant au flux de chaleur dans le circuit thermique
    # l'équation suivante provient de la p.31 du recueil de formules
    return  1/r_tot * delta_tlm