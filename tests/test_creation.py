from nans_are_numbers import NAN

# Static random floating point numbers for tests
x = 0.9026374256857772
y = -0.17507582380505715


def test_NAN_from_int():
    """
    Create NAN from a int. Check that it evaluates to the float rep.
    """
    z = 17
    assert float(z) == float(NAN(z))


def test_NAN1():
    """
    Create a NAN, one level deep. Check that it evaluates to the float.
    """
    assert x == float(NAN(x))


def test_NAN2():
    """
    Create a NAN, two levels deep. Check that it evaluates to the float.
    """
    assert x == float(NAN(NAN(x)))


def test_NAN3():
    """
    Create a NAN, three levels deep. Check that it evaluates to the float.
    """
    assert x == float(NAN(NAN(x)))
