# 3. What is an Interpreted language?
# An Interpreted language executes its statements line by line. Languages such as 
# Python, Javascript, R, PHP, and Ruby are prime examples of Interpreted languages.

# 4. What is PEP 8 and why is it important? 
# PEP stands for Python Enhancement Proposal. A PEP is an official design document 
# providing information to the Python community, or describing a new feature for 
# Python or its processes.

# 5. What is Scope in Python? 
# Every object in Python functions within a scope. A scope is a block of code where an 
# object in Python remains relevant.

# 6. What are lists and tuples? What is the key difference between the two? 
# Lists and Tuples are both sequence data types that can store a collection of objects 
# in Python. The objects stored in both sequences can have different data types. Lists 
# are represented with square brackets ['sara', 6, 0.19] , while tuples are 
# represented with parantheses ('ansh', 5, 0.97) . 
# But what is the real difference between the two? The key difference between the two 
# is that while lists are mutable, tuples on the other hand are immutable objects. 
# This means that lists can be modified, appended or sliced on the go but tuples 
# remain constant and cannot be modified in any manner.

# 7. What are the common built-in data types in Python?
# Numeric Types:
# There are three distinct numeric types - integers, floating-point numbers, and 
# complex numbers. Additionally, Booleans are a sub-type of integers.

# Sequence Types: 
# According to Python Docs, there are three basic Sequence Types - lists, tuples, and range objects.
# Mapping Types: 
# A mapping object can map hashable values to random objects in Python. Mappings 
# objects are mutable and there is currently only one standard mapping type, the dictionary.
# dict : Stores comma-separated list of key: value pairs
# Set Types:
# set : Mutable unordered collection of distinct hashable objects. 
# frozenset : Immutable collection of distinct hashable objects.

# 8. What is pass in Python?
# It is generally used for the purpose of filling up empty blocks of code which may execute during runtime but has yet to be written.

# 10. What are global, protected and private attributes in 
# Python?
# Global variables are public variables that are defined in the global scope. To use the variable in the global scope inside a function, we use the global keyword. 
# Protected attributes are attributes defined with an underscore prefixed to their identifier eg. _sara. They can still be accessed and modified from outside the class they are defined in but a responsible developer should refrain from doing so. 
# Private attributes are attributes with double underscore prefixed to their identifier eg. __ansh. They cannot be accessed or modified from the outside directly and will result in an AttributeError if such an attempt is made.

# 11. What is the use of self in Python?
# Self is used to represent the instance of the class. With this keyword, you can access the attributes and methods of the class in python.

# 12. What is __init__? 
# __init__ is a contructor method in Python and is automatically called to allocate 
# memory when a new object/instance is created.

# 13. What is break, continue and pass in Python?	
# Break :The break statement terminates the loop immediately and the control flows to the statement aȅ er the body of the loop. 
# Continue The continue statement terminates the current iteration of the statement, skips the rest of the code in the current iteration and the control flows to the next iteration of the loop. 
# Pass As explained above, the pass keyword in Python is generally used to fill up empty blocks and is similar to an empty statement represented by a semi-colon in languages such as Java, C++, Javascript, etc.

# 15. What is docstring in Python? 
# Documentation string or docstring is a multiline string used to document a specific code segment. 
# The docstring should describe what the function or method does.


# 18. What is the difference between Python Arrays and lists?
# Arrays in python can only contain elements of same data types i.e., data type of array should be homogeneous. It is a thin wrapper around C language arrays and consumes far less memory than lists. 
# Lists in python can contain elements of different data types i.e., data type of lists can be heterogeneous. It has the disadvantage of consuming large memory.

# 20. What are Python namespaces? Why are they used?
# A namespace in Python ensures that object names in a program are unique and can be used without any conflict.

# 22. What are decorators in Python? 
# Decorators in Python are essentially functions that add functionality to an existing function in Python without changing the structure of the function itself.

# # decorator function to convert to lowercase 
# def lowercase_decorator(function): 
# def wrapper(): 
# func = function() 
# string_lowercase = func.lower() 
# return string_lowercase 
# return wrapper 
# # decorator function to split words 
# def splitter_decorator(function): 
# def wrapper(): 
# func = function() 
# string_split = func.split() 
# return string_split 
# return wrapper 
# @splitter_decorator # this is executed next 
# @lowercase_decorator # this is executed first 
# def hello(): 
# return 'Hello World' 
# hello() # output => [ 'hello' , 'world' ]

