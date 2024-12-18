# Transferts_Thermiques
Tous les codes qui ont permis les calculs associés à la préanalyse énergétique. Deux solutions potentielles sont envisagées. Un tuyau hors-terre et un dans le seul. Les calculs pour les deux codes sont faits.

Les codes main_hors_terre.py et main_profond.py permettent de rapidement calculer les résistances thermiques, les pertes totales du système ainsi que la demande en puissance de pompage pour les deux solutions proposées. 

Les codes graph(...).py permettent de visualiser l'influence de plusieurs paramètres comme le diamètre du tuyau, l'épaisseur de l'isolant, la profondeur (cas dans le sol), la température externe (selon la saison), la vitesse du vent (selon la saison). Ces fichiers permettent d'obtenir tous les graphiques qui se trouvent en annexe du rapport.

Afin d'arriver aux résultats préliminaires qui s'intéressent plutôt au ordres de grandeur, plusieurs hypothèses ont été posées.

Tout d'abord, la température d'alimentation et de retour du système ont été estimée à l'aide de la moyenne de la plage de valeur fournie étant donnée que ces valeurs peuent fluctuer dans le temps selon la demande émergétique des habitations.

Par ailleurs, étant donné que les propriétés varient peu dans la plage de température en jeu dans le projet, celle-ci ont été considérées comme constante pour simplifier les calculs. Les propriétés ont été évaluées à la température moyenne de la plage d'opération. Les valeurs peuvent retrouvées dans le code aisèment dans la section prévue à cet effet (en haut de chaque fichier).

Pour l'air, les propriétés sont plus sensibles à la température pour les températures en jeu, alors une interpolation linéaire des tables en annexe du recueil a été faite.


Pour ce qui est des équations/corrélations utilisées, elles proviennent toutes du recueil. Les détails pour chacune des équations ainsi que leur utilisation se retourve dans les fichiers qui séparent les équations par catégorie et permet leur présentation.


L'estimation des pertes a été possible en connaissant la demande en énergie des habitations ainsi que les températures d'entrée et de sortie du réseau entier. En laissant le diamètre du tuyau d'alimentation et la vitesse de l'eau comme paramètre libre, le débit massique se dirigeant vers les habitations est déterminé. La connaissance de ce débit massique permet de retrouver la température en sortie du tuyau d'alimentaion (ou entrée des habitations) à l'aide d'un bilan d'énergie $q = \dot{m}c_p\Delta T$ au niveau des habitations. L'obtention de cette température permet alors d'estimer les pertes dans le tuyau d'alimentation. Il est cependant nécessaire de calculer la résistance thermique totale entre l'air ambiant et l'écoulement. Les détails du circuit thermique se trouvent dans les différents fichiers. Les pertes peuvent ensuite être calculées avec un bilan d'énergie sur le tuyau d'alimentation à l'aide de l'équation suivante du recueil $$q_{pertes} = \frac{1}{R_tot}\Delta T_{lm}$$


