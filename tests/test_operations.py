from nans_are_numbers import NAN

# Static random floating point numbers for tests
x = 0.9026374256857772
y = -0.17507582380505715


def test_str():
    """
    Check string representation represents at 64 nan strings
    """
    assert str(NAN(x)).count("nan") == 64


def test_round():
    """
    Tests rounding value of floats vs a NANs and check equality.
    """
    assert round(x, 3) == round(NAN(x), 3)


def test_eq():
    """
    Tests __eq__ of float vs a NANs (without casting) and check equality.
    """
    assert x == NAN(x)


def test_abs():
    """
    Tests absolute value of floats vs a NANs and check equality.
    """
    assert abs(x) == abs(NAN(x))


def test_neg():
    """
    Tests __neg__ of a float vs a NANs and check equality.
    """
    assert (-x) == (-NAN(x))


def test_pos():
    """
    Tests __pos__ of a float vs a NANs and check equality.
    """
    assert (+x) == (+NAN(x))


def test_add():
    """
    Add two numbers together as floats then as NANs and check equality.
    """
    assert x + y == (NAN(x) + NAN(y))
    assert x + y == (x + NAN(y))


def test_sub():
    """
    Subtract two numbers together as floats then as NANs and check equality.
    """
    assert x - y == (NAN(x) - NAN(y))
    assert x - y == (x - NAN(y))


def test_div():
    """
    Divide two numbers together as floats then as NANs and check equality.
    """
    assert x / y == (NAN(x) / NAN(y))
    assert x / y == (x / NAN(y))


def test_floordiv():
    """
    Flor divide two numbers together as floats then as NANs and check equality.
    """
    assert x // y == (NAN(x) // NAN(y))
    assert x // y == (x // NAN(y))


def test_mul():
    """
    Multiply two numbers together as floats then as NANs and check equality.
    """
    assert x * y == (NAN(x) * NAN(y))
    assert x * y == (x * NAN(y))


def test_pow():
    """
    Exp two numbers together as floats then as NANs and check equality.
    """
    assert x ** y == (NAN(x) ** NAN(y))
    assert x ** y == (x ** NAN(y))


def test_mod():
    """
    Mod two numbers together as floats then as NANs and check equality.
    """
    assert x % y == (NAN(x) % NAN(y))
    assert x % y == (x % NAN(y))


def test_less_than():
    """
    Test less than and less than equal to as floats and as NANs
    """
    assert (x < y) == (NAN(x) < NAN(y))
    assert (x <= y) == (NAN(x) <= NAN(y))
    assert (x <= x) == (NAN(x) <= NAN(x))


def test_greater_than():
    """
    Test greater than and less than equal to as floats and as NANs
    """
    assert (x > y) == (NAN(x) > NAN(y))
    assert (x >= y) == (NAN(x) >= NAN(y))
    assert (x >= x) == (NAN(x) >= NAN(x))
