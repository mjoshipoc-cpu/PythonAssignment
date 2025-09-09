"""Problem Statement: Write a Python program that:
1.   Uses a for loop to iterate over numbers from 1 to 50.
2.   Calculates the sum of all integers in this range.
3.   Displays the final sum"""
a=range(1,50)
summk=0
for i in a:
    summk+=i
print(f"sum is {summk}")