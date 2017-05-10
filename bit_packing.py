import numpy as np


nums = [7, 10, 0xaa]

nums = np.array([[num] for num in nums])

# print nums

bytes = np.unpackbits(nums.astype(np.uint8), axis=1)

print bytes