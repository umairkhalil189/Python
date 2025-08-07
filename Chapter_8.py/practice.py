from average import avg
n = int(input("How many numbers your want to to find average of:    "))
i=1
num= []
for i in range(n):
    a = int(input("Enter the number: "))
    num.append(a)
    i+=1

avg(num, n)



# print(num)