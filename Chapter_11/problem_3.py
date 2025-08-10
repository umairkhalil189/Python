class employee:
    salary = 20000
    increment = 20

    @property
    def salaryAfterincrement(self):
        return (self.salary + self.salary* (self.increment/100))
    
    @salaryAfterincrement.setter
    def salaryAfterincrement(self, salary):
        self.increment = ((salary/self.salary) -1)*100



e = employee()
e.salaryAfterincrement = 25000
print(e.increment)