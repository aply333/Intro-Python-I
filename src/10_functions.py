# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

def is_even(x):
    """Determines if the given value is even or odd. It takes one argument that is an integer"""
    if x % 2 == 0:
        print('Even')
        return True
    else:
        print('Odd')
        return False


# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE

is_even(num)


