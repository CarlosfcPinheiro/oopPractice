# Creating classes ===========
# Base class
class Animal:
    def __init__(self, name:str, age:int, breed:str) -> None:
        self.name = name
        self.age = age
        self.breed = breed
    
    def eat(self):
        return print(f"{self.name} thinks it's delicious!")
    
    def sleep(self):
        return print(f"{self.name} is sleeping. Zzzzz")
    
# Derived/child classes
class Dog(Animal):
    family = 'Dog'
    def takeBall(self):
        return print(f'{self.name} caught the ball and is having fun 🐶')

class Cat(Animal):
    family = 'Cat'
    def bake(self):
        return print(f'{self.name} is making little breads 😼')
    
    def seekLaser(self):
        return print(f'{self.name} is seeking for the laser point. Attention!! 😾')

class Bird(Animal):
    family = 'Bird'
    def fly(self):
        return print(f'{self.name} is flying beautifully')