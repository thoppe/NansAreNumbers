import pytest
from nans_are_numbers import NAN

_x =  0.9026374256857772
_y = -0.17507582380505715

def test_addition():
    """
    Add two numbers together as floats then as NANs and check equality.
    """
    assert _x + _y == float(NAN(_x) + NAN(_y))
    
