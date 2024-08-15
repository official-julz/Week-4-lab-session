def add_numbers():
    # Define two integers
    num1 = 8
    num2 = 9
    
    # Calculate the sum
    sum = num1 + num2
    
    # Return the sum
    return sum

def greet():
    # Display a welcome message
    print("Welcome to the addition program!")
    
    # Call add_numbers() and display the result
    result = add_numbers()
    print(f"The result of adding the numbers is: {result}")

# Call the greet function to execute the program
greet()
