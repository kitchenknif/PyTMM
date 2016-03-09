---
layout: page
title: "Total internal reflection"
category: tut
date: 2016-03-08 18:08:28
order: 3
---
Script to demonstrate total internal reflection when incident light is coming
from a medium with a higher refractive index.

{% highlight python%}

import numpy as np
import matplotlib.pyplot as plt

from PyTMM.pytmm.transferMatrix import *

n = 2
aoi = np.linspace(0, np.pi/2, 1000)
TE = []
TM = []
for i in aoi:
    # TE
    a = TransferMatrix.boundingLayer(n, 1, i, Polarization.s)

    R, T = solvePropagation(a)
    TE.append(np.abs(R**2))

    # TM
    a = TransferMatrix.boundingLayer(n, 1, i, Polarization.p)
    R, T = solvePropagation(a)
    TM.append(np.abs(R**2))


plt.plot(aoi, TE)
plt.plot(aoi, TM)
plt.xlabel("Angle, rad")
plt.ylabel("Reflectance")
plt.title("Angle dependence of reflectivity")
plt.legend(['TE', 'TM'], loc='best')
plt.show(block=True)

{% endhighlight%}
