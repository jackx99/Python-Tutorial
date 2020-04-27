# Hello Guys
# When you know the program to use iterative way (while loop, for in loop) but there is a other way 
# Learn Recursion the process of solving a problem by reducing it to successively small versions of itself.
# Execute code by small chunks of itself. 
# Recursive definition has 
#  one or more base case(s)
#  the general case must eventually reduced to base case
#  the base case stops the recursion

"""
A palindrome is a string that reads the same both forward and backward. For example, 
the string "madam" is a palindrome. Write a program that uses a recursive method to check 
whether a string is a palindrome. Your program must contain a value-returning recursive method 
that returns true if the string is a palindrome and false otherwise. 
Use appropriate parameters in your method.
""" 

def is_palindrome(word):
    if len(word) == 0 or len(word) == 1: # The base case
        return True
    else: # The general case or recursive case
        if word[0] == word[len(word) - 1]: # We match first character and last character if evaluates to true
            return is_palindrome(word[1 : len(word) - 1]) # The word is reduced slicing the strings between first and end character 
            # then the function is_palindrome is called with new 'word' value
    return False # Otherwise the first character and end character is not equal and end the program

word = "level"
print(is_palindrome(word))