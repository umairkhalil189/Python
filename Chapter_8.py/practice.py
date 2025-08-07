n = int(input("How many numbers your want to to find average of:    "))
i=1
num= []
for i in range(n):
    a = int(input("Enter the number: "))
    num.append(a)
    i+=1

def avg (num, n):
    total = 0
    total = sum(num)
    avg = (total)/n
    print(f"Average is:  {avg}")
    return avg


avg(num, n)



# print(num)