# def names_decorator(function): 
# def wrapper(arg1, arg2): 
# arg1 = arg1.capitalize() 
# arg2 = arg2.capitalize() 
# string_hello = function(arg1, arg2) 
# return string_hello 
# return wrapper 
# @names_decorator 
# def say_hello(name1, name2): 
# return 'Hello ' + name1 + '! Hello ' + name2 + '!' 
# say_hello('sara', 'ansh') # output => 'Hello Sara
# 23. What are Dict and List comprehensions?
# Python comprehensions, like decorators, are syntactic sugar constructs that help build altered and filtered lists, dictionaries, or sets from a given list, dictionary, or set.
# Performing mathematical operations on the entire list
# my_list = [2, 3, 5, 7, 11] 
# squared_list = [x**2 for x in my_list] # list comprehension 
# # output => [4 , 9 , 25 , 49 , 121] 
# squared_dict = {x:x**2 for x in my_list} # dict comprehension 
# # output => {11: 121, 2: 4 , 3: 9 , 5: 25 , 7: 49}
# Performing conditional filtering operations on the entire list
# my_list = [2, 3, 5, 7, 11] 
# squared_list = [x**2 for x in my_list if x%2 != 0] # list comprehension 
# # output => [9 , 25 , 49 , 121] 
# squared_dict = {x:x**2 for x in my_list if x%2 != 0} # dict comprehension 
# # output => {11: 121, 3: 9 , 5: 25 , 7: 49}

# Combining multiple lists into one
# a = [1, 2, 3] 
# b = [7, 8, 9] 
# [(x + y) for (x,y) in zip(a,b)] # parallel iterators 
# # output => [8, 10, 12] 
# [(x,y) for x in a for y in b] # nested iterators 
# # output => [(1, 7), (1, 8), (1, 9), (2, 7), (2, 8), (2, 9), (3, 7), (3, 8), (3, 9)]

# 24. What is lambda in Python? Why is it used? 
# Lambda is an anonymous function in Python, that can accept any number of
# arguments, but can only have a single expression.
# mul = lambda a, b : a * b 
# print(mul(2, 5)) #

# def myWrapper(n): 
# return lambda a : a * n 
# mulFive = myWrapper(5) 
# print(mulFive(2))


# 29. What is PYTHONPATH in Python? 
# PYTHONPATH is an environment variable which you can set to add additional directories where Python will look for modules and packages.

# 31. What is the difference between .py and .pyc files? 
# .py files contain the source code of a program. Whereas, .pyc file contains the bytecode of your program. We get bytecode after compilation of .py file (source code). .pyc files are not created for all the files that you run. It is only created for the files that you import.
# Before executing a python program python interpreter checks for the compiled files. If the file is present, the virtual machine executes it. If not found, it checks for .py file. If found, compiles it to .pyc file and then python virtual machine executes it. 
# Having .pyc file saves you the compilation time.

# 34. What are iterators in Python?
# An iterator is an object.
# __iter__() method initializes an iterator. 
# It has a __next__() method which returns the next item in iteration and points to the next element. Upon reaching the end of iterable object __next__() must return StopIteration exception.

# class ArrayList: 
# def __init__(self, number_list): 
# self.numbers = number_list 
# def __iter__(self): 
# self.pos = 0 
# return self 
# def __next__(self): 
# if(self.pos < len(self.numbers)): 
# self.pos += 1 
# return self.numbers[self.pos - 1] 
# else:
# raise StopIteration 

# array_obj = ArrayList([1, 2, 3]) 
# it = iter(array_obj) 
# print(next(it)) #output: 2 
# print(next(it)) #output: 3 
# print(next(it)) 
# #Throws Exception 
# #Traceback (most recent call last): 
# #... 
# #StopIteration


# 36. Explain split() and join() functions in Python? 
# You can use split() function to split a string based on a delimiter to a list of strings. 
# You can use join() function to join a list of strings based on a delimiter to give a single string

# 37. What does *args and **kwargs mean? 
# *args
# *args is a special syntax used in the function definition to pass variable-length arguments. 
# “*” means variable length and “args” is the name used by convention. You can use any other

# def multiply(a, b, *argv): 
# mul = a * b 
# for num in argv: 
# mul *= num 
# return mul 
# print(multiply(1, 2, 3, 4, 5)) #output: 120



# **kwargs

# **kwargs is a special syntax used in the function definition to pass variable- length keyworded arguments. 
# Here, also, “kwargs” is used just by convention. You can use any other name. 
# Keyworded argument means a variable that has a name when passed to a function. 
# It is actually a dictionary of the variable names and its value


