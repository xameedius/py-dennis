# Exception Handling
# try, except (Error message)

try:
    number = int(input("Enter Number: ")) #Value Error
    print(number)
except ValueError:
    print("No strings allowed")


while True:
    try:
        user_input = input("Enter your first number (or enter 'stop' to exit)")
        if user_input == 'stop':
            break
        number1 = float(user_input)

        user_input2 = input("Enter your second number (or enter 'stop' to exit)")
        if user_input == 'stop':
            break
        number2 = float(user_input2)
        
        print(number1/number2)

    except ValueError:
        print("Value Error")

    except ZeroDivisionError:
        print("Zero Division Error")
    
# else, finally

try:
    num = int(input("Enter a number: "))
    print(f"You entered {num}")
except ValueError:
    print("Error: Please enter a valid number")
else:
    print("this is the end of program")

student = {
    "name" : "Dennis",
    "age"  : 14,
}

print(student["country"])

file = open("myfile.txt" , "r")

# try , except, else, finally

try:
    num = int(input("Enter a number: "))
    result = 10/num
except ZeroDivisionError:
    print("Error: cannot divide by Zero")
except ValueError:
    print("Error: Invalid Input")
else:
    print("Success! The result is:", result) # runs if there is no error
finally:
    print("End of program")  # Always runs

# def check_age(age):
#     if age < 18:
#        raise ValueError("You must be 18 or older to register")
#     return "registration successful"

# # Main code

# age = int(input("Enter your age"))
# print(check_age(age))


# Write a program that asks for a number and handles a ValueError if the input is not a number.

while True:
    try:
        num = float(input("Enter a number: "))
        print(f"you entered {num}")
        break
    except ValueError:
        print("You did not enter a number")