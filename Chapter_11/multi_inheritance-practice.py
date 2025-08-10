class employee:
    company = "ITC"
    name = "harry"

    def show(self):
        print(f"The employee name is:    {self.name} and the company is {self.company}")


# class programmer:
#     company = "ITC infotech"

#     def show(self):
#         print(f"The name is:    {self.name} and the salary is {self.salary}")

#     def showLanguage(self):
#         print(f"The name is:    {self.name} and he is good with {self.language} language")

# class coder:
#     language = "Python"
#     def print_languages(self):
#         print(f"Out of all the languages, here is your language {self.language}")

class programmer(employee):
    company = "ITC infotech"

    def showLanguage(self):
        print(f"The company name is:    {self.company} and they are good with {self.language} language")

class program_manager(programmer):
    company = "ITC infotech"

    def showLanguage(self):
        print(f"The company name is:    {self.company} and they are good with {self.language} language")

a= employee()
b= programmer()

b.show()
b.print_languages()
b.showLanguage()