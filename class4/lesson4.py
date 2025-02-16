number_to_guess = 5
user_number = 0 #initializing a variable

while number_to_guess != user_number:
    user_number = int(input("Enter a number: "))
    if user_number > number_to_guess:
        print("Guess lower")
    elif user_number < number_to_guess:
        print("Guess higher")

print("You guessed the number")



# Fixed Iteration Loop - Number of times the loop runs is finite
# Conditional Loop - For the loop to break a certain condition needs to be met


