def multiply_numbers():
    print("Simple multiplication table")

    number = int(input("Enter a number: "))

    for i in range(1, 11):
        result = number * i
        print(f"{number} x {i} = {result}")

# Call the function
multiply_numbers()
