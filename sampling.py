import numpy as np

def reservoir_sampling(data, size):
    result = []
    n = 0
    for item in data:
        n += 1
        if len(result) < size:
            result.append(item)
        else:
            r = np.random.randint(0, n)
            result[r] = item