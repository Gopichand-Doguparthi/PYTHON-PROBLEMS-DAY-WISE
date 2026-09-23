# Data structures
# List data structure

l1 = [10, 10, 10, 10, 20.5, "Hello", True]

print(l1[5])


# Creating different types of list

empty_list = []

empty_list2 = list()

print(empty_list, type(empty_list))
print(empty_list2, type(empty_list2))


Het_list = [10, 20.5, "Hello", True]

print(Het_list)


dup_list = [10, 10, 10, 20, 30]

print(dup_list)


# Nested list

nested_list = [[1, 2], [10, 20], ["Hello", "World"], 1000]

print(nested_list)

len(nested_list)

nested_list[1][0]


# Concatenating lists

concat_list = Het_list + dup_list + nested_list

print(concat_list)


# Accessing list items

Hours_study = [1, 5, 4, 2, 3, 4, 2, 3, 1.5, 2, 2, 3, 20, 24]

Hours_study[1]


# Updating list items

list_politician = [
    "Vijay",
    "CBN",
    "Pavan",
    "JaiLalita",
    "Balayya",
    "Anushka"
]


# Update single element

list_politician[1] = "Dance with"

print(list_politician)


# Update multiple elements: update more elements with less

list_politician[3:5] = ["Dance with"]

print(list_politician)


# Update less elements with more

list_politician[1:4] = [
    "Rahul",
    "Kejriwal",
    "Yogi",
    "Mamta"
]

print(list_politician)


list_politician[-2] = "Dance with"

print(list_politician)


list_politician[-5:-1] = ["Dance with"]

print(list_politician)


# Insert items in list
# append(), extend(), insert()

l2 = []


# append()
# append() is used to insert a single element at the last of the list

l2.append(10)
print(l2)

l2.append(20)
print(l2)

l2.append(30)
print(l2)


# extend()
# extend() is used to insert multiple elements at the end

l2.extend([40, 50, 60, 70, 80])

print(l2)


# insert()
# insert() can be used to insert at a specific index

l2.insert(4, "Dinesh")

print(l2)

l2.insert(5, [10, 20, 30])

print(l2)


# Delete item from list
# remove(), pop(), clear(), del

food_list = [
    "Papu",
    "Biryani",
    "fried rice",
    "Sambar",
    "Payasum",
    "Curd rice"
]


# remove()
# remove() deletes the item with given value

food_list.remove("fried rice")

print(food_list)


# pop()
# pop() is used to delete the item from a particular index

food_list.pop(4)

print(food_list)


# pop() without index deletes the last element

food_list.pop()

print(food_list)


food_list = [
    "Papu",
    "Biryani",
    "fried rice",
    "Sambar",
    "Payasum",
    "Curd rice"
]


# del
# Delete multiple elements together

del food_list[1:4]

print(food_list)


# clear()
# clear() is used to delete all the items from the list

food_list.clear()

print(food_list)


# del
# Delete the list itself

del food_list


# Popular list inbuilt functions

Age_list = [22, 23, 22, 20, 19, 18, 21, 16, 19, 20, 99]

print(len(Age_list))
print(min(Age_list))
print(max(Age_list))
print(sum(Age_list))

Age_list.reverse()

print(Age_list)


# In Python sort() function uses Tim Sort
# Tim Sort = Merge Sort + Insertion Sort
# Time complexity = O(n log n)

Age_list.sort()

print(Age_list)

Age_list.sort(reverse=True)

print(Age_list)


# list()
# Convert tuple to list

t1 = (10, 20, 30, 40, 50)

s1 = {60, 70, 80, 90}

l2 = list(t1)

l3 = list(s1)

value = range(1, 10)

l4 = list(value)

print(l2)
print(l3)
print(l4)


l5 = list(input("Enter all your X names").split())

print(l5)


# List comprehension
# Creating the list in a single line using a loop

l1 = [i for i in range(1, 11)]

print(l1)


l2 = [i**2 for i in range(1, 11)]

print(l2)


l3 = [i for i in range(1, 11) if i % 2 == 0]

print(l3)


l3 = [
    i
    for i in range(1, 11)
    if i % 2 == 0
    if i % 3 == 0
]

print(l3)


l4 = [
    i**2 if i % 2 == 0 else i + 2
    for i in range(1, 11)
]

print(l4)


l4 = [
    i**2 if i % 2 == 0 else i + 2
    for i in range(1, 11)
    if i > 5 and i < 9
]

print(l4)


# Nested list comprehension

l6 = [
    [i for i in range(1, 5)]
    for j in range(1, 3)
]

print(l6)


l6 = [
    [
        [i for i in range(1, 5)]
        for j in range(1, 3)
    ]
    for k in range(1, 3)
]

print(l6)