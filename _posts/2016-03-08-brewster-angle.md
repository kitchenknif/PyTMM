---
layout: page
title: "Brewster angle"
category: tut
date: 2016-03-08 18:08:02
order: 2
---
Short script to demonstrate the Brewster angle for p-polarized light when hitting
a dielectric-dieletric boundary.

### Imports

{% highlight python %}
    import numpy as np
    import matplotlib.pyplot as plt

    from pytmm.transferMatrix import *
{% endhighlight %}

### Calculations

{% highlight python %}
    n = 2
    d = 600  # slab thickness, nm
    l = 500  # wavelength, nm
    aoi = np.linspace(0, np.pi/2, 1000)
    TE = []
    TM = []

    for i in aoi:
        # TE
        a = TransferMatrix.layer(n, d, l, i, Polarization.s)

        R, T = solvePropagation(a)
        TE.append(np.abs(R**2))

        # TM
        a = TransferMatrix.layer(n, d, l, i, Polarization.p)
        R, T = solvePropagation(a)
        TM.append(np.abs(R**2))
{% endhighlight %}

### Plot

{% highlight python %}
    plt.plot(aoi, TE)
    plt.plot(aoi, TM)
    plt.xlabel("Angle, rad")
    plt.ylabel("Reflectance")
    plt.title("Angle dependence of reflectivity")
    plt.legend(['TE', 'TM'], loc='best')
    plt.show(block=True)
{% endhighlight %}
