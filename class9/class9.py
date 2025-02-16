# #List is a DATA STRUCTURE

# colors = ["yellow", "blue", "black"]
#         #     0   ,    1   ,   2

# #print(colors[0])
#Dictionaries is a DATA STRUCTURE

# # Keys : Values
# people = {
#     "Dennis" : "USA",
#     "Sameed" : "UAE",
#     "Ali"    : "Bangaladesh",
# }

# print(people["Ali"])

student = {
    "name" : "Alice",
    "age"  : 14,
    "grade": "9th",
    "city" : "Dubai",
    "country" : "UAE",
    "number" : "8309275948759"
}

# print(student["name"])
# # Alternate approach
# print(student.get("name"), "name not found")

# if "number" in student:
#     print("key exists")
# else:
#     print("key not found!")


# for key in student:
#     print(key , ": ", student[key])

# # Alternative Approach
# for key, value in student.items():
#     print(f"{key}: {value}")


# colors = ["yellow", "blue"]

# for color in colors:
#     print(color)


scores = {
    "Sameed" : 10,
    "Dennis" : 20,
    "Ali"    : 34,
    "Alex"   : 81,
    "Xam"    : 90,
}

# Output: Alex, Xam

employees = {
    "Sam" : 30000,
    "Jake" : 45000,
    "Ben"  : 50000,
}

# Update Jakes salary to 60000

# s = "hello world"
# char_count = {}

# for char in s:
#     char_count[char] = char_count.get(char, 0) + 1

# print(char_count)
#Output {h: None, e: None}

# people = ["Alex", "Ben", "John"]  #Keys
# favourite_colors = ["Red", "Purple", "Brown"] #Values


employees = {
    "Sam" : 30000,
    "Jake" : 45000,
    "Ben"  : 50000,
}

xyz = {
    "Alex" : "Red",
    "Ben"  : "Purple",
    "John" : "Brown"
}

# employees.update(xyz)
# print(employees)

# merged_dict = {**employees , **xyz}
# print(merged_dict)

# keys = ["Alex", "Ben", "John"]
# values = ["Red", "Purple", "Brown"] 

# dictionary = dict(zip(keys, values))

# print(dictionary)

