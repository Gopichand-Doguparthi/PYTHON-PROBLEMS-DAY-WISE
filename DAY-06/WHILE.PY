# while loop

# Example-1

i = 1

while i <= 10:
    print(i)
    i += 1

print(i)


# Example-1

i = 1

while i <= 10:
    i += 1
    print(i)


# Example-2 : break statement
# break statement helps to come out of the loop

i = 1

while i <= 10:
    print(i)

    if i == 5:
        break

    i += 1


i = 1

while i <= 10:
    i += 1
    print(i)

    if i == 5:
        break


# Example-3 : continue statement
# continue will take the control to the start of the loop
# if continue will execute then further statements will not execute

i = 1

while i < 10:
    i += 1

    if i < 5:
        continue

    print(i)


i = 1

while i < 10:

    if i < 5:
        continue

    i += 1
    print(i)


i = 1

while i < 10:
    i += 1

    if i < 5:
        continue

    if i > 8:
        break

    print(i)


# Example-4 : else statement with while loop
# else statement executes only if loop is successfully completed

i = 1

while i <= 10:
    print(i)
    i += 1

    if i > 5:
        break

else:
    print("loop is successfully completed")


# Example-5 : pass statement
# pass statement is a placeholder for future code

i = 0

while i <= 10:

    if i == 5:
        pass

    else:
        print(i)

    i += 1


# Chocolate question

i = 10

while i >= 1:
    i -= 1

    if i > 4 and i < 8:
        continue

    elif i < 2:
        break

    pass

    print(i)

else:
    print("go to hell")