class employee:
    company = "ITC"
    name = "harry"
    def show(self):
        print(f"The employee name is:    {self.name} and the company is {self.company}")

class programmer(employee):
    company = "ITC infotech"
    language= "python"
    def print_language(self):
        print(f"The company name is:    {self.company} and they are good with {self.language} language")

class program_manager(programmer):
    company = "GOOGLE"
    def showLanguage(self):
        print(f"The company name is:    {self.company} and they are good with {self.language} language")

a= employee()
b= program_manager()
c= programmer()

b.show()
c.print_language()
b.print_language()
b.showLanguage()