import matplotlib.pyplot as plt
import numpy as np
import math

loop=1
Nx=30
Ny=30
M=4000

#Matriz potencial
V = np.zeros((Nx, Ny))

#Matriz de cargas
Rho = np.zeros((Nx, Ny))
Rho[Nx/2, Ny/2] = 25

#Condicoes de fronteira
V[0,:]=50
V[Nx-1,:]=0
V[:,1]=0
V[:,Ny-1]=0

w = math.cos(math.pi/Nx)+math.cos(math.pi/Ny) # Converging Term
Ncount = 0
while loop==1:
    Rmin=0
    for i in range (1, Nx - 2):
        for j in range(1, Ny-2):
            #Erro na linha abaixo: da um numero mto maior do que deveria
            #Fiz baseada nessa linha do prog em MatLab
            #Residue=w.*(0.25.*(V(i-1,j)+V(i+1,j)+V(i,j-1)+V(i,j+1)+rho(i,j))-V(i,j));
            #A.*B is the element-by-element product of A and B
            Residue = w*(0.25*(V[i-1,j]+V[i+1,j]+V[i,j-1]+V[i,j+1]+Rho[i,j])-V[i,j]);
            Rmin = Rmin + abs(Residue)
            V[i,j]= V[i,j] + Residue


    Rmin=Rmin/(Nx*Ny) # Average Residue per grid point

    if(Rmin>=0.00001):
        Ncount=Ncount+1
        if(Ncount>M):
            loop=0
            print "nao converge."
        else:
            loop=0
            print "Converge em " + str (Ncount)

plt.imshow(V, cmap='hot', interpolation='nearest')
plt.show()
