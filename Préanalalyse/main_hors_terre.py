import numpy as np
import pandas as pd
from proprietes import *
from resistance_convection_interne import *
from resistance_conduction import *
from resistance_convection_externe import *
from pertes import *
from demande_en_pompage import *


# variables imposées
demande = 1*10**6 # demande des bâtiments en W

T_in = 60 # température en ˚C de l'eau en entrée du tuyau
T_out = 45 # température en ˚C de l'eau en sortie du tuyau

# paramètres de l'eau
V_eau = 2 # vitesse moyenne de l'eau dans le tuyau
rho_eau = 1000 # densité de l'eau en kg/m^3
C_eau = 4.18 * 10**3 # chaleur spécifique de l'eau qui est considéré comme constante pour la plage de temp. considérée
k_eau = 650 * 10**-3 # conductivite de l'eau en W/m.k

# paramètres de l'air
k_air = 24*10**-3
V_air = 5
rho_air = 1.2
T_air = 0

# paramètres du tuyau
D_tuy = 0.15 # diametre du tuyau d'alimentation
k_tuy = 50 # conducivité du tuyau en acier au carbone, estimée à 50 w/m.K
L_tuy = 1500 # longueur du tuyau, fixée à 1.5 km
t_tuy = 0.01 # épaisseur du tuyau en mètres

# paramètres de l'isolsant
D_iso = D_tuy+(2*t_tuy)
t_iso = 0
L_iso = L_tuy
k_iso = 0.035 #conductuvité thermique de l'isolant - 0.035 = laine de verre ou laine de roche


# étape 1: évaluer la température en entrée des bâtiments
m_dot = rho_eau * np.pi * 1/4 * D_tuy**2 * V_eau # débit massique
T_out_theorique = demande/(m_dot * C_eau) + T_out
T_moy = (T_in + T_out_theorique)/2 # évaluation des propriétés à cette température

# paramètres calculés en fonction de ceux imposés
Pr_eau = 6.9
# mu_eau = calculer_viscosite_eau(T_moy)
mu_eau = 4.67 * 10**-4
Re_eau = calculer_reynolds(rho_eau, V_eau, D_tuy, mu_eau)

Pr_air = calculer_prandtl_air(T_air)
mu_air = calculer_viscosite_air(T_air)
Re_air = calculer_reynolds(rho_air, V_air, D_iso + 2*t_iso, mu_air)

# étape 2: évaluer la résistance totale du circuit thermique
R_conv_int = résistance_convection_interne(D_tuy, k_eau, L_tuy)
R_cond_tuy = calculer_Rconduction_cylindre(D_tuy, t_tuy, L_tuy, k_tuy)
R_cond_iso = calculer_Rconduction_cylindre(D_iso, t_iso, L_tuy, k_iso)
R_conv_ext = résistance_convection_externe(D_iso + 2*t_iso, k_air, L_tuy, Re_air, Pr_air)
print(f"Résistance de convection interne {R_conv_int}")
print(f"Résistance de conduction tuyau {R_cond_tuy}")
print(f"Résistance de conduction isolant {R_cond_iso}")
print(f"Résistance de convection externe {R_conv_ext}")

R_tot = R_conv_int + R_cond_tuy + R_conv_ext + R_cond_iso 
print(f"La résistance totale est {R_tot:.5f}")

# étape 3: évaluer les pertes de chaleur en puissance

delta_tlm = delta_tlm(T_air, T_in, T_out_theorique)
pertes = calculer_pertes(R_tot, delta_tlm)

print(f"Les pertes sont évaluées à {pertes:.2f} W vers l'extérieur")

# étape 4: évaluer la puissance en pompage nécessaire

perte_charge = perte_de_charge(Re_eau, L_tuy, D_tuy, rho_eau, V_eau)
puissance_pomp = puissance_pompage(perte_charge, m_dot, rho_eau)

print(f"La puissance de pompage requise est {puissance_pomp:.0f} W")