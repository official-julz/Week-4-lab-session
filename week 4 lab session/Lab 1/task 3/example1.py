# Author : Sana Alyaseri
# Class software development
# Example 4 : Accessing a Global Variable
count = 0
def increment():
    global count
    count += 1
    print(f"Count inside functions: {count}")

# call the function
increment()
increment()

# access the global variable
print(f"count outside function: {count}")