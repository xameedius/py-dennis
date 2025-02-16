#Totalling

n = int(input("How many numbers do you want a sum of? "))
sum = 0 

for _ in range(n):
    number = float(input("Enter a number: "))
    sum = sum + number

print(sum)