class Human:
    # You can define default values for all instances of Human with this
    isAHuman = True
    def __init__(self, name, age):
        self.age = age
        self.name = name
        self.nameTag = name + " (" + str(age) + ")"

    def greet(self, otherPerson):
        print("Hello " + otherPerson.nameTag + ", I am " + self.nameTag)

    def greet(self, otherPerson):
        print("Goodbye " + otherPerson.nametag)

John = Human("John", 200)
Mary = Human("Mary", 193)

John.greet(Mary)
# Hello Mary (193), I am John (200)

John.goodbye(Mary)
# Goodbye Mary (193)

Human.isAHuman
# True

John.isAHuman
# True

Mary.isAHuman
#True


# https://docs.python.org/3/tutorial/classes.html