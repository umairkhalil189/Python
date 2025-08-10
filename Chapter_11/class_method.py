class employee:

    a = 1

    @classmethod
    def show(self):
        print(f"The value of class operator a is:   {self.a}")

    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name(self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

e = employee()
e.a= 45             #Instance Val
e.name= "harry khan"
print(e.name)
e.show()
