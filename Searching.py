# Hello Guys
# Today lesson to learn Search. We are going to apply simple algorithm, that is sequential search algorithm.
# It makes two key comparisons to determine whether the search item is in the list.

"""
Write a method, remove, that takes three parameters: a list of integers, the length of the list,
and an integer, say, removeItem. The method should find and delete the first occurence of removeItem
in the list. If the value does not exist or the list is empty, output an appropriate message. (Note
that after deleting the element, the list size is reduced by 1.) You may assume that the list is
unsorted.
"""

def remove(list, list_length, removeItem):
    for key, value in enumerate(list): # We can access index or subscript of a list by using enumerate function
        if removeItem == value: # Here we match iterate value to our remove item if evaluates to true,
            list[key] = None # replace the value of None,
            list = [value for value in list if value] # Here we create a new list and filter the element with None value
            print(f'The list after removing the item {removeItem}: {list}.')
            return # We call return statement to end the execution of the program
    print("The list did not find the item to remove.")

list = [71, 29, 67, 18, 92, 4, 49, 48, 86, 40]
item = 18
print(f'The list before removing the item {item}: {list}')
remove(list, len(list), item) # List, Size of the list, Item to remove
