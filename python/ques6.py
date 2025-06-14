# You are given the firstname and lastname of a person on two different lines. Your task is to read them and print the following:

# Hello firstname lastname! You just delved into python.

# Function Description

# Complete the print_full_name function in the editor below.

# print_full_name has the following parameters:

# string first: the first name
# string last: the last name
# Prints

# string: 'Hello  ! You just delved into python' where  and  are replaced with  and .
# Input Format

# The first line contains the first name, and the second line contains the last name.

# Constraints

# The length of the first and last names are each ≤ .

# Sample Input 0

# Ross
# Taylor
# Sample Output 0

# Hello Ross Taylor! You just delved into python.
# Explanation 0

# The input read by the program is stored as a string data type. A string is a collection of characters.


# solution

# Define the function that takes first name and last name as input
def print_full_name(first, last):
    # Use an f-string to format and print the message
    print(f"Hello {first} {last}! You just delved into python.")

# This block ensures the code below runs only when this file is executed directly
if __name__ == '__main__':
    # Read the first name from user input
    first_name = input()  # Example input: Ross
    # Read the last name from user input
    last_name = input()   # Example input: Taylor
    # Call the function with the given inputs
    print_full_name(first_name, last_name)
