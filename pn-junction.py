#!/usr/bin/env python
#-*- coding: utf-8 -*-

## Import common moduli
import matplotlib, sys, os, time
import matplotlib.pyplot as plt
import numpy as np
from scipy.constants import c, hbar, pi

x           = np.linspace(-10e-6, 10e-6, 1000)    # (m)
p_dop       = zeros_like(x)
p_dop[x<0]  = 1e18*(1e2**3)           # (m^-3)
n_dop       = zeros_like(x)
n_dop[x>0]  = 1e17*(1e2**3)           # (m^-3)

plt.plot(x, p_dop)

## ==== Outputting ====
## Finish the plot + save 
plt.xlabel(u"x"); 
plt.ylabel(u"y"); 
plt.grid()
plt.legend(prop={'size':10}, loc='upper right')
plt.savefig("output.png", bbox_inches='tight')

