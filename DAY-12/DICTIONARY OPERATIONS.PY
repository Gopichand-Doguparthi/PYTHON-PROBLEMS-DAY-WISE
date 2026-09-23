# Accessing dictionary values

student = {
    "name": "Gopi",
    "age": 22,
    "city": "Hyderabad"
}

# Using []
print(student["name"])
print(student["age"])


# Using get()
print(student.get("name"))
print(student.get("age"))


# Iterating keys
for key in student:
    print(key)


# Iterating values
for value in student.values():
    print(value)


# keys()
print(student.keys())


# values()
print(student.values())


# items()
print(student.items())


# Iterating key and value
for key, value in student.items():
    print(key, value)


# Nested dictionary

students = {
    "student1": {
        "name": "Gopi",
        "age": 22
    },

    "student2": {
        "name": "Ravi",
        "age": 23
    }
}

print(students)
print(students["student1"])
print(students["student1"]["name"])