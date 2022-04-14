def func1(param):
    print(param)

# func1("Hello Planet!") will output Hello Planet! to the command line


def areaOfRectangle(length, width):
    area = length * width
    return area

# areaOfTenByTenRectangle = areaOfRectangle(10, 10);
# The value of areOfTenByTenRectangle = 10 * 10 = 100

class Human:
    def __init__(self, name, age):
        self.age = age
        self.name = name
        self.nameTag = name + " (" + str(age) + ")"

    def sayHi(self, otherPersonsName):
        print("Hello " + otherPersonsName + ", I am " + self.nameTag)

# someHuman = Human("Jeremy", 100)
# This is creating a new "instance" of the class "Human"
# someHuman.age is 100, someHuman.name is Jeremy, someHuman.nameTag is Jeremy (100)

# >> someHuman.sayHi("Jenny")
# << Hello Jenny, I am Jeremy (100)

# Always remember to add "self" as the first parameter to functions which are defined
# within classes

# "self" within methods in classes refers to the instance of the class that you created
# e.g. in the case above, self is Human("Jeremy", 100), which is 
# { age: 100, name: "Jeremy", nameTag: "Jeremy (100)" }

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def length(self):
        return (self.x * self.x + self.y * self.y) ** 0.5

    def normalised(self):
        return Vector(self.x / self.length(), self.y / self.length())

# You can access methods of a certain class with self too
# In this case: length() returns the length of a Vector
# normalised() can take this length value and do more calculations with it
# (In this case, dividing a vector by its length produces a vector which is always of length 1)

# https://docs.python.org/3/tutorial/classes.html