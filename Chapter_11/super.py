class employee:
    def __init__(self):
         print("Constructor of Employee")
          
    a= 1

class coder(employee):
    def __init__(self):
        super().__init__()
        print("Constructor of Coder")
    b=2

class manager(coder):
    def __init__(self):
        super().__init__()
        print("Constructor of Programmer")
    c=3

# o = employee()
# print(o.a)
# o = coder()
# print(o.a, o.b)
o = manager()
print(o.a, o.b, o.c)