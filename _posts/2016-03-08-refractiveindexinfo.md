---
layout: page
title: "Refractiveindex.info"
category: tut
date: 2016-03-08 18:19:04
order: 4
---
```
import numpy
import matplotlib.pyplot as plt

from PyTMM.transferMatrix import *
from PyTMM.refractiveIndex import *

database = path_to_database_root
catalog = RefractiveIndex(database)

sio2 = catalog.getMaterial('main', 'SiO2', 'Malitson')

ran = range(400, 800, 1)
reflectance = []

for i in ran:
    a = TransferMatrix.boundingLayer(1, sio2.getRefractiveIndex(i))
    R, T = solvePropagation(a)
    reflectance.append(numpy.abs(R**2))
    
plt.plot(ran, reflectance)
plt.xlabel("wavelength, nm")
plt.ylabel("reflectance")
plt.title("Reflectance of single SiO2 Boundary")
plt.show(block=True)

```
