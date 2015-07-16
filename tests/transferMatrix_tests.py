from transferMatrix import *
import matplotlib.pyplot as plt
from refractiveIndex import *

catalog = RefractiveIndex("..\RefractiveIndex")
si = catalog.getMaterial('main', 'Si', 'Aspnes')

r, t = [], []
r1, t1 = [], []
r2, t2 = [], []
r3, t3 = [], []


#single layer
for i in range(100, 900):
    a = TransferMatrix.layer(1.46, 2000, i)
    b = TransferMatrix.layer(1.46-0.001j, 2000, i)
    c = TransferMatrix.layer(1.46-0.01j, 2000, i)
    d = TransferMatrix.layer(1.46-0.1j, 2000, i)

    R, T = solvePropagation(a)
    r.append(numpy.abs(R)**2)
    R, T = solvePropagation(b)
    r1.append(numpy.abs(R)**2)
    R, T = solvePropagation(c)
    r2.append(numpy.abs(R)**2)
    R, T = solvePropagation(d)
    r3.append(numpy.abs(R)**2)

    #res2 = solvePropagation(e)
    #b = findReciprocalTransferMatrix(res1[1], res1[0])

    #c = findGeneralizedTransferMatrix(res1[1], res1[0], res2[1], res2[0], bottomMat2=TransferMatrix.layer(1.46-1j*47, 1000, i))

    #res3 = solvePropagation(c)

    #R = numpy.abs(res3[1]-res1[1])

plt.plot(range(100, 900), r)
plt.plot(range(100, 900), r1)
plt.plot(range(100, 900), r2)
plt.plot(range(100, 900), r3)
plt.legend(['1.46', '1.46-0.001j', '1.46-0.01j', '1.46-0.1j'])
plt.show()