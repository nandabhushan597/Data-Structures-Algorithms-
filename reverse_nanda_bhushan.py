"""
Reverse a simple list using just "empty", "head", and "rest" and other functions written here

Examples:

INCLUDE AT LEAST TWO TEST CASES FOR append(l, x) 

>>> print reverse(my_list())
[]
>>> print reverse(my_list().prepend(5))
[5]
>>> print reverse(my_list().prepend(5).prepend(3))
[5, 3]
>>> print reverse(my_list().prepend(5).prepend(3).prepend(16))
[5, 3, 16]

>>> print append(my_list(), 8) 
[8]

>>> print append(my_list().prepend(7).prepend(2), 10)
[2,7,10]



"""
import sys
sys.path.append('/home/courses/python')
from logic import *
from my_list import *


# append method 
# AXIOMS HERE
#       append(my_list(),x)         === x
#       append(my_list(h,r), x)     === my_list(h,append(r, x))
#Complexity: linear in number of items in a list and uses prepend function
def append(l, x):
    precondition(type(my_list()) == type(l))   #precondition that data type of my_list and l are the same 

    if l == my_list():                          
        return my_list().prepend(x)         
    else:
        return append(l.rest(), x).prepend(l.head())
    
#reverse method 
#AXIOMS HERE
#       reverse(my_list())          === my_list()
#       reverse(my_list(h,r)        === my_list append(reverse(r),h))
#Complexity: linear because depends on the length or number of items in a list and accesses append function
def reverse(l):
    """ replace this with your "reverse" function """
    precondition(type(my_list()) == type(l))    #precondition that data type of my_list and l are the same 

    if l == my_list():                          #if the list is empty return the list 
        return l
    else:
        return append(reverse(l.rest()), l.head()) #otherwise append the head to the reverse of the rest 

# The following gets the "doctest" system to check test cases in the documentation comments

def _test():
    import doctest
    return doctest.testmod()

if __name__ == "__main__":
    if _test()[0] == 0:
        print "Congratulations! You have passed all the tests"
