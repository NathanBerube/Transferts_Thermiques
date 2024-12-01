import numpy as np
import pandas as pd
from path import path_temperature
from fonctions import *

# variables imposées
demande = 1*10**6 # demande des bâtiments en W

temp_alimentation = 60 # température en ˚C de l'eau en entrée du tuyau
temp_retour = 45 # température en ˚C de l'eau en sortie du tuyau
temp_moyenne = (temp_alimentation + temp_retour)/2 # évaluation des propriétés à cette température

vitesse_eau = 3 # vitesse moyenne de l'eau dans le tuyau
densite_eau = 1000 # densité de l'eau en kg/m^3
chaleur_specifique_eau = 4.18 * 10**3 # chaleur spécifique de l'eau qui est considéré comme constante pour la plage de temp. considérée
conductivite_eau = 650 * 10**3 # conductivite de l'eau en W/m.k

# paramètres du tuyau
diametre = 0.15 # diametre du tuyau d'alimentation
conductivite = 50 # conducivité du tuyau en acier au carbone, estimée à 50 w/m.K
longueur = 1500 # longueur du tuyau, fixée à 1.5 km
epaisseur_tuyau = 0.01 # épaisseur du tuyau en mètres


# paramètres calculés en fonction de ceux imposés
prandtl = calculer_prandtl_eau(temp_moyenne)
viscosite_eau = calculer_viscosite_eau(temp_moyenne)
reynolds = calculer_reynolds(densite_eau, viscosite_eau, diametre, viscosite_eau)



# étape 1: évaluer la température en entrée des bâtiments

# étape 2: évaluer la résistance totale du circuit thermique

# étape 3: évaluer les pertes de chaleur en puissance