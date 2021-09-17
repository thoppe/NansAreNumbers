# NaNsAreNumbers
An esoteric data type built entirely of NaNs.

Underneath all floating point number is a collection of bits, 1s and 0s. For example, the number -20.22 as a 64-bit number looks like

    1100000000110100001101011100001010001111010111000010100011110110

The first bit tells us if it's positive or negative and the rest of the bits give the representation. Even things that aren't numbers like positive or negative infinity or NaNs are represented by special sequences of bits:

    0111111111111000000000000000000000000000000000000000000000000000
    1111111111110000000000000000000000000000000000000000000000000000
    0111111111110000000000000000000000000000000000000000000000000000

Those things called [NaNs](https://en.wikipedia.org/wiki/NaN) (short for Not A Number) are used as a value that is undefined or unrepresentable.

But guess what?! You can have POSTIVE and NEGATIVE NaNs! It's all a matter of changing the sign bit, the [IEEE 754](https://en.wikipedia.org/wiki/IEEE_754) specification for NaNs does not check against the first bit. This is great news, since we can map the mapping:

    -math.nan -> 1
     math.nan -> 0

A thus we can create a new data type that acts like a float but it is built entirly of NaNs. Let's call it NAN (NaNs Are Numbers):


``` python

from nans_are_numbers

x, y = NAN(-1.3), NAN(9.7)
print(x == -1.3)  # True
print(float(x))   # -1.3
print(x)

# [nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan]
```


Depth, Size in bytes
1 1840
2 58040
3 3,680,488
4 235,471,960 