# reservoir-sampling
[![Build Status](https://travis-ci.org/saromanov/reservoir-sampling.svg?branch=master)](https://travis-ci.org/saromanov/reservoir-sampling)

Implementation of reservoir sampling algorithm

## Example
```python
import reservoir

reservoir.sampling([5,4,2,5,9,6,3], 3, iters=3)
#[[5, 4, 2], [9, 4, 2], [5, 3, 2]]
```

Of course, each call will return different response

