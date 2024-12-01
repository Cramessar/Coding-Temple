#lesson7

list_of_numbers = [3, 99, 12, 1, 7]

# in order to operate on an existing list, i.e to modify a list you need you 
# use that list as an argument in the function. so new list using existing list 
# define new list like def newlist(oldlist): 
def list_of_squares(list_of_numbers):
    squared_numbers = []  
    for num in list_of_numbers:  
        squared_numbers.append(num ** 2)  
    return squared_numbers  

print(list_of_squares(list_of_numbers))
