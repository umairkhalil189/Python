a= 1
b=2
c=3

def greatest(a, b, c):
    if(a>b and a>c):
        print("a is the greatest")
    elif(b>a and b>c):
         print("b is the greatest")
    elif(c>a and c>b):
         print("c is the greatest")

greatest(a, b, c)