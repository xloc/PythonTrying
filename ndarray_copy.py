import copy
import numpy as np

# Without copy
template = np.arange(1, 10)
a = template

a[2:7] = np.zeros(5)

print np.all(a == template)


# Copy by numpy copy
template = np.arange(1, 10)
b = np.copy(template)

b[2:7] = np.zeros(5)

print np.all(b == template)

# Copy by build-in module copy
template = np.arange(1, 10)
c = copy.copy(template)

c[2:7] = np.zeros(5)

print np.all(c == template)