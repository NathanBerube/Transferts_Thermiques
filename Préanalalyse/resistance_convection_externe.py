import numpy as np

def churchill_bernstein(reynolds, prandtl):
    premier_terme = (0.62 * reynolds**(1/2) * prandtl**(1/3))/(1 + (0.4/prandtl)**(2/3))**(1/4)
    deuxieme_terme = (1 + (reynolds/282000)**(5/8))**(4/5)

    return 0.3 + premier_terme*deuxieme_terme

def résistance_convection_externe(D, k, L, Re, Pr):
    Nu = churchill_bernstein(Re, Pr)
    h = Nu * k / L
    print(h)
    A = L * np.pi * D

    return 1/(h*A)