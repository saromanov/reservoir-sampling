import numpy as np

def reservoir_sampling(data, size, iters=1):
    result = []
    n = 0
    for it in range(iters):
        tmp = []
        for item in data:
            n += 1
            if len(tmp) < size:
                tmp.append(item)
            else:
                r = np.random.randint(0, n)
                if r < size: tmp[r] = item
        result.append(tmp)
    return result