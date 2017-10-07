"""
my_list class:
    A simple list class with operations that can be performed quickly.
    By John Dougherty, possibly Kris Brower, Dave Wonnacott

Examples:
>>> print my_list()
[]

#PREPEND 
>>> print my_list().prepend(5)
[5]
>>> print my_list().prepend(5).prepend(3).prepend(16)
[16, 3, 5]

#EMPTY 
>>> print my_list().empty()
True

>>> print my_list().prepend(5).prepend(3).prepend(16).empty()
False

#HEAD & REST & SIZE 
>>> print my_list().prepend(5).prepend(3).prepend(16).head()
16

>>> print my_list().prepend(5).prepend(3).prepend(16).rest()
[3, 5]

>>> print my_list().prepend(5).prepend(3).prepend(16).rest().head()
3

>>> print my_list().prepend(5).prepend(3).prepend(16).size()
3

>>> print my_list().prepend(5).prepend(3).prepend(16).rest().size()
2

>>> print my_list().prepend(7)
7

>>> print my_list().prepend(7).prepend(8).prepend(9)
[9,8,7]

#EQUAL
>>> other_list = my_list()

>>> print my_list().prepend(5).prepend(3).prepend(16) == other_list.prepend(5).prepend(3).prepend(16)
True

>>> print my_list().prepend(5).prepend(3).prepend(16) == other_list.prepend(7).prepend(8).prepend(9)
False




"""
import sys
sys.path.append('/home/courses/python')
from logic import *


class my_list:

    # First, the constructors:
    #  A list is either empty, or an item followed by a list 

    # constructor: primitive (my_list()), creates an empty list 
    # Complexity: constant in terms of number of items in a list because a list is created once and remains
                # empty until methods are called to the list               
    def __init__(self):
        self.rep = []

    # constructor: prepending (my_list(l, x))
    # precondition: self must be a my_list (this has to be true in Python)
    # Complexity: linear in number of items in a list because run time increases as items are prepended 
    def prepend(self, x):       #prepend passes in primitive self and x to be prepended to the list 
        t = my_list()           #assign t to list 
        t.rep = [x] + self.rep #make t.rep variable equal to the item prepended and the original list 
        return t

    # Now the accessor functions:
    #  empty, head, rest, and equality checking
    #  Also, for convenience, a printing function

    #empty method 
    #axioms:
    #   empty(my_list())        === True
    #   empty(my_list(h, r))    === False
    # Complexity: constant in terms of number of items in a list 
    def empty(self):
        # REPLACE WITH YOUR CODE HERE
        return self.rep == []   #if the list is empty will return true 

    #head method 
    #   head(my_list())        === undefined (precondition out)
    #   head(my_list(h, r))    === h
    # Complexity: constant in number of items in list because there is always only one head
    def head(self):
        # REPLACE WITH YOUR CODE HERE
        precondition(not self.empty())  #precondition that list is not empty 
        return self.rep[0]              #returns first value or the head 

    #   rest method 
    #   rest(my_list())        === undefined (precondition out)
    #   rest(my_list(h, r))    === r
    # Complexity: linear in number of items in list because number of items in list can change 
    def rest(self):
        precondition(not self.empty())  #precondition that list is not empty 
        r = my_list()                   #make variable r equal to the list 
        r.rep = self.rep[1:]            #the representation of rest equal to the rest of the list 
        return r

    # equals method 
    # AXIOMS HERE:
    #  equals(my_list(), my_list()) === True
    #  equals(my_list(), my_list(l, x)) === False  
    #  equals(my_list(l, x), my_list(m, y))
    #   === x == y AND equals(l, m)
    # Complexity: linear in number of items in list 
    def __eq__(self, other):
        # REPLACE WITH YOUR CODE HERE
        return self.rep == other.rep

    # display (just uses built-in python operation)
    # Complexity: linear because depends on the length of list  
    def __str__(self):
        return str(self.rep)

    # abstraction (just uses built-in python operation)
    # Complexity: linear because depends on the length of list  
    def __repr__(self):
        return repr(self.rep)

    # size method 
    # AXIOMS HERE
    # size(my_list()) === 0
    # size(my_list(h, r)) === 1 + size(r)
    
    def size(self):
        # REPLACE WITH YOUR CODE HERE
        return len(self.rep)        #uses len function to determine size of the list 

# The following gets the "doctest" system to check test cases in the documentation comments

def _test():
    import doctest
    return doctest.testmod()

if __name__ == "__main__":
    if _test()[0] == 0:
        print "Congratulations! You have passed all the tests"
