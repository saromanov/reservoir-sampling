import pytest
import reservoir

def test_basic():
    result = reservoir.sampling([5,4,2,5,9,6,3], 3, iters=3)
    assert len(result) == 3