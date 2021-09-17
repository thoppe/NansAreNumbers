from nans_are_numbers import NAN
from pympler import asizeof
import math

x, y = NAN(-1.3), NAN(9.7)

print(x == -1.3)
print(x + 1)
print(float(x))

print(x.bitmask)

print(NAN(math.nan).bitmask)
print(NAN(-math.nan).bitmask)

q = NAN(math.inf)
print(''.join(map(str,q.bitmask)))

q = NAN(-math.inf)
print(''.join(map(str,q.bitmask)))

q = NAN(math.nan)
print(''.join(map(str,q.bitmask)))


q = NAN(-20.21)
print(''.join(map(str,q.bitmask)))

exit()


print(q1.bitmask, len(str(q1)))
print(type(q1.parent))
print(float(q1))
print(float(q1 + p1))
print(asizeof.asized(q1).size)
print(asizeof.asized(q1 + p1).size)
print(q1 + p1)
print()
print(float(q1 + 9.0))


q2, p2 = NAN(q1), NAN(p1)
print(q2.bitmask, len(str(q2)))
print(float(q2))
print(float(q2 + p2))
print(asizeof.asized(q2).size)
print(asizeof.asized(p2 + q2).size)

print(float(q2 - p2))
print(float(q2 / p2))
print(float(q2 ** p2))
print(float(-(q2 - p2)))

q3, p3 = NAN(q2), NAN(p2)
print(q3.bitmask, len(str(q3)))
print(float(q3))
print(float(q3 + p3))
print(asizeof.asized(q3).size)

exit()

q4, p4 = NAN(q3), NAN(p3)
print(q4.bitmask, len(str(q4)))
print(float(q4))
print(float(q4 + p4))
print(asizeof.asized(q4).size)
print(float(q4 * p4))
print(float(q4 - p4))
