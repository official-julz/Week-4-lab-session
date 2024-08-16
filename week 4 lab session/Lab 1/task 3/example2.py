# Author : Sana Alyaseri
# Class software development
# Example 5: Using Global Variables to share data between functions

total_sum = 0

def add_to_sum(num):
    global total_sum
    total_sum += num

def display_sum():
    print(f"Toatl sum: {total_sum}")

# call the function
add_to_sum(6)
add_to_sum(12)
add_to_sum(18)
display_sum()