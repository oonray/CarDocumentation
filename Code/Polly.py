"""
.. codeauthor:: Alexander
.. date:: 2018-01-24
.. modulename:: polly

"""

class Cage:
    def __init__(self, Name):
        self.name = Name
        self.bars = True
        self.has_animal = False
        self.animal = None

    def cage(self,animal):
        self.animal = animal
        self.has_animal = True

    def release(self):
        animal = self.animal
        self.has_animal= False
        self.animal = None
        print("{} Flew Away!".format(animal.name))
        print(animal.say())
        return animal

class Food:
    def __init__(self, Name):
        self.name = Name
        self.nutrients = 100
        self.calories = 100
        self.color = "Brown"

class Animal:
    def __init__(self, Name, Food, Cage):
        self.name = Name
        self.alive = True
        self.hungry = False
        self.food = Food
        self.cage = Cage

    def feed(self,food):
        if food == self.food:
            print("Yummy!")
            self.hungry = False
            return True
        else:
            print("The animal does not eat this!")
            return False

    def say(self):
        print("Indestinct Sound")



class Bird(Animal):
    def __init__(self, Name, Food, Cage):
        Animal.__init__(self,Name, Food, Cage)
        self.food = "Bird Seeds"
        self.cage = Cage

    def say(self):
        print("Squeeek!")


class Dog(Animal):
    def __init__(self,Name, Food, Cage):
        Animal.__init__(self,Name, Food,Cage)
        self.food = "Dog Food"
        self.cage = None

    def say(self):
        print("Woof!")


class AnimalFactory:
    def __init__(self):
        self.food = {
            "Dog Food":lambda: Food("Dog"),
            "Bird Food":lambda: Food("Seeds")
        }

        self.cages = {
            "Bird Cage": lambda: Cage("Bird")
        }

        self.animals = {
            "Dog":self.get_dog,
            "Bird":self.get_bird
        }

    def get_animal(self, Animal, Name):
        if Animal in self.animals.keys():
            return self.animals[Animal](Name)
        else: return False


    def get_dog(self, Name):
        return Dog(Name,self.food["Dog Food"],None)

    def get_bird(self, Name):
        animal = Bird(Name,self.food["Bird Food"],self.cages["Bird Cage"]())
        animal.cage.cage(animal)
        return animal


AFactory = AnimalFactory()

birb = AFactory.get_animal("Bird","Polly")
dog = AFactory.get_animal("Dog","Joe")

birb.say()
dog.say()

birb.cage.release()
print(birb.cage.has_animal)






