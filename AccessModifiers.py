# Hi Enthusiast, You enjoy learning python.
# Our topic is about Access Modifier
# These access modifier are: public, private, and protected
# The public modifier is accessible even outside of the class
# The private modifier is only accessible inside of the class
# The protected modifier is accessible from declared class and subclass of the class

from dataclasses import dataclass

@dataclass # We use decorated method 'dataclass' to predefine the methods you need.
# These predefine methods are:
#  __init__ __repr__ __eq__ __ne__ __lt__ __le__ __gt__ __ge__
# Learn more at https://www.python.org/dev/peps/pep-0557/

class Animal:
    name: str # A public modifier is a default
    sound: str
    _legs: int # A protected modifier has prefix of one (_)underscore.

class Dog(Animal):
    __iq = 20 # A private modifier has prefix of two (_) underscore.

if __name__ == "__main__":
    dog = Dog(name="Cremo", sound="bow", _legs=4)
    print(dog._legs)