# Mixin Classes

# A mixin is a class whose purpose is to add 
# extra functionality to other class definitions

# Idea:  If a user implements some basic 
# features in their class, a mixin can be used to 
# fill out the class with extra functionality

# Sometimes used as a technique for reducing 
# the amount of code that must be written 

class Dog:
    def noise(self):
        return 'Woof!'

class Bike:
    def noise(self):
        return 'Whroom!'

class Loud:
    def noise(self):
        return super().noise().upper()

# Mxin features:
#   Not usable in isolation
#   Mixes with other classes via inheritance
class LoudDog(Loud, Dog): ...
class NotSoLoudDog(Dog, Loud): ...
class LoudBike(Loud, Bike): ...
# Order of inheritance matters


if __name__ == '__main__':
    ld1 = LoudDog()
    print(ld1.noise())      # WOOF!

    ld2 = NotSoLoudDog()
    print(ld2.noise())      # Woof!

    # print(LoudDog.__mro__)      # NotSoLoudDog, Dog, Loud ...
    # print(NotSoLoudDog.__mro__) # LoudDog, Loud, Dog ...