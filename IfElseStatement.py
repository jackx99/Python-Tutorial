"""
In a right triangle, the square of the length of one side is equal to
the sum of the squares of the lengths of the other two sides. Write a program
that prompts the user to enter the lengths of three sides of a triangle and then outputs
a message indicating whether the triangle is a right triangle.
"""

side1 = int(input("Enter side1: "))
side2 = int(input("Enter side2: "))
side3 = int(input("Enter side3: "))

if (side1**2 + side2**2) == (side3**2):
    print("Its a right triangle.")
else:
    print("Its not a right triangle.")