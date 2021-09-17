from nans_are_numbers import NAN
import math

# Static random floating point numbers for tests
x = 0.9026374256857772
y = -0.17507582380505715


def test_NAN_from_int():
    """
    Create NAN from a int. Check that it evaluates to the float rep.
    """
    z = 17
    assert float(z) == float(NAN(z))


def test_NAN_to_int():
    """
    Cast a NAN to an int. Check that it evaluates to the correct number
    """
    z = -1.3
    assert int(z) == int(NAN(z))


def test_NAN1():
    """
    Create a NAN, one level deep.

    Check that it evaluates to the same float and fails when floats differ.
    Check that it is made up of NaNs.

    """
    q = NAN(x)

    assert x == float(q)
    assert y != float(q)

    assert all(math.isnan(z) for z in q)


def test_NAN2():
    """
    Create a NAN, two levels deep.

    Check that it evaluates to the same float and fails when floats differ.
    Check that it is made up of lists of NaNs.
    """
    q = NAN(NAN(x))

    assert x == float(q)
    assert y != float(q)

    assert all(isinstance(z1, list) for z1 in q)
    assert all(all(math.isnan(z0) for z0 in z1) for z1 in q)


def test_NAN2_bitmask():
    """
    Check that a NAN2 and NAN have the same bitmask, and different if
    base representation is different.
    """
    assert NAN(x).bitmask == NAN(NAN(x)).bitmask
    assert NAN(y).bitmask != NAN(NAN(x)).bitmask


def test_NAN3():
    """
    Create a NAN, three levels deep.

    Check that it evaluates to the same float and fails when floats differ.
    Check that it is made up of lists of lists of NaNs.
    """
    q = NAN(NAN(NAN(x)))

    assert x == float(q)
    assert y != float(q)

    assert all(isinstance(z2, list) for z2 in q)
    assert all(all(isinstance(z1, list) for z1 in z2) for z2 in q)
    assert all(all(all(math.isnan(z0) for z0 in z1) for z1 in z2) for z2 in q)
