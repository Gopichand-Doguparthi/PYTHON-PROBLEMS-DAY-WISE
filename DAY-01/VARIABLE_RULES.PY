# Rules for variable names:
#
# 1. Variable name should not start with a digit.
# 2. Variable name can start with a letter or underscore.
# 3. Special characters are not allowed.
# 4. Spaces are not allowed.
# 5. Python keywords cannot be used as variable names.

student_name = "Gopi"
_age = 22
college1 = "ABC"

print(student_name)
print(_age)
print(college1)

# ------------------------------------------------------------

number = 100

print(number)

del number

# number is deleted here.
# print(number) would give NameError.


# ------------------------------------------------------------
#Swap_variables
# ------------------------------------------------------------

a = 10
b = 20

print("Before swapping:", a, b)

a, b = b, a

print("After swapping:", a, b)


# ------------------------------------------------------------
#comments_indentation
# ------------------------------------------------------------

# This is a single-line comment.

"""
This is a
multi-line string.
"""

x = 10

if x > 5:
    print("x is greater than 5")

print("Program completed")

