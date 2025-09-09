def fact(n):
    if n<2:
        return 1
    else:
        return n*fact(n-1)


u =input("enter a integer")
try:
    val =int(u)
    print(f"factorial of {val} is {fact(val)}")
except Exception as e:
    print(e)



