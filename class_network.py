""" Test Cases so far -- jd

# read in and generate the graph representing the courses-students
>>> CN = ClassNetwork()

# ClassNetwork.StudentCount(course)

>>> print CN.StudentCount("cmsc106")

>>> assert CN.StudentCount("cmsc106") == 39    # counting everyone!

# ClassNetwork.CourseCount(course) 
>>> course = "cmsc106"
>>> assert CN.CourseCount(course) == 37*4 + 2*2
>>> print CN.CourseCount("cmsc106")

# X.Roster(CN)
>>> jd = Student("Dougherty", "John", "green")
>>> assert jd.Roster(CN) == Roster(["cmsc106", "cmsc287"])

# X.Shared(CN, Y)
>>> sl = Student("Lindell", "Suzanne", "blue")  # if blue is Suzanne's color!
>>> assert jd.Shared(CN, sl) == Roster(["cmsc106"])

# ClassNetwork.Popular()
>>> assert CN.Popular() == "cmsc106"

# ClassNetwork.Second()
>>> assert CN.Second() == "???" # whatever the second most popular is in the list

# ClassNetwork.CourseColor(course)
>>> assert CN.CourseColor("cmsc106") == "green"    # assuming green is most popular
"""
#LAB 6
#INTRO TO DATA STRUCTURES
#PROF JD SPRING 2017

import pprint       # just to make the list easier to read
import csv

ClassList = []      # an empty list to be filled from class.csv file

with open('class.csv', 'rb') as f:  # access local file 'class.csv'
    reader = csv.reader(f)          # connects reader object to file
    for row in reader:              # reads one text line at a time
        ClassList += [row]          # .. and appends to the ClassList
    #pprint.pprint(ClassList)        # confirm the file reading process
    
    
def list(ClassList):     
    for n in range(len(ClassList)):
        if ClassList[n][0] != lastname and ClassList[n][1] != firstname and ClassList[n][3] != Color:
            studentlist += [lastname, firstname, color]
        else:
            studentList = [[ClassList]]
                   
class Student:
    def __init__(self, firstname, lastname, color): #contstructor/paramaters for student are firstname, lastname, & color 
        self.firstname = firstname                  #declare instance variables 
        self.lastname = lastname
        self.color = color
        self.roster = []
        self.rep = str(firstname) + str(lastname) + str(color) 
 
    
    def __repr__(self): 
        return str(self.firstname + self.lastname + self.color) #representation of student as firstname, lastname, color or all attributes 
        
    def Roster(self, ClassNetwork):                 #Roster Method 
        self.roster = ClassNetwork.graph[self.rep]  #roster equals ClassNetwork.graph[self.rep] or the list of values or classes a student or key has            
        return self.roster
            
    def Shared(self,other):             
        for n in range(len(self.roster)):           #loop through roster 
            if self.Roster()[i] in other.Roster():  #if one class is in another roster, return that specific class meaning there is shared class 
                return self.Roster()[i]
            else:
                return None 
        
    
class Roster:
    def __init__(self, course): #constructor
        self.rep = []                     #constructs new list, roster is a list of all classes
        
    def courses(self, course):
        self.rep.append(course)           #appends courses to list, appends courses to self.rep 

    def __repr__(self):             
        return self.rep                   #returns list of courses
    
    def __len__(self):                    #wrote this method because continued to receive a length error message
        return len(self.rep) 
        

