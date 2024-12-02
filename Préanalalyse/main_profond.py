import numpy as np
import pandas as pd
from proprietes import *
from resistance_convection_interne import *
from resistance_conduction import *
from resistance_facteur_de_forme import *
from pertes import *
from demande_en_pompage import *

# variables imposées
demande = 1*10**6 # demande des bâtiments en W

temp_entree_alimentation = 60 # température en ˚C de l'eau en entrée du tuyau
temp_retour = 45 # température en ˚C de l'eau en sortie du tuyau
T_air = 0

# paramètres du tuyau
D = 0.15 # diametre du tuyau d'alimentation
conductivite = 50 # conducivité du tuyau en acier au carbone, estimée à 50 w/m.K
longueur = 1500 # longueur du tuyau, fixée à 1.5 km
epaisseur_tuyau = 0.01 # épaisseur du tuyau en mètres
profondeur_tuyau = 1

#paramètre de l'eau
vitesse_eau = 2 # vitesse moyenne de l'eau dans le tuyau
densite_eau = 1000 # densité de l'eau en kg/m^3
chaleur_specifique_eau = 4.18 * 10**3 # chaleur spécifique de l'eau qui est considéré comme constante pour la plage de temp. considérée
conductivite_eau = 650 * 10**-3 # conductivite de l'eau en W/m.k
conductivite_sol = 2.18
mu_eau = 4.67 * 10**-4
Re_eau = calculer_reynolds(densite_eau, vitesse_eau, D, mu_eau)

# paramètres de l'isolsant
D_iso = D+(2*epaisseur_tuyau)
t_iso = 0.1
L_iso = longueur
k_iso = 0.035 #conductuvité thermique de l'isolant - 0.035 = laine de verre ou laine de roche

# étape 1: évaluer la température en entrée des bâtiments
debit_massique = densite_eau * np.pi * 1/4 * D**2 * vitesse_eau
temp_sortie_alimentation = demande/(debit_massique * chaleur_specifique_eau) + temp_retour
temp_moyenne = (temp_entree_alimentation + temp_sortie_alimentation)/2 # évaluation des propriétés à cette température

# paramètres calculés en fonction de ceux imposés
prandtl = calculer_prandtl_eau(temp_moyenne)
viscosite_eau = calculer_viscosite_eau(temp_moyenne)
reynolds = calculer_reynolds(densite_eau, viscosite_eau, D, viscosite_eau)

# étape 2: évaluer la résistance totale du circuit thermique

R_conv_int = résistance_convection_interne(D, conductivite_eau, longueur)
R_cond = calculer_Rconduction_cylindre(D, epaisseur_tuyau, longueur, conductivite)
R_cond_iso = calculer_Rconduction_cylindre(D_iso, t_iso, longueur, k_iso)
R_S = R_profond(longueur, profondeur_tuyau, D, conductivite_sol)

R_tot = R_conv_int + R_cond + R_S + R_cond_iso
print(f"La résistance totale est {R_tot:.5f}")

# étape 3: évaluer les pertes de chaleur en puissance

delta_tlm = delta_tlm(T_air, temp_entree_alimentation, temp_retour)
pertes = calculer_pertes(R_tot, delta_tlm)

print(f"Les pertes sont évaluées à {pertes:.2f} W vers l'extérieur")

# étape 4: évaluer la puissance en pompage nécessaire

perte_charge = perte_de_charge(Re_eau, longueur, D, densite_eau, vitesse_eau)
puissance_pomp = puissance_pompage(perte_charge, debit_massique, densite_eau)

print(f"La puissance de pompage requise est {puissance_pomp:.0f} W")