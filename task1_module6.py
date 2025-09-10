"""Problem Statement: Write a Python program that:
1.   Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the student’s name is not found, display an appropriate message."""

mydict={"s1":11,"alice":12}
name=input("please enter student name: ")
if name.lower() in mydict:
    print(f" {name}'s mark is {mydict[name.lower()]}")
else:
    print("please enter correct name")