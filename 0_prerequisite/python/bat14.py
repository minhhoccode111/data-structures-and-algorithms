# 6.2 multiple inheritance


# another class definition
class Bat:
    species = "Baty"

    def __init__(self, can_fly=True):
        self.fly = can_fly

    # this class also has a say method
    def say(self, msg):
        msg = "... ... ..."
        return msg

    # and its own method as well
    def sonar(self):
        return "))) ... ((("


if __name__ == "__main__":
    b = Bat()
    print(b.say("Hello"))
    print(b.fly)
