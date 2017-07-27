import matplotlib.pyplot as plt
import numpy as np
import math

loop=1
Nx=50
Ny=50
M=4000

#Matriz potencial
V = np.zeros((Nx, Ny))

#Matriz de cargas
Rho = np.zeros((Nx, Ny))
Rho[9, :] = 50 #carga na placa superior
Rho[29, :] = -50 #carga na placa inferior

w = math.cos(math.pi/Nx)+math.cos(math.pi/Ny) # Converging Term

Ncount = 0
while loop==1:
    Rmin=0
    for i in range (1, Nx - 2):
        for j in range(1, Ny-2):
            Residue = 0.25*(V[i-1,j]+V[i+1,j]+V[i,j-1]+V[i,j+1]+Rho[i,j])-V[i,j];
            Rmin = Rmin + abs(Residue)
            V[i,j]= V[i,j] + Residue
            
    Rmin=Rmin/(Nx*Ny) # Average Residue per grid point
    Ncount = Ncount + 1
    if(Rmin<=0.00001):
        if(Ncount>M):
            loop=0
            print "nao converge."
        else:
            loop=0
            print "Converge em " + str (Ncount)

plt.imshow(V, cmap='hot', interpolation='nearest')
plt.show()
