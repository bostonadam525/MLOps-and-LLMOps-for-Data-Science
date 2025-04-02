# Factory Design Pattern in Python
class Dog:
    """A simple dog class."""

    def __init__(self, name):
        self._name = name

    def speak(self):
        return "Woof!"

    def get_pet(pet="dog"):

    ## create objects and return to user with a dict
        """The Factory Method"""
        pets = dict(dog=Dog("Hope"))
        return pets[pet]

class Cat:
    """A simple cat class."""

    def __init__(self, name):
        self._name = name

    def speak(self):
        return "Meow!"

## get_pet method not part of Cat class
def get_pet(pet="dog"):
    ## create objects and return to user with a dict
    """The Factory Method"""
    pets = dict(dog=Dog("Hope"), cat=Cat("Peace"))
    return pets[pet]

## invoke get_pet method just added
d = get_pet("dog")
print(d.speak())

c = get_pet("cat")
print(c.speak())





### Abstract Factory
class Dog:
    """One of the objects to be returned."""

    ## 1. speak method
    def speak(self):
        return "Woof!"

    def __str__(self):
        return "Dog"

## concrete factory --> returns 2 objects
class DogFactory:
    """Concrete Factory"""

    def get_pet(self):
        """Returns a Dog object"""
        return Dog()

    def get_food(self):
        """Returns a Dog Food object."""
        return "Dog Food!"


class PetStore:
    """PetStore houses our Abstract Factory."""
    def __init__(self, pet_factory=None):
        """pet_factory is our Abstract Factory"""
        self._pet_factory = pet_factory

    def show_pet(self):
        """Utility method to display details of objects returned by DogFactory."""

        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()

        print("Our pet is '{}'!".format(pet))
        print("Our pet says hello by '{}'".format(pet.speak()))
        print("Its food is '{}'!".format(pet_food))

# Create a Concrete Factory to be used by the Abstract Factory
factory = DogFactory()

# Create a pet store housing our Abstract Factory
shop = PetStore(factory)

# Invoke utility method to show details of our pet
shop.show_pet()
