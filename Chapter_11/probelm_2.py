class animal:
    pass
        


class pet(animal):
    pass

class dog(pet):

    @staticmethod
    def bark():
        print("Bow bow! Dog barksss ")

o = dog()
o.bark()


