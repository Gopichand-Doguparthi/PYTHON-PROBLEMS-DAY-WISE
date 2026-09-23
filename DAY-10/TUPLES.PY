# Tuple data structure

t1 = (10, 20.5, "Hello", 10, 10, 10)

print(t1[-2])


# Creating different types of tuples

empty_tuple = ()

empty_tuple2 = tuple()

print(empty_tuple, type(empty_tuple))
print(empty_tuple2, type(empty_tuple2))


het_tuple = (10, 10.5, "hello", True)

print(het_tuple)


dup_tuple = (10, 10, 10, 10, 20, 30)

print(dup_tuple)


nested_tuple = (
    (10, 20, 30),
    [40, 50],
    {60, 70, 80, 90},
    "Hello"
)

print(nested_tuple)


# Convert list and set to tuple using tuple()

list1 = [10, 20, 30, 40]

tuple1 = tuple(list1)

print(tuple1)


set1 = {10, 20, 30, 40}

tuple1 = tuple(set1)

print(tuple1)


values = range(1, 11)

tuple2 = tuple(values)

print(tuple2)

print(tuple(range(1, 11)))


# Tuple concatenation

t1 = (1, 2, 3)

t2 = (4, 5, 6)

t3 = (7, 8, 9)

t4 = t1 + t2 + t3

print(t4)


# Tuple comprehension using generator expression

t5 = tuple(i for i in range(10))

print(t5)


# Accessing tuple items

Veg_tuple = (
    "tomata",
    "Mirapakaya",
    "allugada",
    "Vankaya",
    "Bendakaya",
    "Sorakaya"
)

Veg_tuple[-1:0:-1]


# Insert, delete and update operations indirectly

tuple1 = (10, 20.5, "Hello", [10, 20, 30])

tuple1[3][2] = 5000

tuple1


# Tuple items cannot be updated directly
# Complete item in tuple cannot be updated directly
# But if item is mutable, elements inside this mutable item can be updated


# Insert

tuple3 = (10, 20, 30)

list1 = list(tuple3)

print(list1)

list1.extend([100, 200, 300])

print(list1)

tuple3 = tuple(list1)

print(tuple3)


# Delete

tuple3 = (10, 20, 30)

list1 = list(tuple3)

print(list1)

list1.remove(30)

print(list1)

tuple3 = tuple(list1)

print(tuple3)


# Update

tuple3 = (10, 20, 30)

list1 = list(tuple3)

print(list1)

list1[2] = 300000

print(list1)

tuple3 = tuple(list1)

print(tuple3)


# Popular inbuilt functions for tuple

Salary = (6, 70, 100, 600, 700, 90, 10, 80, 120)

print(tuple(reversed(Salary)))

print(len(Salary))

print(min(Salary))

print(max(Salary))

print(sum(Salary))


sorted_list = tuple(sorted(Salary, reverse=True))

print(sorted_list)


# sort() is an inplace function
# inplace means sorting is done in the same data structure

# sorted() function returns a list
# sort() function does not return anything


l1 = [34, 40, 50, 60, 1, 3, 4, 70]

l1.sort()

print(l1)