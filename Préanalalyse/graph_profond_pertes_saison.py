import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from proprietes import *
from resistance_convection_interne import *
from resistance_conduction import *
from resistance_facteur_de_forme import *
from pertes import *
from demande_en_pompage import *


# Code pour le graphique qui met en relation la profondeur du tuyau hors sol et les pertes de chaleur moyennes pour les quatres saisons
# Les caractéristiques de l'écoulement sont les valeurs moyennes des plages d'utilisation fournies dans l'énoncé

# Propriétés du vent pour le vent par saison [température en ˚C, vitesse en m/s]
H = [-19.8, 4.32]
P = [-12.4, 4.45]
E = [8.2, 4.40] 
A = [2.3, 4.40]
saisons = [H,P,E,A]
noms_saisons = ["Hiver", "Printemps", "Été", "Automne"]

# Variables imposées
demande = 1*10**6 # demande des bâtiments en W

# Température à l'entrée et la sortie du système en prenant la moyenne des plages fournies
T_in = 60 # température en ˚C de l'eau en entrée du tuyau
T_out = 45 # température en ˚C de l'eau en sortie du tuyau

# paramètres de l'eau
V_eau = 2 # vitesse moyenne de l'eau dans le tuyau
rho_eau = 1000 # densité de l'eau en kg/m^3
C_eau = 4.18 * 10**3 # chaleur spécifique de l'eau qui est considéré comme constante pour la plage de temp. considérée
k_eau = 650 * 10**-3 # conductivite de l'eau en W/m.k
mu_eau = 4.67 * 10**-4 # viscosité dynamique de l'eau en Pa.s (assumée comme constante dans la plage de température)
Pr_eau = 6.9 # Prandlt de l'eau (assumé comme constant dans la plage de température)

conductivite_sol = 2.18

# paramètres du tuyau
D_tuy = 0.15 # diametre du tuyau d'alimentation
k_tuy = 50 # conducivité du tuyau en acier au carbone, estimée à 50 w/m.K
L_tuy = 1500 # longueur du tuyau, fixée à 1.5 km
t_tuy = 0.01 # épaisseur du tuyau en mètres
Z_tuyau = np.linspace(3*D_tuy/2, 3, 200)

# paramètres de l'isolsant
D_iso = D_tuy+(2*t_tuy) # diamètre interne de la couche d'isolant en m
t_iso = 0.05 # épaisseur de l'isolant en m
L_iso = L_tuy # longueur de l'isolant qui est la même que celle du tuyau
k_iso = 0.04 # conductuvité thermique de l'isolant - 0.04 = laine de verre ou laine de roche ou du polyurethane 
# https://nmc-insulation.com/wp-content/uploads/sites/3/2020/03/3010332_CLIMATUBE_BRO_FR_2020-03.pdf

for i, saison in enumerate(saisons):
    print(noms_saisons[i])

    # paramètres de l'air
    k_air = 24*10**-3 # conductivité de l'air en W/k.m
    V_air = saison[1] # vitesse du vent pour la saison
    rho_air = 1.2 # densité de l'air en kg/m^3 qui est environ constante selon la température
    T_air = saison[0] # température de l'air pour la saison


    # étape 1: évaluer la température en entrée des bâtiments
    # utilisation de l'équation q = m_dot * c_p (T_in - T_out) pour calculer la température de sortie 
    # T_out_theorique à la sortie du tuyau d'alimentation (en entrée des habitations) en connaissant la 
    # température en sortie des bâtiments (en moyenne de 45˚C selon les plages fournies)
    m_dot = rho_eau * np.pi * 1/4 * D_tuy**2 * V_eau # débit massique dans le tuyau
    T_out_théorique = demande/(m_dot * C_eau) + T_out # température de sortie du tuyau d'alimentation

    # paramètres calculés en fonction de ceux imposés
    T_moy = (T_in + T_out_théorique)/2 # évaluation des propriétés à cette température
    Re_eau = calculer_reynolds(rho_eau, V_eau, D_tuy, mu_eau) # Reynolds de l'eau

    # étape 2: évaluer la résistance totale du circuit thermique
    R_conv_int = résistance_convection_interne(D_tuy, k_eau, L_tuy) # résistance de convection interne dans le tuyau
    R_cond_tuy = calculer_Rconduction_cylindre(D_tuy, t_tuy, L_tuy, k_tuy) # résistance de conduction dans le tuyau
    R_cond_iso = calculer_Rconduction_cylindre(D_iso, t_iso, L_tuy, k_iso) # résistance de conduction dans l'isolant
    R_S = R_profond(L_tuy, Z_tuyau, D_iso + 2*t_iso, conductivite_sol) # résistance de conduction dans le sol
    print(f"Résistance de convection interne {R_conv_int}")
    print(f"Résistance de conduction tuyau {R_cond_tuy}")
    print(f"Résistance de conduction isolant {R_cond_iso}")
    print(f"Résistance profond {R_S}")

    # résistance totale circuit thermique sachant que les résistances sont en série
    R_tot = R_conv_int + R_cond_tuy + R_S + R_cond_iso
    print(f"La résistance totale est {R_tot}")

    # étape 3: évaluer les pertes de chaleur en puissance
    delta_tlm = del_tlm(T_air, T_in, T_out_théorique) # calcul du ∆T_lm avec les températures en entrée et sortie du tuyau
    pertes = calculer_pertes(R_tot, delta_tlm) # calcul des pertes selon l'équation q = UA ∆T_lm avec 1/R_tot = UA

    print(f"Les pertes sont évaluées à {pertes} W vers l'extérieur")

    # étape 4: évaluer la puissance en pompage nécessaire
    perte_charge = perte_de_charge(Re_eau, L_tuy, D_tuy, rho_eau, V_eau) # calcul de la perte de charge dans le tuyau
    puissance_pomp = puissance_pompage(perte_charge, m_dot, rho_eau) # calcul de la puissance de pompage requise

    print(f"La puissance de pompage requise est {puissance_pomp} W")

    plt.plot(Z_tuyau, np.abs(pertes)/1000, label=noms_saisons[i])

plt.xlabel("Profondeur du tuyau [m]", fontsize=18)
plt.ylabel("Pertes de chaleur estimées [kW]", fontsize=18)
plt.legend()
plt.show()

