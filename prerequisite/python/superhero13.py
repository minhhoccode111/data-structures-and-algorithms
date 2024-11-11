# 6.1 inheriance

# inheritance allows new child classes to be defined that inherit methods and variable from their parent class

# using the Human class defined in 12.py as the base or parent class, we can define a child class, Superhero, which inherits variables like "species", "name", and "age", as well as methods, like "sing" and "grunt" from the Human class, but can also have its own unique properties

# to take advantage of modularization by file you could place the classes above (12.py) in their own files, say, human.py

# to import functions from other files use the following format
# from "filename-without-extension" import "function-or-class"

from human12 import Human


# specify the parent class(es) as parameters to the class definition
class Superhero(Human):
    # if the child class should inherit all of the parent's definitions without any modifications, you can just use the "pass" keyword (and nothing else)
    # but in this case it is commented out to allow for a unique child class:
    # pass

    # child classes can override their parents' attributes
    species = "Superhuman"

    # children automatically inherit their parent class's constructor including its arguments, but can also define additional arguments or definitions and override its methods such as the class constructor
    # this constructor inherits the "name" argument from the "Human" class and adds the "superpower" and "movie" arguments
    def __init__(
        self, name, movie=False, superpower=["super strength", "bulletproofing"]
    ):
        # add additional class attributes:
        self.fictional = True
        self.movie = movie
        # be aware of mutable default values, since defaults are shared
        self.superpowers = superpower

        # the "super" function lets you access the parent class's methods that are overridden by the child, in this case, the __init__ method
        # this calls the parent class constructor:
        super().__init__(name)

    # override the sing method
    def sing(self):
        return "Dun, dun, DUN!"

    # add an additional instances method
    def boast(self):
        for power in self.superpowers:
            print("I wield the power of {pow}!".format(pow=power))


if __name__ == "__main__":
    sup = Superhero(name="Tick")

    # isntance type checks
    if isinstance(sup, Human):
        print("I am human")
    if type(sup) is Superhero:
        print("I am a superhero")

    #  get the "method resolution order" used by both getattr() and super()
    # the order in which classes are searched for an attribute or method
    # this attribute is dynamic and can be updated

    print(Superhero.__mro__)  # (<class '__main__.Superhero'>,
    # <class 'human.Human'>, <class 'object'>)

    # calls parent method but uses its own class attribute
    print(sup.get_species())  # Superman

    # calls overridden method
    print(sup.sing())  # Dun, dun, DUN!

    # calls method from Human
    sup.say("Spoon")  # Tick: Spoon

    # call method that exists only in Superhero
    sup.boast()  # I wield the power of super strength!
    ############## I wield the power of bulletproofing!

    # inherited class attribute
    sup.age = 31
    print(sup.age)  # 31

    # attribute that only exists within Superhero
    print("Am I Oscar eligible? " + str(sup.movie))
