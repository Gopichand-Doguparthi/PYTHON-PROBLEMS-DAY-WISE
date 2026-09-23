# Strings in Python

# Different ways to define a string in Python

s1 = "helloWorld"

s2 = 'helloworld'

s3 = '''Multi
line
string'''

s4 = """multi
line
string"""

print(s1, type(s1))
print(s2)
print(s3)
print(s4, type(s4))


# Basic interview Question:
# String is Mutable or Immutable?
# Answer: String is IMMUTABLE

# Mutable:
# insert, delete and update operations can be performed

# Immutable:
# insert, delete and update operations CANNOT be performed


x1 = "Helloworld"

# x1[0] = 'a'


# Operations on strings

# 1. Concatenation (+)

str1 = "Babai "
str2 = "likes "
str3 = "Pinni"

str4 = str1 + str2 + str3

print(str4)


# 2. Repetition (*)

str6 = "bla "

print(10 * str6)


# 3. Membership (in, not in)

str7 = "Hello World"

print("Hell" in str7)
print("Helll" in str7)
print("o W" in str7)
print("Helo" not in str7)


# len()

len(str7)


# 4. Indexing & Slicing

# string[start:end:step]
# start = 0
# end = n-1
# step = 1

Heroine = "Samantha"

print(Heroine[4])
print(Heroine[-6])

print(Heroine[0:5])
print(Heroine[0:5:3])
print(Heroine[::])

print(Heroine[7:1:1])

print(Heroine[6:3:-1])

print(Heroine[-1])
print(Heroine[-6])

print(Heroine[-1:-6])

print(Heroine[-1:-6:-1])

print(Heroine[-7::])

print(Heroine[0:2:1] + Heroine[5::1])

print(Heroine[::-1])


# Reverse the string

Heroine = "Samantha"

rev_result = ""

for char in Heroine:
    rev_result = char + rev_result

print(rev_result)