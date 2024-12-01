import numpy as np
import pandas as pd
from fonctions import *
from resistance_convection_interne import *
from resistance_conduction import *
from resistance_convection_externe import *

# variables imposées
demande = 1*10**6 # demande des bâtiments en W

T_in = 60 # température en ˚C de l'eau en entrée du tuyau
T_out = 45 # température en ˚C de l'eau en sortie du tuyau

# paramètres de l'eau
V_eau = 2 # vitesse moyenne de l'eau dans le tuyau
rho_eau = 1000 # densité de l'eau en kg/m^3
C_eau = 4.18 * 10**3 # chaleur spécifique de l'eau qui est considéré comme constante pour la plage de temp. considérée
k_eau = 650 * 10**-3 # conductivite de l'eau en W/m.k

k_air = 24*10**-3
V_air = 5
rho_air = 1.2

# paramètres du tuyau
D_tuy = 0.15 # diametre du tuyau d'alimentation
k_tuy = 50 # conducivité du tuyau en acier au carbone, estimée à 50 w/m.K
L_tuy = 1500 # longueur du tuyau, fixée à 1.5 km
t_tuy = 0.01 # épaisseur du tuyau en mètres

# étape 1: évaluer la température en entrée des bâtiments
m_dot = rho_eau * np.pi * 1/4 * D_tuy**2 * V_eau # débit massique
T_out_theorique = demande/(m_dot * C_eau) + T_out
T_moy = (T_in + T_out_theorique)/2 # évaluation des propriétés à cette température

# paramètres calculés en fonction de ceux imposés
Pr_eau = calculer_prandtl_eau(T_moy)
mu_eau = calculer_viscosite_eau(T_moy)
Re_eau = calculer_reynolds(rho_eau, V_eau, D_tuy+2*t_tuy, mu_eau)
Pr_air = 0.72
mu_air = 16 * 10**-6
Re_air = calculer_reynolds(rho_air, V_air, D_tuy+2*t_tuy, mu_air)

# étape 2: évaluer la résistance totale du circuit thermique

R_conv_int = résistance_convection_interne(D_tuy, k_eau, L_tuy)
R_cond = calculer_Rconduction_cylindre(D_tuy, t_tuy, L_tuy, k_tuy)
R_conv_ext = résistance_convection_externe(D_tuy, k_air, L_tuy, Re_air, Pr_air)

R_tot = R_conv_int + R_cond + R_conv_ext

print(R_tot)

# étape 3: évaluer les pertes de chaleur en puissance