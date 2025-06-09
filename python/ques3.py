# Task
# Given an integer, , and  space-separated integers as input, create a tuple, , of those  integers. Then compute and print the result of .

# Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.

# Input Format

# The first line contains an integer, , denoting the number of elements in the tuple.
# The second line contains  space-separated integers describing the elements in tuple .

# Output Format

# Print the result of .

# Sample Input 0

# 2
# 1 2
# Sample Output 0

# 3713081631934410656




# Read the number of elements in the tuple
n = int(raw_input())  

# Read space-separated integers, convert each to int, and store as a list
integer_list = map(int, raw_input().split())

# Convert the list to a tuple (immutable sequence)
t = tuple(integer_list)

# Print the hash value of the tuple
print hash(t)