class ClassNetwork:
    def __init__(self):
        
        self.ClassList = []  
        with open('class.csv', 'rb') as f:
            reader = csv.reader(f)
            for row in reader:
                self.ClassList += [row]
        #reimported ClassList againt
        #empty list completed by csv file 
                
        #declares self.graph as a dictionary
        #construct a dictionary D = (student : roster)
        #                       D = (course : students)
        
        self.graph = dict()

        #loop through classlist 
        for n in self.ClassList:
            course = n[2]                       #course equals row with index 2/all courses 
            student = Student(n[0], n[1], n[3]) #student equals attributes/index 0,1,3 or lastname,firstname, and color 
            roster = Roster(n[2])               #roster equals row with index 2/all respective courses 
            if course not in self.graph.keys(): #creates new key + value if key not present in ClassNetwork if the course is not in the dictionary keys, add one student to the class 
                self.graph[course] = [student]  #adds new student to course if key is already present in ClassNetwork 
            else:
                self.graph[course] += [student] #if the course is already in the graph, add the student attributes/information  
                
        for n in self.ClassList:
            student= Student(n[0], n[1], n[3])
            roster = Roster(n[2]) 
            if student not in self.graph.keys(): #if the student is not in the dictionary keys, add their classes 
                self.graph[student.rep] = roster 
            else:                               #if the student is already in the graph, add their class 
                self.graph[student.rep].rep += roster.rep   
                
        def __repr__(self):
            return str(self.graph)
        
 
    
    def StudentCount(self, course): 
        count = len(self.graph[course]) #returns the length or number of values for course or key pair 
        return count 
    
    def CourseCount(self,course):
        count = 0
        for student in self.graph[course]: #loop thaat parses through each student in a course 
            count += len(self.graph[student.rep]) #add or increment number of courses for each student 
        return count
    
    def Second(self):                       #this code is taken from the popular method and reformatted to fit second most popular/repeat for loops but do not allow secondmostpopular to equal mostpopular
        secondmostpopular = ""              #declare secondmostpopular as an empty string
        mostpopular = ""                    #declare mostpopular as empty string  
        size_mostpopular = 0                #size_mostpopular counter starts at 0 
        for i in range(len(self.graph())):  #for loop that parses through the graph
            if len(self.graph[course]) == size_mostpopular: #if the number of students == 0 or any number x, add course to empty string 
                mostpopular += "," + course
            elif len(self.graph[course]) > size_mostpopular: #if the number of students is greater than 0 or any number x, this course now becomes the most popular course
                mostpopular = course
        return mostpopular
                                            #function finds the most popular but the next most popular with second for loop 

        size_secondmostpopular = 0          #size_secondmostpopular counter starts at 0 
        for i in range(len(self.graph())):  #for loop that parses through graph 
            if str(course) != str(mostpopular):     #if the course does not equal the most popular allow the for loop to run to find the second most popular course 
                for i in range(len(self.graph())):  
                    if len(self.graph[course]) == size_secondmostpopular:
                        mostpopular += "," + course
                    elif len(self.graph[course]) > size_secondmostpopular:
                        mostpopular = course
                return secondmostpopular
    
    def Popular(self):                      #same logic as Second 
        mostpopular = ""                    #mostpopular is empty string or name of course        
        size_mostpopular = 0                #counter of size of class/number of students starts at 0 
        for i in range(len(self.graph())):  #for loop parses through graph 
            if len(self.graph[course]) == size_mostpopular: #if the number of students equals 0, add the course to empty string 
                mostpopular += "," + course
            elif len(self.graph[course]) > size_mostpopular: #if the number of students greater than 0 or updated size_mostpopular, this becomes the mostpopular course 
                mostpopular = course
        return mostpopular  
        
    def CourseColor(self,listed_course):
    
        FavColor = dict()      #create a dictionary of favorite colors
                               #if the target course or if course being looked for is equal to the course, parse through the graph
        for course in self.graph:
            if listed_course == course:
                for student in self.graph[course]: #for each student in a course if their favorite color is not in the FavColor dictionary, add 1 as a value pair to add that that student has a unique favorite color 
                    if self.color not in FavColor:
                        FavColor[self.color] = 1
                    else:                           #if that color is already in there, increment the value pair 
                        FavColor[self.color] += 1
        numberofcolors = 0
        for i in range(len(self.color())):          #parse through self.color dictionary 
            if FavColor[self.color] == numberofcolors: #if the value pair equals 0 or any number x, keep incrementing through self.color
                numberofcolors += self.color[i]
            elif len(self.color) > numberofcolors:      #if the vlaue pair is greater than 0 or any number x, the most popular course color is updated  
                numberofcolors = FavColor               #uses the same logic as popular and second 
        return FavColor  
                   

def _test():
        import doctest
        return doctest.testmod()

if __name__ == "__main__":
    if _test()[0] == 0:
        print "Congratulations! You have passed all the classnetwork tests"
                

