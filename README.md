# Transferts_Thermiques
Tous les codes ayant permis les calculs associés à la préanalyse énergétique sont présentés ici. Deux solutions potentielles sont envisagées : un tuyau hors-terre et un tuyau enterré. Les calculs pour les deux cas sont réalisés dans le code.

Les scripts main_hors_terre.py et main_profond.py permettent de calculer rapidement les résistances thermiques, les pertes totales du système, ainsi que la demande en puissance de pompage pour les deux solutions proposées.

Les scripts graph(...).py permettent de visualiser l'influence de plusieurs paramètres tels que le diamètre du tuyau, l'épaisseur de l’isolant, la profondeur (cas enterré), la température externe (selon la saison) et la vitesse du vent (selon la saison). Ces fichiers génèrent tous les graphiques présentés en annexe du rapport.

Afin d’obtenir des résultats préliminaires orientés sur les ordres de grandeur, plusieurs hypothèses ont été formulées.

Tout d’abord, la température d’alimentation et de retour du système a été estimée à partir de la moyenne de la plage de valeurs fournies, étant donné que ces températures peuvent fluctuer dans le temps selon la demande énergétique des habitations.

Par ailleurs, étant donné que les propriétés de l’eau varient peu dans la plage de températures concernées par le projet, celles-ci ont été considérées comme constantes pour simplifier les calculs. Les propriétés de l’eau ont été évaluées à la température moyenne de la plage d’opération. Ces valeurs peuvent être retrouvées aisément dans la section prévue à cet effet (en haut de chaque fichier).

En ce qui concerne l’air, ses propriétés, plus sensibles à la température dans la plage considérée, ont été déterminées par interpolation linéaire à partir des tables présentées en annexe du recueil.

Les équations et corrélations utilisées proviennent intégralement du recueil. Les détails concernant chaque équation, ainsi que leur utilisation, sont documentés dans les fichiers, qui les classent par catégorie pour en faciliter la consultation.

L’estimation des pertes thermiques a été réalisée en tenant compte de la demande en énergie des habitations, ainsi que des températures d’entrée et de sortie du réseau. En laissant le diamètre du tuyau d’alimentation et la vitesse de l’eau comme paramètres libres, le débit massique dirigé vers les habitations a été déterminé. Cette connaissance permet de calculer la température en sortie du tuyau d’alimentation (ou entrée des habitations) grâce à un bilan d’énergie, $q = \dot{m}c_p\Delta T$, effectué au niveau des habitations.

La température ainsi obtenue permet d’estimer les pertes thermiques dans le tuyau d’alimentation. Pour cela, il est nécessaire de calculer la résistance thermique totale entre l’air ambiant et l’écoulement. Les détails du circuit thermique sont disponibles dans les différents fichiers. Les pertes thermiques sont ensuite calculées à l’aide d’un bilan d’énergie appliqué au tuyau d’alimentation avec l’équation suivante extraite du recueil $q_{pertes} = \frac{1}{R_{tot}}\Delta T_{lm}$


Les détails concernant la perte de charge et la demande en pompage se trouve dans le fichier demande_en_pompage.py.


Également, l'influence de la saison peut-être observée en sélectionnant les valeurs moyennes de température et de vitesse de vent en choisisant la saison désirée dans les scripts main_hors_terre.py et main_profond.py. Plus de détails s'y trouvent.


