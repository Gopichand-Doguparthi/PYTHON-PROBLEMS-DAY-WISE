# Adding elements

a = {10, 20, 30}

# add()
a.add(40)

# update()
a.update([50, 60, 70])


# Removing elements

# remove()
a.remove(20)

# discard()
a.discard(30)

# pop()
a.pop()

# clear()
a.clear()

# del
a = {10, 20, 30}
del a


# Built-in functions

a = {10, 20, 30, 40}

print(len(a))
print(min(a))
print(max(a))
print(sum(a))
print(sorted(a))


# Membership operators

a = {10, 20, 30, 40}

print(20 in a)
print(50 in a)

print(20 not in a)
print(50 not in a)