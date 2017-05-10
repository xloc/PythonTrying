import numpy as np

#
# a = np.arange(9).reshape(3,3)
# print a
#
# print np.hsplit(a, 3)


data = np.arange(16).reshape((4, 4))

s = np.vsplit(data, 2)

print s
