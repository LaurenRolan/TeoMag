import matplotlib.pyplot as plt
import numpy as np
import math

loop=1
Nx=50
Ny=500
M=4000

#Matriz potencial
V = np.zeros((Nx, Ny)) #y = x, x = y
V[9, :] = 10 #tensao na placa superior
V[39, :] = 5 #tensao na placa inferior

#Condicoes de fronteira
V[0,:]= 0
V[Nx-1,:]=0
V[:,0]=0
V[:,Ny-1]=0

w = math.cos(math.pi/Nx)+math.cos(math.pi/Ny) # Converging Term
Ncount = 0
while loop == 1:
    Rmin = 0
    for i in range (10, 38):
        for j in range(1, Ny-2):
            Residue = 0.25*(V[i-1,j]+V[i+1,j]+V[i,j-1]+V[i,j+1])-V[i,j];
            Rmin = Rmin + abs(Residue)
            V[i,j]= V[i,j] + Residue
    Rmin=Rmin/(Nx*Ny) # Average Residue per grid point

    for i in range (38, 10, -1):
        for j in range(1, Ny-2):
            Residue = 0.25*(V[i-1,j]+V[i+1,j]+V[i,j-1]+V[i,j+1])-V[i,j];
            Rmin = Rmin + abs(Residue)
            V[i,j]= V[i,j] + Residue
    Rmin=Rmin/(Nx*Ny) # Average Residue per grid point
    
    Ncount = Ncount + 1
    
    if(Rmin<=0.0000000001):
        if(Ncount>M):
            loop=0
            print "nao converge."
        else:
            loop=0
            print "Converge em " + str (Ncount)
            
#Plota o mapa de calor
plt.title("Potencial")
plt.imshow(V, cmap='hot', interpolation='nearest')
plt.show()

#Plota o mapa vetorial
y, x = np.mgrid[50:-50:100j, 500:-500:100j]
dy, dx = np.gradient(V)
fig, ax = plt.subplots()
ax.quiver(x, y, dx, dy, V)
ax.set(aspect=1, title='Campo Eletrico')
plt.show()

