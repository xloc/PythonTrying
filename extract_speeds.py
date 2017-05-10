import json
import numpy as np

with open('./test_rec.json') as f:
    j = json.load(f)
    a = []
    for d in j:
        a.append(d['speeds'])

a = np.array(a)
print a.T[0:2]