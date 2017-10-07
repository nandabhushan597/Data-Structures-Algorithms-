"""
Determine whether or not a list is a "palindrome"

Examples:
>>> print palindrome(my_list().prepend(5).prepend(3).prepend(16))
False
>>> print palindrome(my_list().prepend(16).prepend(3).prepend(16))
True

"""
import sys
sys.path.append('/home/courses/python')
from logic import *
from my_list import *
from reverse_lab_2 import *

#axioms
#   palindrome(my_list())                             === my_list() 
#   palindrome(my_list(l,x))                          === my_list(x,l)
#   palindrome(my_list(h, r))                         === my_list(reverse(r),append(h))     

#   Complexity: linear in terms of number of items in a list and uses the reverse function 
def palindrome(l):
    """ replace this with your "palindrome" function """
    precondition(type(my_list()) == type(l))    #precondition that datatype of my_list and l are equal

    return l == reverse(l)                      #returns true if l and the reverse of l are equal 
        
# The following gets the "doctest" system to check test cases in the documentation comments

def _test():
    import doctest
    return doctest.testmod()

if __name__ == "__main__":
    if _test()[0] == 0:
        print "Congratulations! You have passed all the tests"
