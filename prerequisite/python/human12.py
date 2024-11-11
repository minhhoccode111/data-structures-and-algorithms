# 6. classes


# we use the 'class' statement to create a class


class Human:
    # a class attribute. it is shared by all instance of this class
    species = "H. sapiens"

    # basic initializer, this is called when this class is instantiated
    # note that the double leading and trailing underscores denote objects or attributes that are used by python but that live in user-controlled namespaces. methods (or object or attributes) like: __init__, __str__, __repr__ etc. are called special methods (or sometimes called dunder methods). you should not invent such names on your own
    def __init__(self, name):
        # assign the argument to the instance's name attribute
        self.name = name

        # initialize property
        self._age = 0  # the leading underscode indicates the 'age' property is intended to be used internally
        # do not rely on this to be enforces: it's a hint to other devs

    # an instance method. all methods take 'self' as the first argument
    def say(self, msg):
        print("{name}: {message}".format(name=self.name, message=msg))

    # another instance method
    def sing(self):
        return "yo... yo... microphone check... one two... one two..."

    # a class method is shared among all instances
    # they are called with the calling class as the first argument
    @classmethod
    def get_species(cls):
        return cls.species

    # a static method is called without a class or instance reference
    @staticmethod
    def grunt():
        return "*grunt*"

    # a property is just like a getter
    # it turns the method age() into a read-only attribute of the same name
    # there's no need to write trivial getters and setters in python, though
    @property
    def age(self):
        return self._age

    # this allows the property to be set
    @age.setter
    def age(self, age):
        self._age = age

    # this allow the property to be deleted
    @age.deleter
    def age(self):
        del self._age


# when a python interpreter reads a source file it executes all its code
# this __name__ check makes sure this code block is only executed when this module is the main program
if __name__ == "__main__":
    # instantiate a class
    i = Human(name="Ian")
    i.say("hi")  # "Ian: hi"
    j = Human("Joel")
    j.say("hi")  # "Joel: hello"
    # i and j are instances of type Human; i.e., they are Human objects

    # call our class method
    i.say(i.get_species())  # "Ian: H. sapiens"
    # change the shared attribute
    Human.species = "H. neanderthalensis"
    i.say(i.get_species())  # "Ian: H. neanderthalensis"
    j.say(j.get_species())  # "Joel: H. neanderthalensis"

    # call the static method
    print(Human.grunt())  # "*grunt*"

    # update the property for this instance
    i.age = 42
    # get the property
    i.say(i.age)  # "Ian: 42"
    j.say(j.age)  # "Joel: 0"
    # delete the property
    del i.age
    # i.age # this would raise an AttributeError
