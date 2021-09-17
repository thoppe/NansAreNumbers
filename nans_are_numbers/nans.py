import math
from .core_float_utils import float_to_binary_list, bin_to_float

# https://docs.python.org/3.3/reference/datamodel.html#object.__truediv__

# Representation of a NaN as a list of 0s and 1s, since the sign bit marks
# a 0, we have pos NaN == -math.nan
_POS_NAN_BITS = float_to_binary_list(-math.nan)
_NEG_NAN_BITS = float_to_binary_list(math.nan)


class NAN:
    def __init__(self, x, create_from=None):

        if isinstance(x, int):
            x = float(x)

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

    def __int__(self):
        return int(float(self))

    def __repr__(self):
        return str(self.rep)

    def __iter__(self):
        yield from self.rep

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

            # Call the main function for side effects (and tests!)
            null_result = func(*args)  # noqa: F841

            float_func = getattr(float, func.__name__)

            # Round *requires* the second argument to be an int
            if func.__name__ == "__round__":
                result = float_func(float(args[0]), args[1])
            else:
                result = float_func(*map(float, args))

            # Functions like __le__ return different types
            # (eg. bool or int). If not a float, return it directly
            if not isinstance(result, float):
                return result

            # Otherwise return the result as the object itself
            return NAN(result, create_from=args[0])

        return cast

    @cast_down_compute_cast_up
    def __eq__(*args):
        pass

    @cast_down_compute_cast_up
    def __pos__(*args):
        pass

    @cast_down_compute_cast_up
    def __neg__(*args):
        pass

    @cast_down_compute_cast_up
    def __abs__(*args):
        pass

    @cast_down_compute_cast_up
    def __round__(*args):
        pass

    @cast_down_compute_cast_up
    def __add__(*args):
        pass

    @cast_down_compute_cast_up
    def __radd__(*args):
        pass

    @cast_down_compute_cast_up
    def __sub__(*args):
        pass

    @cast_down_compute_cast_up
    def __rsub__(*args):
        pass

    @cast_down_compute_cast_up
    def __mul__(*args):
        pass

    @cast_down_compute_cast_up
    def __rmul__(*args):
        pass

    @cast_down_compute_cast_up
    def __truediv__(*args):
        pass

    @cast_down_compute_cast_up
    def __rtruediv__(*args):
        pass

    @cast_down_compute_cast_up
    def __floordiv__(*args):
        pass

    @cast_down_compute_cast_up
    def __rfloordiv__(*args):
        pass

    @cast_down_compute_cast_up
    def __pow__(*args):
        pass

    @cast_down_compute_cast_up
    def __rpow__(*args):
        pass

    @cast_down_compute_cast_up
    def __mod__(*args):
        pass

    @cast_down_compute_cast_up
    def __rmod__(*args):
        pass

    @cast_down_compute_cast_up
    def __lt__(*args):
        pass

    @cast_down_compute_cast_up
    def __le__(*args):
        pass

    @cast_down_compute_cast_up
    def __gt__(*args):
        pass

    @cast_down_compute_cast_up
    def __ge__(*args):
        pass

    """
    Divmod is not supported. Add it yourself.
    """
