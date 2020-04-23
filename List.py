# Hello Guys
#
# The general form to declare a one dimensional list
# list = [] # empty list
#
# The general form (syntax) used to access an list element
# list[index]
# index is an expression whose value is non-negative integer and less than the size of the list
#
# List Initialization
# list = ['apple', 'orange', 'kiwi', 'peach', 'watermelon']
# initializer list contains a initial values that are placed between square brackets
# and separated by commas.
#
# Index Error: list index out of range
# index = 0
# list = ['apple', 'orange', 'kiwi', 'peach', 'watermelon']
# while index <= len(list):
#     print(str(list[index]))
#     index += 1
# Here we have a list that has 5 elements. When index becomes 5, the loop
# test condition index <= len(list) check if true, the body of the loop executes, and the program
# to access list[5] which does not exist.


"""
Write a Python method, lastLargestIndex, that takes as parameters an int list and
returns the index of the last occurence of the largest element in the list. 
Also, write a program to test your method.
"""

def lastLargestIndex(list):
    largestElement = 0
    lastOccurenceIndex = 0
    count = 0
    while count < len(list):
        if list[count] > largestElement:
            largestElement = list[count]
            lastOccurenceIndex = count
        count += 1
    return lastOccurenceIndex

num = [4, 1, 23, 56, 120, 3, 5, 29]
print("lastLargestIndex: " + str(lastLargestIndex(num)))
        

"""
Write a program that uses the class RollDie to roll a pair of dice 1000 times 
( or 10000 pairs of dice). The program then outputs the pair of numbers rolled by the dice, 
the sum of the numbers rolled by each pair of dice, the number of times each sum is rolled,
and the sums that are rolled the maximum number of times. (Use a two-dimensional list to 
create 1000 pairs of dice and to store the pairs of numbers rolled by each pair of dice.)
"""

# output 
# the pair of numbers rolled by the dice
# the sum of the numbers rolled by each pair of dice

# the number of times each sum is rolled
# the sums that are rolled the maximum number of times -> 1000 times = sum of it

import random

class RollDie:

    __dice_list = []
    __times = None

    def __init__(self, times):
        self.__times = times

    def roll(self):
        for _ in range(0, self.__times): # The (_) underscore ignores the iterate value of the loop
            first_dice = random.randint(1, 100)
            second_dice = random.randint(1, 100)
            self.__dice_list += [[first_dice, second_dice]] # Here we add new two-dimensional array 
        print("Pair of Dice: " + str(self.__dice_list))
    
    def sumOfEachPairDice(self):
        for index, dice in enumerate(self.__dice_list, start=1): # We use enumerate instead of for in loop because we need 
            # to access the index value
            print("Sum of Dice {0}: ". format(index) + str(dice[0] + dice[1]))
    
    
    def numberOfTimesEachSum(self):
        print("Number of times for each sum: " + str(self.__times))
        
    def sumOfAllRolledPairDice(self):
        sum = 0
        for dice in self.__dice_list:
            sum += dice[0] + dice[1]
        print("The sum of all rolled pair dice: " + str(sum))

number_to_roll = int(input("Enter the number of times to roll the dice: "))
roll_die = RollDie(number_to_roll)
roll_die.roll()
roll_die.sumOfEachPairDice()
roll_die.numberOfTimesEachSum()
roll_die.sumOfAllRolledPairDice()

