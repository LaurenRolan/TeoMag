import matplotlib.pyplot as plt
import numpy as np
import math

loop=1
Ny=50
Nx=100
M=4000
centro = 28
#Matriz potencial
V = np.zeros((Ny, Nx))
V[23:33, :] = 5 # tensao no centro
V[12, :] = 0  # tensao na placa inferior
V[44, :] = 0
#Condicoes de fronteira
V[0,:]= 0
V[Ny-1,:]=0
V[:,0:20]=0
V[:,Nx-1]=0
#Matriz de cargas
Rho = np.zeros((Ny, Nx))

#Rho[1:Ny, 1:Nx]=0.0

for j in range(Ny-1):
    for i in range(Nx-1):
        # se estiver entre os dois aneis
        if((j > 12 and j < 22) or (j > 34 and j < 44)) and i > 20:
            Rho[j, i] = pow(abs(j - centro), -1)

Ncount = 0
while loop == 1:
    Rmin = 0
    for j in range (12, 44):
        for i in range(1, Nx-2): #Ny - 2
            if(j > 22 and j < 33 and i > 20):
                continue
            Residue = 0.25*(V[j-1,i]+V[j+1,i]+V[j,i-1]+V[j,i+1] + Rho[j, i])-V[j,i]
            Rmin = Rmin + abs(Residue)
            V[j,i]= V[j,i] + Residue
    Rmin=Rmin/(Nx*Ny) # Average Residue per grid point
    if(Rmin <= 0.0001):
        if(Ncount > M):
            loop=0
            print "nao converge."
        else:
            loop=0
            print "Converge em " + str (Ncount)

plt.title("Potencial")
plt.imshow(V, cmap='hot', interpolation='nearest')
plt.show()

skip = (slice(None, None, 3), slice(None, None, 3))
y, x = np.mgrid[500:-500:50j, 500:-500:100j]
dy, dx = np.gradient(V)
fig, ax = plt.subplots()
ax.quiver(x[skip], y[skip], dx[skip], dy[skip], V[skip])
ax.set(aspect=1, title='Campo Eletrico')
plt.show()