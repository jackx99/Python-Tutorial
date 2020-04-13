"""
Write a program that prompts the user to input an integer and then outputs both
the individual digits of the number and the sum of the digits. For example, 
the program should: output the individual digits of 3456 as 3 4 5 6 and the sum as 18.
"""
print("While Loop")
number = input("Enter a numbers: ")
sum = 0
count = 0 # initialize the loop control variable(s)
while count < len(number): # expression test the loop control variable
 print(number[count], end = ' ') # end argument flag the statement without newline
 sum += int(number[count])
 count+=1 # update the loop control variable(s)
print()
print("The sum of the digits: " + str(sum))

"""
Write a Python method, lastLargestIndex, that takes as its parameters an int array 
and returns the index of the last occurence of the largest element in the array.
Also, write a program to test your method.
"""
print()
print("For Loop")
num_arr = [34, 6, 25, 50, 76, 100, 325, 225, 312]

def lastLargestIndex(arr):
    largest = 0
    for number in arr:
        if number > largest:
            largest = number
    return largest

print(num_arr)
print("The largest element in the array: " + str(lastLargestIndex(num_arr)))