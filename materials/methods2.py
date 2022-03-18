class human:
    name = 'John'
    age = 20
    height = 170

    def __init__(self, name,  age, height):
        self.name = name
        self.age = age
        self.height = height

    def greet(self):
        return 'Hello'

    def goodbye(self):
        return 'Bye Bye'

    def intro(self):
        print(f'Hi, my name is {self.name}, I am {self.age}. I am {self.height} cm tall ')

John = human
Mary = human

print(John.greet(Mary))
John.intro(John)


print(John.goodbye(Mary))



def greet():
    print('hello')

greet()


