# Sets

# Empty set
a = set()
print(a)

# {} creates an empty dictionary, not a set
a = {}
print(type(a))

# Set with values
a = {10, 20, 30, 40}
print(a)

# Duplicate values are automatically removed
a = {10, 20, 20, 30, 30, 40}
print(a)

# Different data types
a = {10, 20.5, "Python", True}
print(a)

# Set using set()
a = set([10, 20, 30, 40])
print(a)

# Frozenset
a = frozenset([10, 20, 30, 40])
print(a)

# Tuple can be stored inside a set
a = {(10, 20), 30, 40}
print(a)

# Frozenset can be stored inside a set
a = {frozenset([10, 20]), 30, 40}
print(a)