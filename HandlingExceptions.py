# Hello Guys
# Today we're going to learn how to handle exceptions.
# So exception as an occurence of an undesirable situation that can be detected during program execution. Example of opening file but that file does not exist is an exception.
# until now we did not implemented any code to handle exceptions. If exceptions occurred during program execution, the program is terminated with appropriate error message.
# The general syntax of try/except/finally block
# try:
#    # statements
# except ExceptionClassName:
#    # exception handler code
# finally:
#    # statements
#
# Statements that might generate an exceptions are placed in try block. The try block might also contain statements that should not be executed if an exception occurs.
# The try block is followed by one or more except and contains an exception handler. any codes contained in finally block always executed, regardless of whether the exception occurs.
#
# Exception-handling techniques
#  1. Terminate the Program - Sometimes the best decision is to let the program terminate when an exception occurs.
# Suppose you wrote a program that inputs data from file. If the input file does not exist when the program
# executes, then there is no point of continuing with the program. Error message outputs and terminate.
#  2. Fix the Error and Continue - Other case, you want to handle exception and let the program continue.
# Suppose, you have program takes an input integer. If a user inputs a character in place of a digit, the program will throw an 
# ValueError. You prompt the user to input an integer again until entry is valid.
#  3. Log the Error and Continue - A program terminates when the an exception occurs usually assumes that a termination is reasonably safe.
# When a long-running server suddenly occur an exception, it cannot be terminated.

"""
Write a program that prompts the user to enter the length in feet and inches and outputs 
the equivalent length in inches and in centimeters. If the user enters a negative number or a nondigit number, 
throw and handle an appropriate exception and prompt the user to enter another set of numbers.
"""

import traceback # we imported this module to implement stacktrace to identify the error happened

completed = False
while not(completed):
    try:
        length_in_feet = int(input("Enter a measured number in Feet: "))
        length_in_inches = int(input("Enter a measured number in Inches: "))
        assert length_in_feet > 0 # we use assert keyword to check if entered value is valid entry.
        converted_in_inch = length_in_feet * 12
        converted_in_cm = length_in_inches * 2.54
        print(f'The entered measured number of length in feet: {length_in_feet}')
        print(f'The entered measured number of length in inches: {length_in_inches}')
        print(f'The converted length in feet to inches: {converted_in_inch}')
        print(f'The converted length in inches to centimeters: {converted_in_cm}')
        completed = True
    except AssertionError: # AssertionError, Description: Raised when an assert statement fails.
        # This exception is called when Line 39 fail to match
        print("The measured number is negative")
    except ValueError: # ValueError, Description: Raised when an operation or function receives an argument that 
        # has the right type but an inappropriate value, and the situation is not described by a more precise 
        # exception such as IndexError.
        # This exception is called when either Line 37 or 38 pass a nondigit.
        traceback.print_exc() # This prints the stack trace of the failed statement inside try block
        print("The measured number is nondigit")
