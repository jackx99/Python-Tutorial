# Hello Guys
# I am going to teach you creating a class by solving a problem set
# Its about Day Problem
# Let's start

"""
Design and implement the class Day that implements the day of the week in a program. 
The class Day should store the day, such as Sun for Sunday.The program should be able 
to perform the following operations on an object of type Day:
a.) Set the day.
b.) Print the day.
c.) Return the day.
d.) Return the next day.
e.) Return the previous day.
f.) Calculate and return the day by adding certain days to the current day. For example, 
if the current day is Monday and we four days, the day to be returned is Friday. Similarly, 
if today is Tuesday and we add 13 days, the day to be returned is Monday.
g.) Add the appropriate constructors.
h.) Write the definitions of the methods to implement the operations for the class Day, 
as defined in a through g.
i.) Write a program to test various operations on the class Day.
"""

# We have to create an enum for day of the week
# Let's use modules enum and datetime
from enum import Enum
from datetime import (datetime, timedelta)

# Let's create a class and inherit Enum so we use the implementation
# class <name>(SuperClass):
# SuperClass is called for a class that is extended by another class
class DayOfWeek(Enum):
    Mon = 'Monday'
    Tue = 'Tuesday'
    Wed = 'Wednesday'
    Thu = 'Thursday'
    Fri = 'Friday'
    Sat = 'Saturday'
    Sun = 'Sunday'

# Then we are going to create class Day
# class <name>:
class Day:

    # These are member of the class Day
    # None means null value
    # two underscore means private access modifier
    # private access variable can only be use, inside by its class
    __dayOfWeekArr = None # store the day of the week
    __day = None # store the day

    # Constructor
    # This is executed automatically whenever the class is created
    def __init__(self):
        self.__dayOfWeekArr = [
            DayOfWeek.Mon.value, # We get string value 'Monday' 
            DayOfWeek.Tue.value, 
            DayOfWeek.Wed.value,
            DayOfWeek.Thu.value,
            DayOfWeek.Fri.value,
            DayOfWeek.Sat.value,
            DayOfWeek.Sun.value
        ]
        self.__day = DayOfWeek.Mon.value # Set default value for variable day


    def setDay(self, day): # This is a mutator method because it modifies value(s) of one or more data member(s)
        self.__day = day
    
    def getDay(self): # This is a accessor method because only access the value(s) of the data member(s)
        self.__day
        
    def getPreviousDay(self):
        today_date = datetime.now() # Here we get current datetime
        previous_date = today_date - timedelta(days=1) # Then substract 1 day to current datetime
        dayOrdinal = previous_date.weekday() # Then we call weekday() which returns integer
        return self.__dayOfWeekArr[dayOrdinal] # Then access the list from integer we provided
        # It returns string value the day of the week

    def getNextDay(self):
        today_date = datetime.now()
        tomorrow_date = today_date + timedelta(days=1) # Here We Add 1 day
        dayOrdinal = tomorrow_date.weekday()
        return self.__dayOfWeekArr[dayOrdinal]

    def add(self, amount):
        today_date = datetime.now()
        new_date = today_date + timedelta(days=amount) # Here we can choose the amount we want to add days
        dayOrdinal = new_date.weekday()
        self.__day = self.__dayOfWeekArr[dayOrdinal] # Then pass the new value to day variable

    def __str__(self): # This is a magic method 
        # This method is to return string value
        # So if we print the object created this method is called
        return "The Day of the week: " + self.__day


if __name__ == "__main__":
    day = Day() # we create day object
    print("Yesterday: " + day.getPreviousDay()) # This is Accessing class members
    # referenceVariableName.memberName
    # dot . (period) is called as member access operator
    print("Tomorrow: " + day.getNextDay())
    day.add(5) # Here we add 5 days
    print(day) # Then class Day called __str__ magic method