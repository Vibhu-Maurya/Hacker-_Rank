# you are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

# For Example:

# Www.HackerRank.com → wWW.hACKERrANK.COM
# Pythonist 2 → pYTHONIST 2  
# Function Description

# Complete the swap_case function in the editor below.

# swap_case has the following parameters:

# string s: the string to modify
# Returns

# string: the modified string
# Input Format

# A single line containing a string .

# Constraints


# Sample Input 0

# HackerRank.com presents "Pythonist 2".
# Sample Output 0

# hACKERrANK.COM PRESENTS "pYTHONIST 2".



# Define a function named swap_case that takes one argument 's'
def swap_case(s):
    # Use Python's built-in swapcase() method to switch lowercase to uppercase and vice versa
    return s.swapcase()

# This ensures the code below runs only when the script is executed directly (not imported)
if __name__ == '__main__':
    # Read a line of input from the user and store it in variable 's'
    s = input()
    
    # Call the swap_case function with input 's' and store the result
    result = swap_case(s)
    
    # Print the final result with cases swapped
    print(result)
