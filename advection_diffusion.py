# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 16:23:22 2020

@author: chloe
"""

# Advection-Diffusion equation


import numpy as np
import matplotlib.pyplot as plt

# Setting the parameters
# We are using the same initial and boundary contions and velocity as in the advection equation quesiton

n = 50 # Number of elements
length = 100
x = np.linspace(0, n, length)
dt = 1.0
dx = 1.0
D = 1.0
Nsteps = 2000

v = -0.01 # advection velocity, assumed constant

f_LF = np.linspace(0, 1, length) # For Lax-Friedrich advection
f_ID = np.copy(f_LF) # For implicit diffusion

# Initializing these
f_LF[0] = 0.0
f_ID[0] = 0.0

# Constants we are given in the 'Writing Hydro Codes' document
alpha = (v*dt)/dx
beta = (D*dt)/(dx**2)

# Setting up the plots and plotting the initial state as a reference
plt.ion()
fig, axes = plt.subplots(1,2)
axes[0].set_title('Lax-Friedrich Advection', fontsize=14)
axes[1].set_title('Implicit Diffusion', fontsize=14)

axes[0].plot(x, f_LF, color='darkorange')
axes[1].plot(x, f_ID, color='darkorange')

# These are the objects that will be changing 
plt1, = axes[0].plot(x, f_LF, 'bo')
plt2, = axes[1].plot(x, f_ID, 'bo') 

fig.canvas.draw()

# Looping through f_LF and f_ID
a = 0 # counter
while a < Nsteps:
    
    # Lax-Friedrich :
    # Boundary conditions
    f_LF[-1] = 1.0
    f_LF[0] = 0.0
    
    # Lax-Friedrich advection
    f_LD[1:n-1] = 0.5*(f_LF[:n-2] + f_LF[2:]) - 0.5*alpha*(-f_LF[:n-2] + f_LF[2:])
        
    # Implicit diffusion :
    # Boundary conditions
    f_ID[-1] = 1.0
    f_ID[0] = 0.0
    
    # Implicit diffusion
    A = np.eye(n)*(1.0 + 2.0 * beta) + np.eye(n, k=1) * (-beta) + np.eye(n, k=-1) * (-beta) 
    
    # Applying the appropriate boundary conditions on A
    # Two different boundary conditions for diffusinve motion: no-slip and stress-free
    A[n-1][n-1] = 1.0
    A[n-1][n-2] = 0.0
    # To ensure v[0] stays fixed at all times: 
    A[0][0] = 1.0
    A[0][1] = 0.0
    # This makes sure that the first element is fixed and there's no diffusive flux through the first element
    
    # We can now solve for f_ID 
    f_ID = np.linalg.solve(A, f_ID) 
    
    # Plotting f_LF and f_ID
    plt1.set_ydata(f_LF)
    plt2.set_ydata(f_ID)
    fig.canvas.draw()
    plt.pause(0.001)
    a += 1