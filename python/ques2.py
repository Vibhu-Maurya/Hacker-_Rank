# Consider a list (list = []). You can perform the following commands:

# insert i e: Insert integer  at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.
# This block only runs if the script is executed directly
if __name__ == '__main__':

    # Read the number of commands to be processed from user input
    N = int(input())

    # Initialize an empty list to perform operations on
    lst = []

    # Loop N times to process each command
    for _ in range(N):
        # Read the command line, split it into parts by space
        command = input().split()

        # The first word is the command name (e.g., insert, append, etc.)
        cmd = command[0]

        # The rest of the items in the command are arguments (numbers)
        args = command[1:]

        # Check which command was given and perform the corresponding list operation

        if cmd == "insert":
            # Insert the value (args[1]) at the position (args[0])
            lst.insert(int(args[0]), int(args[1]))

        elif cmd == "print":
            # Print the current state of the list
            print(lst)

        elif cmd == "remove":
            # Remove the first occurrence of the value (args[0])
            lst.remove(int(args[0]))

        elif cmd == "append":
            # Add the value (args[0]) to the end of the list
            lst.append(int(args[0]))

        elif cmd == "sort":
            # Sort the list in ascending order
            lst.sort()

        elif cmd == "pop":
            # Remove and return the last item of the list
            lst.pop()

        elif cmd == "reverse":
            # Reverse the order of the list
            lst.reverse()
