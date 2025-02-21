# Core Python - JSON and APIs - Today , Modules - Tomarrow , Classes and Objects - Next Week
# From the week after then next week - first Monday, Tuesday days - Revise Core Python, Do tougher Questions, CS50P - Wednesday - We will focus on a path

# After Core Python - Game Development, Data Science, AI/ML, Web Scraping, API Development, Back-End Web-Development

# What is JSON - JavaScript Object Notation - When we request information using an API, the result we get is in JSON format
# What is API - Is a form of bridge between our code and a website or server - Application Development Interface

# weather = "Summer" #We will use a weather API to get the weather
# print(weather)

# This is how to convert anything into JSON
# import json

# data = {
#     "name": "Alice",
#     "age": 25,
#     "city": "Dubai"
# }

# json_string = json.dumps(data)  # Convert dictionary to JSON
# print(json_string)

# Convert JSON into python Dictionary
# import json
# json_data = '{"name": "Alice", "age": 25, "city": "Dubai"}'
# python_dict = json.loads(json_data)  # Convert JSON string to dictionary
# print(python_dict["age"])  # Output: Alice


# api_key = '8Pv0rs7oSUAyQRMi'

# url = 'https://my.meteoblue.com/packages/basic-1h_basic-day_current_clouds-1h_clouds-day_sunmoon_moonlight-15min_moonlight-30min_moonlight-1h?apikey=8Pv0rs7oSUAyQRMi&lat=25.0772&lon=55.3093&asl=24&format=json'


def prime(num):
    is_prime = True
    for x in range(2,num): 
        if num % x == 0:
            is_prime = False
    return is_prime
            
def main():
    while True:
        try:
            num = int(input("Enter a number: "))
        except ValueError:
            print('your wrote words instead of numbers')
        else:
            break
    print(prime(num))

#Run Code
if __name__ == "__main__":
    main()

