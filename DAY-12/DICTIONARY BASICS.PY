# Dictionary

# Creating dictionary
a = {
    "name": "Gopi",
    "age": 22,
    "city": "Hyderabad"
}

print(a)


# Using dict()
a = dict(name="Gopi", age=22, city="Hyderabad")
print(a)


# Different key types

a = {
    1: "one",
    2.5: "two point five",
    "three": 3,
    (4, 5): "tuple"
}

print(a)


# Dictionary keys must be immutable

a = {
    "name": "Gopi",
    "age": 22
}

print(a)


# Values can be mutable

a = {
    "name": "Gopi",
    "skills": ["Python", "SQL", "HTML"]
}

print(a)


# Duplicate keys
a = {
    "name": "Gopi",
    "name": "Ravi"
}

print(a)


# Dictionary comprehension

a = {x: x * x for x in range(1, 6)}
print(a)