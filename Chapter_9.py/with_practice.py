# f.open("myfile.txt")

# print(f.read())
# f.close()

with open("myfile.txt") as f:
    print(f.read())