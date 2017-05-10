import numpy as np
import matplotlib.pyplot as plt
from math import copysign

x = np.linspace(-1, 1, 100)
y = np.linspace(-1, 1, 100)
xm, ym = np.meshgrid(x, y)

def constrain(a, l, u):
    if a > u:
        return u
    elif a < l:
        return l
    else:
        return a


def l_linear(x, y):
    # if y >= 0:
    #     if x < 0:
    #         return y+x
    #     if x >= 0:
    #         return (x**2 + y**2)**0.5
    # else:
    #     if x < 0:
    #         return y+x
    #     if x >= 0:
    #         return -(x**2 + y**2)**0.5
    return constrain(copysign((x ** 2 + y ** 2) ** 0.5, y) + x, -1, 1)

out = np.zeros(xm.shape)
for i, xi in enumerate(x):
    for j, yi in enumerate(y):
        out[j, i] = l_linear(xi, yi)

plt.subplot(121)
plt.imshow(out, origin='lower')
plt.colorbar()
plt.subplot(122)
plt.contour(out,)
# plt.colorbar()
plt.show()

