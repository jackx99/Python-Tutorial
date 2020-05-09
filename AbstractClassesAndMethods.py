# Hi Enthusiast, You enjoy learning python
# Our topic is about Abstract Classes and Methods
# An abstract method is a method that has only the heading with no body. It is annotated of
# @abstractmethod and body contain the reversed word pass.
# Example of abstract methods:
# @abstractmethod
# def print(self):
#  pass
#
# @abstractmethod
# def larger(self, object, object):
#  pass
#
# @abstractmethod
# def insert(self, insertItem):
#  pass
#
# An abstract class is a class that inherits class ABC
# Facts about abstract classes:
#  It can contain variables, constructors, and nonabstract methods
#  It can contain an abstract method(s)
#  If a class contains an abstract method, then the class must extend from ABC
#  You cannot instantiate an object of an abstract class. You can only declare a reference variable
#  of an abstract class type
#  You can instantiate an object of a subclass of an abstract class, but only if the subclass gives the definitions
#  of all the abstract methods of the superclass
#
# Example of an abstract class:

from abc import (ABC, abstractmethod)

class AbstractClassExample(ABC):
    x = None

    @abstractmethod
    def print(self):
        pass

    def setX(self, a):
        self.x = a
    
    def __init__(self):
        self.x = 0

class InheritAbstractSuperClass(AbstractClassExample):
    
    def print(self):
        print(f'Value of x: {self.x}')

myClass = InheritAbstractSuperClass()
myClass.setX(2)
myClass.print()