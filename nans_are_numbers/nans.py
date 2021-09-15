import math
from .core_float_utils import float_to_binary_list, bin_to_float

# https://docs.python.org/3.3/reference/datamodel.html#object.__truediv__

# Representation of a NaN as a list of 0s and 1s, since the sign bit marks
# a 0, we have pos NaN == -math.nan
_POS_NAN_BITS = float_to_binary_list(-math.nan)
_NEG_NAN_BITS = float_to_binary_list(math.nan)


class NAN:
    def __init__(self, x, create_from=None):

        # Keep a record of our parent for recursive creation
        if create_from:
            self.parent = create_from.parent
        else:
            self.parent = x

        # Check if the parent is a float
        self.base_NAN = isinstance(self.parent, float)

        if isinstance(x, float):
            bitmask = float_to_binary_list(x)
        else:
            bitmask = x.bitmask

        self.rep = [self.get_parent_nans()[bit] for bit in bitmask]

    def ultimate_bit(self, x):
        if isinstance(x, float):
            return int(float_to_binary_list(x) == _POS_NAN_BITS)

        return int([self.ultimate_bit(y) for y in x] == _NEG_NAN_BITS)

    @property
    def bitmask(self):
        """
        Recursively hop down each "bit" in the representation and resolve
        if it ultimately represents a +NaN or -NaN.
        """
        return [self.ultimate_bit(x) for x in self.rep]

    def __float__(self):
        return bin_to_float("".join(map(str, self.bitmask)))

    def __repr__(self):
        # return f"[{len(self.rep)}:{type(self.rep[0])}{self.depth}]"
        return str(self.rep)

    def get_parent_nans(self):
        if self.base_NAN:
            return math.nan, -math.nan
        else:
            return self.parent.get_pos_nan(), self.parent.get_neg_nan()

    def get_pos_nan(self):
        # Returns a positive NAN (or NaN) using the parent
        return [self.get_parent_nans()[bit] for bit in _POS_NAN_BITS]

    def get_neg_nan(self):
        # Returns a negative NAN (or NaN) using the parent
        return [self.get_parent_nans()[bit] for bit in _NEG_NAN_BITS]

    def cast_down_compute_cast_up(func):
        """
        Voodoo magic here. Take the objects (however deeply nested)
        convert them into floats, gather the same-named function from
        the float library (eg. __add__), apply the function, then recast
        the result back into a NAN of complexity of the first input.

        Works for unary (__neg__), binary (__add__), and ternary (__pow__)
        """

        def cast(*args):
            float_func = getattr(float, func.__name__)
            result = float_func(*map(float, args))
            return NAN(result, create_from=args[0])

        return cast

    @cast_down_compute_cast_up
    def __pos__(self, x):
        pass

    @cast_down_compute_cast_up
    def __neg__(self, x):
        pass

    @cast_down_compute_cast_up
    def __abs__(self, x):
        pass

    @cast_down_compute_cast_up
    def __invert__(self, x):
        pass

    @cast_down_compute_cast_up
    def __add__(self, x):
        pass

    @cast_down_compute_cast_up
    def __radd__(self, x):
        pass

    @cast_down_compute_cast_up
    def __sub__(self, x):
        pass

    @cast_down_compute_cast_up
    def __rsub__(self, x):
        pass

    @cast_down_compute_cast_up
    def __mul__(self, x):
        pass

    @cast_down_compute_cast_up
    def __rmul__(self, x):
        pass

    @cast_down_compute_cast_up
    def __truediv__(self, x):
        pass

    @cast_down_compute_cast_up
    def __rtruediv__(self, x):
        pass

    @cast_down_compute_cast_up
    def __floordiv__(self, x):
        pass

    @cast_down_compute_cast_up
    def __rfloordiv__(self, x):
        pass

    @cast_down_compute_cast_up
    def __pow__(self, x):
        pass

    @cast_down_compute_cast_up
    def __rpow__(self, x):
        pass

    @cast_down_compute_cast_up
    def __divmod__(self, x):
        pass

    @cast_down_compute_cast_up
    def __rdivmod__(self, x):
        pass

    @cast_down_compute_cast_up
    def __mod__(self, x):
        pass

    @cast_down_compute_cast_up
    def __rmod__(self, x):
        pass

    @cast_down_compute_cast_up
    def __lshift__(self, x):
        pass

    @cast_down_compute_cast_up
    def __rlshift__(self, x):
        pass

    @cast_down_compute_cast_up
    def __rshift__(self, x):
        pass

    @cast_down_compute_cast_up
    def __rrshift__(self, x):
        pass

    @cast_down_compute_cast_up
    def __and__(self, x):
        pass

    @cast_down_compute_cast_up
    def __rand__(self, x):
        pass

    @cast_down_compute_cast_up
    def __xor__(self, x):
        pass

    @cast_down_compute_cast_up
    def __rxor__(self, x):
        pass

    @cast_down_compute_cast_up
    def __or__(self, x):
        pass

    @cast_down_compute_cast_up
    def __ror__(self, x):
        pass
