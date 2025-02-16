# Counting
count = 0
for _ in range(10):
    number = int(input("Enter a number: "))
    if number < 0:
        count = count + 1

print(count)
