def multiplication_table(n):
    for i in range(1,11): 
        print(f"{n} x {i} = {n * i}")


#Main
multiplication_table(int(input("Enter a number: ")))