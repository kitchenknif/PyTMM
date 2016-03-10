import matplotlib.pyplot as plt

from PyTMM.transferMatrix import *

r, t = [], []
r1, t1 = [], []
r2, t2 = [], []
r3, t3 = [], []

wavelengths = numpy.linspace(300, 1500, 2000)
for i in wavelengths:
    a = TransferMatrix.layer(1.46, 200, i)
    b = TransferMatrix.layer(1.46 - 0.001j, 200, i)
    c = TransferMatrix.layer(1.46 - 0.01j, 200, i)
    d = TransferMatrix.layer(1.46 - 0.1j, 200, i)

    R = solvePropagation(a)[0]
    r.append(numpy.abs(R) ** 2)
    R = solvePropagation(b)[0]
    r1.append(numpy.abs(R) ** 2)
    R = solvePropagation(c)[0]
    r2.append(numpy.abs(R) ** 2)
    R = solvePropagation(d)[0]
    r3.append(numpy.abs(R) ** 2)

plt.plot(wavelengths, r)
plt.plot(wavelengths, r1)
plt.plot(wavelengths, r2)
plt.plot(wavelengths, r3)
plt.legend(['1.46', '1.46-0.001j', '1.46-0.01j', '1.46-0.1j'], loc='best')
plt.show()
