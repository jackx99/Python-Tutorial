# Hello Guys
# In our previous tutorials, we use methods that are already written and provided by Python.
# Today you will learn to write your own methods.
# They are like small program; you can put them together to form a larger program.
# Because Python is a dynamically-typed language that methods can be value-returning or void method
# Just be sure your method name are explicitly understood its purpose.
# Examples of prefix methods are 'is' (Asks for boolean return type), 'set' (Void method and has atleast one formal parameter),
# 'get' (Value-returning method)
# Syntax of the method
# def method_name(formal parameter list):
#  statement
# 
# Then method call
# method_name(actual parameter list)

"""
Write a value-returning method, isVowel, that returns the value true if a given character is vowel,
and otherwise returns false. Also write a program to test your method.
"""

# This is an example of value-returning method
def isVowel(char):
    vowels = ['a', 'e', 'i', 'o', 'u'] # here defined vowel in a form of list
    for c in vowels:
        if char == c: # then we check if char match any character from the vowel list
            return True
    return False

print(isVowel('u'))

"""
Write a method, reverseDigit, that takes an integer as a parameter and returns the
number with its digits reversed. For example, the value of reverseDigit (12345)
is (54321). Also, write a program to test your method.
"""

# This is an example of void method
def reverseDigit(numbers):
    numberInList = list(map(int, str(numbers))) # This operation is a bit complicated
    # It starts from inside nested parenthesis where variable numbers is converted to string object
    # then we map function to transform the string object to int finally return it as list
    length = len(numberInList)
    halfLength = length / 2 # we divide it to half so that swap of numbers are between first and end.
    count = 0
    while count < halfLength:
            lastIndex = count + 1
            first = numberInList[count]
            last = numberInList[-lastIndex] # we get the last element of the list by using negative number and
            # starts with -1
            numberInList[count] = last # here we swap first and last element
            numberInList[-lastIndex] = first
            count += 1

    print("Reversed Digits: " + str(numberInList))

digits = 123456789
print("Digit: " + str(digits))
reverseDigit(digits)