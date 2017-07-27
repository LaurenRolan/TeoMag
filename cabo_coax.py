import matplotlib.pyplot as plt
import numpy as np
import math

loop=1
Nx=50
Ny=50
M=4000

#Matriz potencial
V = np.zeros((Nx, Ny)) #y = x, x = y

#Condicoes de fronteira
V[0,:]= 0
V[Nx-1,:]=0
V[:,0]=0
V[:,Ny-1]=0

width1, height1 = 33, 33
r1 = 16
a, b = 25, 25

width2, height2 = 11, 11
r2 = 5

EPSILON = 2.2

# draw the circle
for y in range(height1):
    for x in range(width1):
        # see if we're close to (x-a)**2 + (y-b)**2 == r**2
        if (x-a)**2 + (y-b)**2 - r1**2 == 0:
            print "Entro aqui."
            V[y, x] = 0

for y in range(height2, height1):
    for x in range(width2, width1):
        # see if we're close to (x-a)**2 + (y-b)**2 == r**2
        if abs((x - a)**2 + (y - b)**2 - r2**2) < EPSILON**2:
            print "Entro aqui."
            V[y, x] = 5

plt.title("Potencial")
plt.imshow(V, cmap='hot', interpolation='nearest')
plt.show()


w = math.cos(math.pi/Nx)+math.cos(math.pi/Ny) # Converging Term
Ncount = 0
while loop == 1:
    Rmin = 0
    for i in range(height2, height1):
        for j in range(width2, width1):
            # see if we're close to (x-a)**2 + (y-b)**2 == r**2
            if abs((x - a) ** 2 + (y - b) ** 2 - r1 ** 2) < EPSILON ** 2:
                Residue = 0.25 * (V[i - 1, j] + V[i + 1, j] + V[i, j - 1] + V[i, j + 1]) - V[i, j];
                Rmin = Rmin + abs(Residue)
                V[i, j] = V[i, j] + Residue
    Rmin=Rmin/(Nx*Ny) # Average Residue per grid point

    for i in range(height1, height2, -1):
        for j in range(width1, width2, -1):
            # see if we're close to (x-a)**2 + (y-b)**2 == r**2
            if abs((x - a) ** 2 + (y - b) ** 2 - r1 ** 2) < EPSILON ** 2:
                Residue = 0.25 * (V[i - 1, j] + V[i + 1, j] + V[i, j - 1] + V[i, j + 1]) - V[i, j];
                Rmin = Rmin + abs(Residue)
                V[i, j] = V[i, j] + Residue
    Rmin=Rmin/(Nx*Ny) # Average Residue per grid point
    Ncount = Ncount + 1
    if(Rmin<=0.0000001):
        if(Ncount>M):
            loop=0
            print "nao converge."
        else:
            loop=0
            print "Converge em " + str (Ncount)

plt.title("Potencial")
plt.imshow(V, cmap='hot', interpolation='nearest')
plt.show()

y, x = np.mgrid[50:-50:100j, 500:-500:100j]
dy, dx = np.gradient(V)
fig, ax = plt.subplots()
ax.quiver(x, y, dx, dy, V)
ax.set(aspect=1, title='Campo Eletrico')
plt.show()
