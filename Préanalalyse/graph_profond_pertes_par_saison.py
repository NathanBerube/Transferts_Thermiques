import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from proprietes import *
from resistance_convection_interne import *
from resistance_conduction import *
from resistance_facteur_de_forme import *
from pertes import *
from demande_en_pompage import *



#Valeur pour le vent par saison [température, vitesse]
H = [-19.8, 4.32]
P = [-12.4, 4.45]
E = [8.2, 4.40] 
A = [2.3, 4.40]

T_moy = (H[0] + P[0] + E[0] + A[0])/4
V_moy = (H[1] + P[1] + E[1] + A[1])/4

x = np.linspace(0, 4, 1000)
pertes_chaleur = []
T = (E[0] - H[0])/2 * np.sin(0.5 * np.pi * x) + (H[0] + E[0])/2

# plt.plot(x, T)
# plt.show()



# variables imposées
demande = 1*10**6 # demande des bâtiments en W

T_in = 60 # température en ˚C de l'eau en entrée du tuyau
T_out = 45 # température en ˚C de l'eau en sortie du tuyau

# paramètres de l'eau
V_eau = 2 # vitesse moyenne de l'eau dans le tuyau
rho_eau = 1000 # densité de l'eau en kg/m^3
C_eau = 4.18 * 10**3 # chaleur spécifique de l'eau qui est considéré comme constante pour la plage de temp. considérée
k_eau = 650 * 10**-3 # conductivite de l'eau en W/m.k
conductivite_sol = 2.18

# paramètres de l'air
k_air = 24*10**-3
V_air = V_moy
rho_air = 1.2

# paramètres du tuyau
D_tuy = 0.15 # diametre du tuyau d'alimentation
k_tuy = 50 # conducivité du tuyau en acier au carbone, estimée à 50 w/m.K
L_tuy = 1500 # longueur du tuyau, fixée à 1.5 km
t_tuy = 0.01 # épaisseur du tuyau en mètres
Z_tuyau = 1 # profondeur du tuyau en m

# paramètres de l'isolant
D_iso = D_tuy+(2*t_tuy)
t_iso = 0.05
L_iso = L_tuy
k_iso = 0.04 #conductuvité thermique de l'isolant - 0.035 = laine de verre ou laine de roche
# https://nmc-insulation.com/wp-content/uploads/sites/3/2020/03/3010332_CLIMATUBE_BRO_FR_2020-03.pdf

# étape 1: évaluer la température en entrée des bâtiments
m_dot = rho_eau * np.pi * 1/4 * D_tuy**2 * V_eau # débit massique
T_out_theorique = demande/(m_dot * C_eau) + T_out
T_moy = (T_in + T_out_theorique)/2 # évaluation des propriétés à cette température

# paramètres calculés en fonction de ceux imposés
Pr_eau = 6.9
# mu_eau = calculer_viscosite_eau(T_moy)
mu_eau = 4.67 * 10**-4
Re_eau = calculer_reynolds(rho_eau, V_eau, D_tuy, mu_eau)

# étape 1: évaluer la température en entrée des bâtiments
m_dot = rho_eau * np.pi * 1/4 * D_tuy**2 * V_eau
T_out_théorique = demande/(m_dot * C_eau) + T_out
T_moy = (T_in + T_out_théorique)/2 # évaluation des propriétés à cette température

# paramètres calculés en fonction de ceux imposés
mu_eau = 4.67 * 10**-4
Re_eau = calculer_reynolds(rho_eau, V_eau, D_tuy, mu_eau)
Pr_eau = 6.9 #Pr_eau = calculer_prandtl_eau(T_moy)

# étape 2: évaluer la résistance totale du circuit thermique
R_conv_int = résistance_convection_interne(D_tuy, k_eau, L_tuy)
R_cond_tuy = calculer_Rconduction_cylindre(D_tuy, t_tuy, L_tuy, k_tuy)
R_cond_iso = calculer_Rconduction_cylindre(D_iso, t_iso, L_tuy, k_iso)
R_S = R_profond(L_tuy, Z_tuyau, D_iso + 2*t_iso, conductivite_sol)
print(f"Résistance de convection interne {R_conv_int}")
print(f"Résistance de conduction tuyau {R_cond_tuy}")
print(f"Résistance de conduction isolant {R_cond_iso}")
print(f"Résistance profond {R_S}")

R_tot = R_conv_int + R_cond_tuy + R_S + R_cond_iso
print(f"La résistance totale est {R_tot}")

for T_air in T:
    # étape 3: évaluer les pertes de chaleur en puissance

    delta_tlm = del_tlm(T_air, T_in, T_out_théorique)
    pertes = calculer_pertes(R_tot, delta_tlm)

    # print(f"Les pertes sont évaluées à {pertes} W vers l'extérieur")

    # étape 4: évaluer la puissance en pompage nécessaire

    perte_charge = perte_de_charge(Re_eau, L_tuy, D_tuy, rho_eau, V_eau)
    puissance_pomp = puissance_pompage(perte_charge, m_dot, rho_eau)


    pertes_chaleur.append(np.abs(pertes)/1000)


plt.plot(x, pertes_chaleur)
plt.xticks([0, 1, 2, 3, 4], ["Printemps", "Été", "Automne", "Hiver", "Printemps"])
plt.show()