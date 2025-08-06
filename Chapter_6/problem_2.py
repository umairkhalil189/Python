a1= int(input("Enter marks 1:  "))
a2= int(input("Enter marls 2:  "))
a3= int(input("Enter marks 3:  "))

perc = ((a1+a2+a3)/300)*100


if(perc >= 40 and a1>=33 and a2>=33 and a3>=33):
    print("You are passed", perc)
else:
    print("You are failed", perc)

# elif(a3>a1 and a3>a2 and a3> a4 ):
#     print(f"a3 = {a3} enterd by user is the greatest number")

# elif(a4>a1 and a4>a2 and a4> a3 ):
#     print(f"a4= {a4} enterd by user is the greatest number")