def tellArguments(**kwargs):
    for key, value in kwargs.items(): 
        print(key + ": " + value) 
        tellArguments(arg1 = "argument 1", arg2 = "argument 2", arg3 = "argument 3") 
#output: 
# arg1: argument 1 
# arg2: argument 2 
# arg3: argument 3


# Python OOPS Interview Questions 
# 39. How do you create a class in Python?
class InterviewbitEmployee: 
    def __init__(self, emp_name): 
        self.emp_name = emp_name 
    def introduce(self): 
        print("Hello I am " + self.emp_name) 
# create an object of InterviewbitEmployee class 
emp_1 = InterviewbitEmployee("Mr Employee") 
print(emp_1.emp_name) #print employee name 
emp_1.introduce() #introduce the employee

"""40. How does inheritance work in python? Explain it with an example.
Inheritance gives the power to a class to access all attributes and methods of another class."""


#Single Inheritance:

class ParentClass: 
    def par_func(self):
        print("I am parent class function")
# Child class 
class ChildClass(ParentClass):
    def child_func(self):
        print("I am child class function")
# Driver code 
obj1 = ChildClass()
obj1.par_func()
obj1.child_func()


#Multi-level Inheritance:

class A:
    def __init__(self, a_name):
        self.a_name = a_name
# Intermediate class 
class B(A):
    def __init__(self, b_name, a_name):
        self.b_name = b_name
        #invoke constructor of class A 
        A.__init__(self, a_name)
# Child class 
class C(B):
    def __init__(self,c_name, b_name, a_name):
        self.c_name = c_name # invoke constructor of class B 
        B.__init__(self, b_name, a_name)
    
    def display_names(self):
        print("A name : ", self.a_name)
        print("B name : ", self.b_name)
        print("C name : ", self.c_name)
# Driver code
obj1 = C('child', 'intermediate', 'parent')
print(obj1.a_name)
obj1.display_names()


#Multiple Inheritance:

class Parent1:
    def parent1_func(self):
        print("Hi I am first Parent")
# Parent class2 
class Parent2:
    def parent2_func(self):
        print("Hi I am second Parent")
        
# Child class 
class Child(Parent1, Parent2):
    def child_func(self):
        self.parent1_func()
        self.parent2_func()
        
# Driver's code 
obj1 = Child()
obj1.child_func()

"""Hierarchical Inheritance:
When a parent class is derived by more than one child class, it is called hierarchical inheritance."""

class A:
    def a_func(self):
        print("I am from the parent class.")
        # 1st Derived class
class B(A):
    def b_func(self):
        print("I am from the first child.")
        
# 2nd Derived class 
class C(A):
    def c_func(self):
        print("I am from the second child.")
# Driver's code 
obj1 = B()
obj2 = C()
obj1.a_func()
obj1.b_func()#child 1 method
obj2.a_func()
obj2.c_func()#child 2 method


"""41. How do you access parent members in the child class?

By using Parent class name: You can use the name of the parent class to access the attributes as shown in the example below:"""

class Parent(object):
    # Constructor
    def __init__(self, name):
        self.name = name 
class Child(Parent):
    # Constructor
    def __init__(self, name, age):
        Parent.name = name
        self.age = age
        def display(self):
            print(Parent.name, self.age)
# Driver Code 
obj = Child("Interviewbit", 6)
obj.display()

"""By using super():
The parent class members can be accessed in child class using the super keyword."""

class Parent(object):
    # Constructor
    def __init__(self, name):
        self.name = name

class Child(Parent):
    # Constructor
    def __init__(self, name, age):
        ''' In Python 3.x, we can also use super().__init__(name) '''
        super(Child, self).__init__(name)
        self.age = age
    def display(self):
        # Note that Parent.name cant be used
        # # here since super() is used in the constructor
        print(self.name, self.age)
        # Driver Code
obj = Child("Interviewbit", 6)
obj.display()


"""42. Are access specifiers used in python?
Python does not make use of access specifiers specifically like private, public, protected"""

class InterviewbitEmployee:
    # protected members
    _emp_name = None
    _age = None
    # private members
    __branch = None
    # constructor
    def __init__(self, emp_name, age, branch):
        self._emp_name = emp_name
        self._age = age
        self.__branch = branch
        #public member
    def display():
        print(self._emp_name + " " + self._age + " "+ self.__branch)


"""47. What is init method in python?"""
class InterviewbitEmployee:
    # init method / constructor
    def __init__(self, emp_name):
        self.emp_name = emp_name
    # introduce method
    def introduce(self):
        print('Hello, I am ', self.emp_name)
