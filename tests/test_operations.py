from nans_are_numbers import NAN
from hypothesis import given, strategies as st
import pytest

@given(st.floats())
def test_str(x):
    """
    Check string representation represents at 64 nan strings
    """
    assert str(NAN(x)).count("nan") == 64


@given(st.floats())
def test_round(x):
    """
    Tests rounding value of floats vs a NANs and check equality.
    """
    assert round(x, 3) == round(NAN(x), 3)


@given(st.floats())
def test_eq(x):
    """
    Tests __eq__ of float vs a NANs (without casting) and check equality.
    """
    assert x == NAN(x)


@given(st.floats())
def test_abs(x):
    """
    Tests absolute value of floats vs a NANs and check equality.
    """
    assert abs(x) == abs(NAN(x))


@given(st.floats())
def test_neg(x):
    """
    Tests __neg__ of a float vs a NANs and check equality.
    """
    assert (-x) == (-NAN(x))


@given(st.floats())
def test_pos(x):
    """
    Tests __pos__ of a float vs a NANs and check equality.
    """
    assert (+x) == (+NAN(x))


@given(st.floats(), st.floats())
def test_add(x, y):
    """
    Add two numbers together as floats then as NANs and check equality.
    """
    assert x + y == (NAN(x) + NAN(y))
    assert x + y == (x + NAN(y))


@given(st.floats(), st.floats())
def test_sub(x, y):
    """
    Subtract two numbers together as floats then as NANs and check equality.
    """
    assert x - y == (NAN(x) - NAN(y))
    assert x - y == (x - NAN(y))


@given(st.floats(), st.floats())
def test_div(x, y):
    """
    Divide two numbers together as floats then as NANs and check equality.
    """
    if y == 0:
        with pytest.raises(ZeroDivisionError):
            NAN(x) / NAN(y)
    else:
        assert x / y == (NAN(x) / NAN(y))
        assert x / y == (x / NAN(y))


@given(st.floats(), st.floats())
def test_floordiv(x, y):
    """
    Floor divide two numbers together as floats then as NANs and check equality.
    """
    if y == 0:
        with pytest.raises(ZeroDivisionError):
            NAN(x) // NAN(y)
    else:
        assert x // y == (NAN(x) // NAN(y))
        assert x // y == (x // NAN(y))


@given(st.floats(), st.floats())
def test_mul(x, y):
    """
    Multiply two numbers together as floats then as NANs and check equality.
    """
    assert x * y == (NAN(x) * NAN(y))
    assert x * y == (x * NAN(y))


@given(st.floats(), st.floats())
def test_pow(x, y):
    """
    Exp two numbers together as floats then as NANs and check equality.
    """
    assert x ** y == (NAN(x) ** NAN(y))
    assert x ** y == (x ** NAN(y))


@given(st.floats(), st.floats())
def test_mod(x, y):
    """
    Mod two numbers together as floats then as NANs and check equality.
    """
    if y == 0:
        with pytest.raises(ZeroDivisionError):
             NAN(x) % NAN(y)
    else:
        assert x % y == (NAN(x) % NAN(y))
        assert x % y == (x % NAN(y))


@given(st.floats(), st.floats())
def test_less_than(x, y):
    """
    Test less than and less than equal to as floats and as NANs
    """
    assert (x < y) == (NAN(x) < NAN(y))
    assert (x <= y) == (NAN(x) <= NAN(y))
    assert (x <= x) == (NAN(x) <= NAN(x))


@given(st.floats(), st.floats())
def test_greater_than(x, y):
    """
    Test greater than and less than equal to as floats and as NANs
    """
    assert (x > y) == (NAN(x) > NAN(y))
    assert (x >= y) == (NAN(x) >= NAN(y))
    assert (x >= x) == (NAN(x) >= NAN(x))
