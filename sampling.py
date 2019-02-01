import numpy as np

def reservoir_sampling(size, count=100):
    result = []
    for i in range(1, count):
        r = np.random.randint(0, i)
        if len(result) < size:
            result.append(r)
            continue
        elif r < size:
            result[r] = result[i]