emp = InterviewbitEmployee('Mr Employee') # __init__ method is called here and initi 
emp.introduce()


"""48. How will you check if a class is a child of another class?"""

class Parent(object):
    pass 
class Child(Parent):
    pass
# Driver Code
print(issubclass(Child, Parent)) #True
print(issubclass(Parent, Child)) #False
obj1 = Child()
obj2 = Parent()
print(isinstance(obj2, Child)) #False
print(isinstance(obj2, Parent)) #True


"""Python Libraries Interview Questions 
70. Differentiate between a package and a module in python."""

"""The module is a single python file.
A module can import other modules (other python files) as objects.

Whereas, a package is the folder/directory where different sub- packages and the modules reside."""


"""71. What are some of the most commonly used built-in modules in Python?"""
"""osmath
sys
random
re
datetime
JSON"""

"""72. What are lambda functions?"""
mul_func = lambda x,y : x*y
print(mul_func(6, 4)) # Output: 24

"""74. Can you easily check if all characters in the given string is alphanumeric?"""
"abdc1321".isalnum() #Output: True 
"xyz@123$".isalnum() #Output: False

import re 
print(bool(re.match('[A-Za-z0-9]+$','abdc1321'))) # Output: True
print(bool(re.match('[A-Za-z0-9]+$','xyz@123$'))) # Output: False


"""81. What is main function in python? How do you invoke it?"""
"""the main is considered as an entry point of execution for a program."""
"""This can be done by defining user-defined main() function and by using the __name__ property of python file.
This __name__ variable is a special built-in variable that points to the name of the current module."""


def main():
    print("Hi Interviewbit!")

if __name__=="__main__":
    main()

"""83. WAP (Write a program) which takes a sequence of numbers and check if all numbers are unique."""

def check_distinct(data_list):
    if len(data_list) == len(set(data_list)):
        return True
    else:
        return False
print(check_distinct([1,6,5,8])) #Prints True 
print(check_distinct([2,2,5,5,7,8])) #Prints False


"""84. Write a program for counting the number of every character of a given text file."""
import collections
import pprint
with open("sample_file.txt", 'r') as data:
    count_data = collections.Counter(data.read().upper())
    count_value = pprint.pformat(count_data)
    print(count_value)


"""85. Write a program to check and return the pairs of a given array A whose sum value is equal to a target value N."""
def print_pairs(arr, N):
    # hash set 
    hash_set = set()
    for i in range(0, len(arr)):
        val = N-arr[i]
        if (val in hash_set): #check if N-x is there in set, print the pair
            print("Pairs " + str(arr[i]) + ", " + str(val))
            hash_set.add(arr[i])
            # driver code
arr = [1, 2, 40, 3, 9, 4]
N = 3
print_pairs(arr, N)

"""86. Write a Program to add two integers >0 without using the plus operator."""
def add_nums(num1, num2):
    while num2 != 0:
        data = num1 & num2
        num1 = num1 ^ num2
        num2 = data << 1
    return num1
print(add_nums(2, 10))

"""88. Write a Program to match a string that has the letter ‘a’ followed by 4 to 8 'b’s."""

import re 
def match_text(txt_data):
    pattern = 'ab{4,8}' 
    if re.search(pattern, txt_data): 
        #search 
        for pattern in txt_data:
            return 'Match found'
    else:
        return('Match not found')
print(match_text("abc")) #prints Match not found
print(match_text("aabbbbbc")) #prints Match found


"""89. Write a Program to convert date from yyyy-mm-dd format to dd-mm-yyyy format."""
import re
def transform_date_format(date):
    return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', date)
date_input = "2021-08-01"
print(transform_date_format(date_input))

from datetime import datetime
new_date = datetime.strptime("2021-08-01", "%Y-%m-%d").strftime("%d:%m:%Y")
print(new_data)

"""90. Write a Program to combine two different dictionaries.
While combining, if you find the same keys, you can add the values of these same keys.
Output the new dictionary"""

from collections import Counter
d1 = {'key1': 50, 'key2': 100, 'key3':200}
d2 = {'key1': 200, 'key2': 100, 'key4':300}
new_dict = Counter(d1) + Counter(d2)
print(new_dict)


"""91. How will you access the dataset of a publicly shared spreadsheet in CSV format stored in Google Drive?"""
from io import StringIO
import pandas
csv_link = "https://docs.google.com/spreadsheets/d/..."
data_source = StringIO.StringIO(requests.get(csv_link).content)
dataframe = pd.read_csv(data_source)
print(dataframe.head())