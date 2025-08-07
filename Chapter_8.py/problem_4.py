'''
sum(1)= 1
sum(2)= 1+2
sum(3)= 1+2+3
sum(n)= 1+2+3+......... (n-1) + n
'''

def sum_natural_numbers(n):
    if (n==1):
        return 1
    return sum_natural_numbers(n-1) + n

n= int(input("Enter the number uptil you want to find natural numbers:  "))
a=sum_natural_numbers(n)
print(f"Sum of first {n} natural numbers are: {a}")