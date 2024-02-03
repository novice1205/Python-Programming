#Duck Typing
class Duck:
    def quack(self):
        print("I am a duck and I quack")
class Goose:
    def quack(self):
        print("I am a goose and I quack")
class Cat:
    def quack(self):
        print("I am a cat and I don't quack")
def duck_check(animal):
    animal.quack()
duck_check(Duck())
duck_check(Goose())
duck_check(Cat())