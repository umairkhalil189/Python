n = int(input("Enter the number:    "))
prod = 1
for i in range(1, n+1):
    prod = prod * i
    i+=1

print(f"The factorial of {n} is {prod}")