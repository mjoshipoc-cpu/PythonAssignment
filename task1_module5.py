"""problem Statement:  Write a Python program that:
1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist."""

try:
    with open("C:/Users/91991/Downloads/myfile.txt","r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found")