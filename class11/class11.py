# File Handling
# Allows reading from and writing to external files (e.g .txt, .csv)
# Useful for storing data permantly unlike variables (stored in RAM)
# Real life examples are.. highsores in games, login details, data storage, configuargation files

# file = open("example.txt", "r") # Open the file in read mode
# content = file.read() # Reads the entire File
# print(content)
# file.close() # Always close the file after reading


# file = open("example.txt", "w")
# file.write("Hi I am overwriting the file")
# # write is used to write
# file.close()

# file = open("example.txt", "a")
# file.write("\nHi I am appending the file")
# # write is used to write
# file.close()

# with open("example.txt" , "r") as file:
#     content = file.read()
#     print(content)

# "Hekllo"
# 'Hello'

# '''
# akdhiukfh
# afhjnkjhe
# '''

# count = 0
# file = open("example.txt" , "r")
# for line in file:
#     count = count + line.count("Python") + line.count("python")
# print(count)
# file.close()

file = open('example.txt' , 'w')
file.write('[1,2,3,4,5]')
file.close()

file = open('example.txt' , 'r')
numbers = file.read().strip("[").strip("]").split(",")
new_list = []
for n in numbers:
    new_list.append(int(n))
file.close()

sum = 0
for n in new_list:
    sum = sum + n
print(sum)