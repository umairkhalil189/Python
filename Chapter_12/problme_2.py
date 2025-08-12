'''
2. Write a program to print third, fifth and seventh element from a list using enumerate 
function

'''


l = [5, 9, 3, 1, 15, 12, 7, 8, 0]
for index, item in enumerate(l):
    if (index == 2) or index == 4 or index == 6:
        print(f"At {index} item is:  {item}")
    

# #-----Below one: I solved thsi for my own curiosity to print ecery 3rd element:
# for index, item in enumerate(l):
#     if (index + 1) % 3 == 0:
#         print(f"At {index} item is:  {item}")
#     # index+=3