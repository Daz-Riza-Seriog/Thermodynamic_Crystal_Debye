import numpy as np
from scipy.integrate import simps
import math

T_env = 50 #Mg  298-->Diamond
T_deybe = 290 #Mg 1860-->Diamond
lim = T_deybe/T_env

N_a = 6.022E23  #Avogadro Constant
K_b = 1.380649E-23  #Boltzman's constant [J/K]

x = np.linspace(0.000000001,lim,endpoint=True)

y = (x**4)*((math.e)**x)/(((math.e)**x)-1)**2

integer = simps(y,x)

fac = (T_env/T_deybe)**3

D = 3*fac*integer

C_v = 3*N_a*K_b*D

### Electron contribution by specific heat ##
U_o = 7.08  # Fermi energy [eV]
k_b = 8.617333262145E-5 # Boltman's constant [eV/K]
N_e = (8.61E28)*((1/100)**3)  #Free electron Number Density [cm^-3]
T_f = U_o/k_b    #Fermi's Temperature [K]

#Heere we use the Boltzman constant in [J/K]
C_v_e = ((np.pi**2)/2)*(N_e)*(K_b)*(T_env/T_f)

print(C_v)
print(C_v_e)