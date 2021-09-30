from nans_are_numbers import NAN
import math
from hypothesis import given, strategies as st, settings
import pytest



@given(st.integers())
def test_NAN_from_int(z):
    """
    Create NAN from a int. Check that it evaluates to the float rep.
    """
    assert z == NAN(z)


@given(st.floats(allow_infinity=False))
def test_NAN_to_int(z):
    """
    Cast a NAN to an int. Check that it evaluates to the correct number
    """
    if math.isnan(z):
        with pytest.raises(ValueError):
            int(NAN(z))
    else:
        assert int(z) == int(NAN(z))


@given(st.floats())
def test_NAN1(x):
    """
    Create a NAN, one level deep.

    Check that it evaluates to the same float.
    Check that it is made up of NaNs.

    """
    q = NAN(x)

    if math.isnan(x):
        assert math.isnan(q)
    else:
         assert x == q

    assert all(math.isnan(z) for z in q)


@given(st.floats())
def test_NAN2(x):
    """
    Create a NAN, two levels deep.

    Check that it evaluates to the same float.
    Check that it is made up of lists of NaNs.
    """
    q = NAN(NAN(x))

    if math.isnan(x):
        assert math.isnan(q)
    else:
         assert x == q

    assert all(isinstance(z1, list) for z1 in q)
    assert all(all(math.isnan(z0) for z0 in z1) for z1 in q)


@given(st.floats())
def test_NAN2_bitmask(x):
    """
    Check that a NAN2 and NAN have the same bitmask, and different if
    base representation is different.
    """
    assert NAN(x).bitmask == NAN(NAN(x)).bitmask

@pytest.mark.slow
@given(st.floats())
@settings(deadline=500.0)
def test_NAN3(x):
    """
    Create a NAN, three levels deep.

    Check that it evaluates to the same float.
    Check that it is made up of lists of lists of NaNs.
    """

    q = NAN(NAN(NAN(x)))

    if math.isnan(x):
        assert math.isnan(q)
    else:
         assert x == q

    assert all(isinstance(z2, list) for z2 in q)
    assert all(all(isinstance(z1, list) for z1 in z2) for z2 in q)
    assert all(all(all(math.isnan(z0) for z0 in z1) for z1 in z2) for z2 in q)
