import numpy as np
import pandas as pd
from fonctions import *
from resistance_convection_interne import *
from resistance_conduction import *
from resistance_facteur_de_forme import *

# variables imposées
demande = 1*10**6 # demande des bâtiments en W

temp_entree_alimentation = 60 # température en ˚C de l'eau en entrée du tuyau
temp_retour = 45 # température en ˚C de l'eau en sortie du tuyau

vitesse_eau = 2 # vitesse moyenne de l'eau dans le tuyau
densite_eau = 1000 # densité de l'eau en kg/m^3
chaleur_specifique_eau = 4.18 * 10**3 # chaleur spécifique de l'eau qui est considéré comme constante pour la plage de temp. considérée
conductivite_eau = 650 * 10**-3 # conductivite de l'eau en W/m.k
conductivite_sol = 2.18

# paramètres du tuyau
diametre = 0.15 # diametre du tuyau d'alimentation
conductivite = 50 # conducivité du tuyau en acier au carbone, estimée à 50 w/m.K
longueur = 1500 # longueur du tuyau, fixée à 1.5 km
epaisseur_tuyau = 0.01 # épaisseur du tuyau en mètres
profondeur_tuyau = 1


# étape 1: évaluer la température en entrée des bâtiments
debit_massique = densite_eau * np.pi * 1/4 * diametre**2 * vitesse_eau
temp_sortie_alimentation = demande/(debit_massique * chaleur_specifique_eau) + temp_retour
temp_moyenne = (temp_entree_alimentation + temp_sortie_alimentation)/2 # évaluation des propriétés à cette température

# paramètres calculés en fonction de ceux imposés
prandtl = calculer_prandtl_eau(temp_moyenne)
viscosite_eau = calculer_viscosite_eau(temp_moyenne)
reynolds = calculer_reynolds(densite_eau, viscosite_eau, diametre, viscosite_eau)



# étape 2: évaluer la résistance totale du circuit thermique

R_conv_int = résistance_convection_interne(diametre, conductivite_eau, longueur)
R_cond = calculer_Rconduction_cylindre(diametre, epaisseur_tuyau, longueur, conductivite)
R_S = R_profond(longueur, profondeur_tuyau, diametre, conductivite_sol)

R_tot = R_conv_int + R_cond + R_S

print(R_tot)

# étape 3: évaluer les pertes de chaleur en puissance