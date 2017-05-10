import numpy
from scipy.signal import lti, step2


g = 9.81       # m/s^2, gravitational constant

m = 5          # kg, mass
l = 0.4        # m, length
c = 0.7        # Nm/rad, damping coefficient
I = m*(l/2)**2    # moment of inertia

wn = (m*g*l/(2*I))**0.5  # un damped natural frequency in rad/s
xi = c/(2*I*wn)          # damping coefficient


def pid_plant(p, i=0, d=0):
    p = lti(
        [d, p, i],
        [1, (2*xi*wn+d), (wn**2 + p), i]
    )

    t = numpy.linspace(0, 15, 1000)
    _, y = step2(p, T=t)
    return t, y

if __name__ == '__main__':
    from matplotlib import pyplot as plt
    plt.plot(*pid_plant(10))
    plt.show()

