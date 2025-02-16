# DATA STRUCTURES - Lists, Dictionaries, Tuples, Sets

colors = ["Yellow", "Blue", "Red"] #A List is muttable
empty_list = list()
# colors.append("Green")



student = {
    "Name" : "Dennis",
    "Age"  : 14,
    "country": "USA",
}
empty_dict = dict()


cards = ("Hearts" , "Spades" , "Clubs" , "Diamonds") # A Tuple is immumatable
more_cards = ("Jokers" , "Uno", "Playcards")
empty_tuple = tuple()


# # Concatination - Combine 2 or more tuples together
# result = cards + more_cards
# print(result)

# # Repetition works as well
# print(cards * 3)

# Reasons to use a tuple instead of a List
# 1 - Faster than Lists (Because they don't change)
# 2 - Used for fixed data like coordinates, colors, etc.

# A set is a collection of unique elements
# Like a dictionary a set also has {}
# In a set Dublicates are autometically removed


# A = {1,2,3,9,10}
# B = {4,5,6,7,8,9,10}

# # Union
# print(f"The Union of A and B is {A | B}")

# # Intersection
# print(f"The Intersection of A and B is {A & B}")

# # Difference
# print(f"The Difference of A and B is {A - B}") # It returns the elements which are in A and not in B

# # Symmetric Difference
# print(f"The Symmetric Difference of A and B is {A ^ B}") # It returns elements that are in either A or B, but not in both

# def remove_duplicates(lst):
#     return list(set(lst))

# #Main
# my_list = [1,1,1,2,2,4,5]
# print(remove_duplicates(my_list))




# def find_largest_smallest(tup):
#     largest = -999999999999999999999
#     smallest = 999999999999999999999
#     for n in tup:
#         if n > largest:
#             largest = n
#         if n < smallest:
#             smallest = n
#     return largest, smallest

# #Main Program
# numbers = (11,22,55,10,15,345)
# largest, smallest = find_largest_smallest(numbers)
# print(f"The largest is {largest}")
# print(f"The smallest is {smallest}")

def get_even(tup):
    even_list = []
    for n in tup:
        if n % 2 == 0:
            even_list.append(n)
    return tuple(even_list)

#main
numbers = (1,2,3,4,5,6,7,8,9,10)
print(get_even(numbers))

#MADE cHANGES
#make changes again
# again