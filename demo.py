from nans_are_numbers import NAN
from pympler import asizeof

x0, x1 = 1.3, 9.7

q1, p1 = NAN(x0), NAN(x1)


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

q4, p4 = NAN(q3), NAN(p3)
print(q4.bitmask, len(str(q4)))
print(float(q4))
print(float(q4 + p4))
print(asizeof.asized(q4).size)
print(float(q4 * p4))
print(float(q4 - p4))
