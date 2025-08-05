n = int(input("Enter total numbers: "))

total = 0

for i in range(n):
    num = float(input(f"Enter number {i +1}: "))
    total += num

avg = total/n

print("Average of numbers are:  ", avg)