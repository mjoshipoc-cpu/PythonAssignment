"""Problem Statement:  Write a Python program that:
1. 	Takes an integer input from the user.
2. 	Checks whether the number is even or odd using an if-else statement.
3. 	Displays the result accordingly."""

user_input = input("Enter integer: ")
try:
    val = int(user_input)
    if val%2==0:
        print(f"{val} is even number ")
    else:
        print(f"{val} is odd number ")
    print("This is an integer.")
except ValueError:
    print("This is not an integer.")

