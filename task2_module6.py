"""Problem Statement: Write a Python program that:
1.   Creates a list of numbers from 1 to 10.
2.   Extracts the first five elements from the list.
3.   Reverses these extracted elements.
4.   Prints both the extracted list and the reversed list"""

l=list(range(1,11))
l5=l[0:5]
l6=l5[::-1]
print(f"original list:{l}\n Extracted first 5 element:{l5} \n Reversed extracted element:{l6}")
