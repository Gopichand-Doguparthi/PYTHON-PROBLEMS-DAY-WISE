# ------------------------------------------------------------
# logical_operators
# ------------------------------------------------------------

a = 10
b = 20

print(a < b and b > 10)
print(a > b or b > 10)
print(not(a > b))


# ------------------------------------------------------------
# bitwise_operators
# ------------------------------------------------------------

a = 10
b = 3

print("AND:", a & b)
print("OR:", a | b)
print("XOR:", a ^ b)
print("Left Shift:", a << 1)
print("Right Shift:", a >> 1)


# ------------------------------------------------------------
#identity_operators
# ------------------------------------------------------------

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)
print(a is c)
print(a is not c)


# ------------------------------------------------------------
# membership_operators
# ------------------------------------------------------------

numbers = [10, 20, 30, 40]

print(20 in numbers)
print(50 in numbers)
print(20 not in numbers)

text = "Python"

print("P" in text)
print("z" in text)