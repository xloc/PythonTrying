import numpy as np

a = np.arange(12).reshape((3,-1))

print a

# print (20,)*4
appending3 = [[20,20,20]]
appending4 = [[20,20,20,20]]

a = np.append(a, appending4, axis=0)

print a