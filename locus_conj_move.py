from scipy.signal import lti, tf2zpk

import numpy as np
import matplotlib.pyplot as plt


n = np.array([1, 12, 35])
d = np.array([1, 3, 2])



def draw_pzs(num, den):
    z, p, k = tf2zpk(num, den)
    plt.plot(np.real(z), np.imag(z), 'or')
    plt.plot(np.real(p), np.imag(p), 'xb')
    print z,p


draw_pzs(n, d)




for k in np.logspace(-2, 1.5):
    n = np.array([1, 12, 35])
    d = np.array([k+1, 3+12*k, 2+35*k])
    draw_pzs(n, d)

plt.grid(True)
plt.show()

