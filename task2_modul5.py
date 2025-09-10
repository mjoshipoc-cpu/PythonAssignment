"""Problem Statement: Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file."""

content=input("please enter text to write in the file: ")
with open("output.txt","w") as e:
    e.write(content)
append=input("please enter text to append in the file: ")
with open("output.txt","a") as e:
    e.writelines(["\n",append])

with open("output.txt","r") as e:
    print(e.read())
