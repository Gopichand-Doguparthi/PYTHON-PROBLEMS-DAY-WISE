# for loop

animals = ["Puli", "Pili", "Kukka", "Pandi", "Kothi"]

for i in animals:
    print(i)


food_name = "Chickan_Dum_Masala_Biryani"

for i in food_name:
    print(i)


# for loop with range()

# range() function is used to generate values
# syntax: range(start, end, step)
# start = 0
# end = end - 1
# step = 1

for i in range(10):
    print(i)


# for loop with range()

for i in range(4, 10):
    print(i)


# for loop with range()

for i in range(4, 10, 3):
    print(i)


# Example-4: break statement
# break statement will bring the control out of the loop

for num in range(1, 6):

    if num == 3:
        break

    print(num)


# Example-5: continue statement
# continue statement takes the control to the start of the loop

for num in range(1, 6):

    if num == 3:
        continue

    print(num)


# Example-6 : nested loop
# for every value of outer loop, inner loop will completely execute

for i in range(3, 6):

    for j in range(2, 7):
        print(i, j)


# Example-7 : else statement
# else statement executes if loop completes execution successfully

for i in range(5):

    if i == 2:
        continue

    elif i == 40:
        break

    else:
        print(i)

else:
    print("loop completed successfully")


# Example-9 : Pattern

# Pattern-1

for j in range(5):

    for i in range(5):
        print("*", end=" ")

    print()


# Pattern-2

for j in range(1, 6):

    for i in range(j):
        print("*", end=" ")

    print()


# Pattern-3

for j in range(5, 0, -1):

    for i in range(j):
        print("*", end=" ")

    print()


# Pattern-4

n = 5

for i in range(n, 0, -1):
    print(" " * i + "* " * (n - i + 1))