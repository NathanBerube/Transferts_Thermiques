import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from proprietes import *
from resistance_convection_interne import *
from resistance_conduction import *
from resistance_facteur_de_forme import *
from pertes import *
from demande_en_pompage import *

# Code pour le graphique qui met en relation le diamètre du tuyau et la puissance de pompage estimée pour différentes vitesse de l'écoulement


# paramètres de l'eau
V_eau = [1,2,3] # vitesse moyenne de l'eau dans le tuyau en m/s
rho_eau = 1000 # densité de l'eau en kg/m^3
mu_eau = 4.67 * 10**-4 # viscosité dynamique de l'eau en Pa.s (assumée comme constante dans la plage de température)

# paramètres du tuyau
D_tuy = np.linspace(0.10,0.5,200) # plage de valeurs pour le diamètre du tuyau en m
L_tuy = 1500 # longueur du tuyau, fixée à 1.5 km


for vitesse_eau in V_eau:

    m_dot = rho_eau * np.pi * 1/4 * D_tuy**2 * vitesse_eau # débit massique dans le tuyau
    Re_eau = calculer_reynolds(rho_eau, vitesse_eau, D_tuy, mu_eau) # Reynolds de l'eau

    perte_charge = perte_de_charge(Re_eau, L_tuy, D_tuy, rho_eau, vitesse_eau)  # calcul de la perte de charge dans le tuyau
    puissance_pomp = puissance_pompage(perte_charge, m_dot, rho_eau) # calcul de la puissance de pompage requise

    print(f"La puissance de pompage requise est {puissance_pomp} W")

    plt.plot(D_tuy, puissance_pomp/1000, label=f"Vitesse de l'eau = {vitesse_eau} m/s")

plt.xlabel("Diamètre du tuyau [m]", fontsize=18)
plt.ylabel("Puissance de pompage estimées [kW]", fontsize=18)
plt.legend()
plt.show()

