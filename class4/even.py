largest = -999999999999999999999999

for _ in range(5):
    number = float(input("Enter a number: "))
    if number > largest:
        largest = number 


print("The largest number is: ", largest)