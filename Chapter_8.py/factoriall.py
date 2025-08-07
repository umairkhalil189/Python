def factorial(n):
    if (n==0 or n==1):
        return 1
    return n* factorial(n-1)


n= int(input("Enter the no. for factorial:  "))
fact= factorial(n)
print(f"The factorial of {n} is {fact}")