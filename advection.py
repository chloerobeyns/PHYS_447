# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 12:21:30 2020

@author: chloe
"""

# Advection equation 

import numpy as np
import matplotlib.pyplot as plt

# Setting up the grid
length = 100
f = np.linspace(0, 1000, length)
x = np.linspace(0, 100, length)
grid = 100
dt = 1.0
dx = 1.0
Nsteps = 5000

v = -0.1 # advection velocity, assumed constant
step = v*dt/(2*dx) 

# Initial conditions
f1 = np.copy(f)
f2 = np.copy(f)

# Setting up the plots and plotting the initial state as a reference
plt.ion()
fig, axes = plt.subplots(1,2)
axes[0].set_title('FTCS', fontsize=14)
axes[1].set_title('Lax-Friedrich', fontsize=14)

axes[0].plot(x, f1, color='darkorange')
axes[1].plot(x, f2, color='darkorange')

# These are the objects that will be changing 
plt1, = axes[0].plot(x, f1, 'bo')
plt2, = axes[1].plot(x, f2, 'bo') 

fig.canvas.draw()

# Looping through f1 and f2
a = 0 # counter
while a < Nsteps:
    
    # FTCS
    f1[1:grid-1] = f1[1:grid-1] - step*(f1[2:] - f1[:grid-2])
    
    # Lax-Friedrich
    f2[1:grid-1] = 0.5*(f2[2:] + f2[:grid-2]) - step*(f2[2:] - f2[:grid-2])
    
    # Plotting these
    plt1.set_ydata(f1)
    plt2.set_ydata(f2)
    fig.canvas.draw()
    plt.pause(0.001)
    a += 1