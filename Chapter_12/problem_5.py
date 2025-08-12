'''"
5. Store the multiplication tables generated in problem 3 in a file named Tables.txt.
'''


n= int(input("Enter the no for table:   "))

table = [n*i for i in range(1, 11)]
print(table)

with open("tables.txt", "a") as f:
    f.write(f"The table of {n} is: {str(table)} \n")
