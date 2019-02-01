import numpy as np

def reservoir_sampling(size):
    result = []
    i = 0
    while True:
        i+=1
        r = np.random.randint(0, i)
        if len(result) < size:
            result.append(r)
        if r < size:
            result[r] = item