# Name: Case Buckmaster
# LAB: 4.17
# Description: Repeatedly takes a string and integer as input to complete a mad libs until the user types "quit".

# Variables

# Asks user for the mad lib's input.
mad_lib_input = input().strip().split()

# Prints the same mad lib until the user types "quit" as an input.
while mad_lib_input[0] != "quit":
    print(f"Eating {mad_lib_input[1]} {mad_lib_input[0]} a day keeps the doctor away.")

    # Ask for input again.
    mad_lib_input = input().strip().split()
