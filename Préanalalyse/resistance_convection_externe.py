import numpy as np

# Ce fichier permet de calculer tout ce qui est en lien avec la convection externe avec l'air dans le cas d'un tuyau hors-terre

def churchill_bernstein(reynolds, prandtl):
    # Fonction qui calcule le nombre de Nusselt d'un tuyau externe à l'aide de la corrélation
    # de Churchill-Bernstein qui est valide sous la condition Re_D * PR >= 0.2 (p. 24 du recueil). Cette condition est toujours remplie
    # pour la plage de valeur considérée.
    premier_terme = (0.62 * reynolds**(1/2) * prandtl**(1/3))/(1 + (0.4/prandtl)**(2/3))**(1/4)
    deuxieme_terme = (1 + (reynolds/282000)**(5/8))**(4/5)

    return 0.3 + premier_terme*deuxieme_terme

def résistance_convection_externe(D, k, L, Re, Pr):
    # calcul de la résistance de convection externe à l'aide de la corrélation présentée plus haut.
    # La coefficient de convection peut être déterminé à partir du nombre de Nusselt selon la définition de ce dernier
    # La résistance de convection est ensuite calculé pour la surface externe du cylindre selon l'équation appropriée (recueil p.7)
    Nu = churchill_bernstein(Re, Pr)
    h = Nu * k / D
    A = L * np.pi * D

    return 1/(h*A)
