class employee:
    lang = "python"
    salary = 1200000

    def __init__(self, name, lang, salary):     #Dunder Method which is automatically called
        self.name = name
        self.lang= lang
        self.salary= salary
    
    def get_info(self):
        print(f"The language is {self.lang}. The salary is:  {self.salary}")

    @staticmethod
    def greet():
        print("\nGood Morning")


e1= employee("Harry", "C++", 2000000)
# e1= employee()
 
# e1.name= "harry"
# e1.get_info()
# e1.greet()
print(e1.name, e1.lang , e1.salary)