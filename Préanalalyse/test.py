import numpy as np
import pandas as pd
from path import path_temperature
from fonctions import *

demande = 1*10**6 # demande des bâtiments en W

temp_alimentation = 90 # température en ˚C de l'eau en entrée du tuyau
temp_retour = 30 # température en ˚C de l'eau en sortie du tuyau
temp_moyenne = (temp_alimentation + temp_retour)/2

vitesse_eau = 3 # vitesse moyenne de l'eau dans le tuyau
densite_eau = 1 # densité de l'eau en kg/m^3
chaleur_specifique_eau = 4.18 * 10**3 # chaleur spécifique de l'eau qui est considéré comme constante pour la plage de temp. considérée
prandtl = calculer_prandtl_eau(temp_moyenne)
viscosite_eau = calculer_viscosite_eau(temp_moyenne)
reynolds = calculer_reynolds(densite_eau, viscosite_eau, 1, viscosite_eau)
print(viscosite_eau)
print(temp_moyenne + 273)



delta_T = temp_alimentation - temp_retour

debit_massique = demande/(delta_T * chaleur_specifique_eau)

d = D(debit_massique, vitesse_eau, densite_eau)

print(f"Le diamètre du tuyau est {d:.2f} m")
