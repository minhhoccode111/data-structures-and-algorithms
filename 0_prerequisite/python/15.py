# and yet another class definition that inherits from Superhero and Bat
from bat14 import Bat
from superhero13 import Superhero


# define Batman as a child that inherits from both Superhero and Bat
class Batman(Superhero, Bat):

    def __init__(self, *args, **kwargs):
        # typically to inherit attributes you have to call super:
        # super(Batman, self).__init__(*args, **kwargs)
        # however we are dealing with multiple inheritance here, and super()
        # only works with the next base class in the MRO list
        # so instead we explicitly call __init__ for all ancestors
        # the use of *args and **kwargs allows for a clean way to pass
        # arguments, with each parent "peeling a layer of the onion"
        Superhero.__init__(
            self, "anonymous", movie=True, superpower=["Wealthy"], *args, **kwargs
        )
        Bat.__init__(self, *args, can_fly=False, **kwargs)
        # override the value for the name attribute
        self.name = "Sad Affleck"

    def sing(self):
        return "nan nan nan nan nan batman!"


if __name__ == "__main__":
    sup = Batman()

    # the method resolution order
    print(Batman.__mro__)  # => (<class '__main__.Batman'>,
    ######################## => <class 'superhero.Superhero'>,
    ######################## => <class 'human.Human'>,
    ######################## => <class 'bat.Bat'>, <class 'object'>)

    # calls parent method but uses its own class attribute
    print(sup.get_species())  # superhuman

    # calls overridden method
    print(sup.sing())  # nan nan nan nan nan batman!

    # calls method from human, because inheritance order matters
    sup.say("I agree")  # sad affleck: i agree

    # call method that exists only in 2nd ancestor
    print(sup.sonar())  # ))) ... (((

    # inherited class attribute
    sup.age = 100
    print(sup.age)  # 100

    # inherited attribute from 2nd ancestor whose default value was overridden
    print("Can I fly? " + str(sup.fly))  # Can I fly? False
