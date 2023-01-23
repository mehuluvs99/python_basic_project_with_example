# # https://www.w3resource.com/python-exercises/python-basic-exercises.php
# import datetime
# print(datetime.datetime.now())

"""Write a Python program that accepts the user's first
and last name and prints them in reverse order with a space between them."""
import os

# print(input("First name"), input("Last Name"))

"""Write a Python program that accepts a sequence of 
comma-separated numbers from the user and generates a list and a tuple of those numbers"""

# x = input("Enter Number using comma").split(",")
# z = tuple(x)
# print(x, z)

"""8. Write a Python program to display the first and last colors from the 
following list. color_list = ["Red","Green","White" ,"Black"]"""

# color_list = ["Red","Green","White" ,"Black"]
# print("%s %s"%(color_list[0],color_list[-1]))

"""
9. Write a Python program to display the examination schedule. (extract the date from exam_st_date). 
"""

# exam_st_date = (11, 12, 2014)
# print("%i/%i/%i"%(exam_st_date))

"""10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn."""
# Sample value of n is 5

# a = int(input("Input an integer : "))
# n1 = int( "%s" % a )
# n2 = int( "%s%s" % (a,a) )
# n3 = int( "%s%s%s" % (a,a,a) )
# print (n1+n2+n3)

"""Write a Python program to calculate the number of days between two dates."""
"""Sample dates : (2014, 7, 2), (2014, 7, 11)"""

# from datetime import date
# Sample_dates = date(2014, 7, 2)
# Sample_dates1 = date(2014, 7, 11)
# delta = Sample_dates - Sample_dates1

# print(delta.days)

"""Write a Python program to calculate the difference between a given number and 17.
If the number is greater than 17, return twice the absolute difference."""

# x = int(input("Enter Number:"))

# if x <= 17:
#     print(17-x)
# else:
#     print((x-17)*2)

"""Write a Python program to test whether a number is within 100 of 1000 or 2000."""
# def near_thousand(n):
#       return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))
# print(near_thousand(1000))
# print(near_thousand(900))
# print(near_thousand(800))   
# print(near_thousand(2200))


"""Write a Python program to calculate the sum of three given numbers.
If the values are equal, return three times their sum."""

# a,b,c = int(input("Enter Number 1 : ")), int(input("Enter Number 2 : ")), int(input("Enter Number 3 : "))
# if a==b==c:
#     print((a+b+c)*3)
# else:
#     print(a+b+c)

# def x(a,b,c):
#     sum = a+b+c

#     if a==b==c:
#         sum = sum*3
#     return sum

# print(x(1,2,3)) 

"""
 Write a Python program to get a newly-generated string from a given string where "Is" has been added to the front.
 Return the string unchanged if the given string already begins with "Is"""

# def s(st):
#     if st[:2] == "Is":
#         return st
#     return "Is"+st
# print(s("IsEmply"))
# print(s("Array"))

"""Write a Python program that returns a string that is n (non-negative integer) copies of a given string."""

# def large_string(s,n):
#     result = ''
#     for i in range(n):
#         result = result+s
#     return result

# print(large_string("abc",2))
# print(large_string(".py",3))


"""Write a Python program that determines whether a given number (accepted from the user) is even or odd, and prints an appropriate message to the user."""

# n = int(input("Enter Number  "))
# if (n % 2) < 0:
#     print("Even")
# else:
#     print("odd")

"""Write a Python program to count the number 4 in a given list."""

# def l(search,arr):
#     count = 0
#     for i in arr:
#         if search == i:
#             count +=1
#     return count
# m = l(4,[1,4,1,2,4,6,7,9,4])
# print(m)


"""Write a Python program to get n (non-negative integer) copies of the first 2 characters of a given string.
Return n copies of the whole string if the length is less than 2"""

# def substring_copy(text, n):
#   flen = 2
#   if flen > len(text):
#     flen = len(text)
#   substr = text[:flen]
#   result = ""
#   for i in range(n):
#     result = result + substr
#   return result
# print(substring_copy('abcdef', 2))
# print(substring_copy('p', 3))


"""Write a Python program to test whether a passed letter is a vowel or not"""

# def letter(search):
#     text = "aeiou"
#     for i in text:
#         if search == i:
#             return True
#     return False


# print(letter("i"))
# print(letter("c"))

"""Write a Python program that checks whether a specified value is contained within a group of values."""

# def letter(text, search):

#     for i in text:
#         if search == i:
#             return True
#     return False


# print(letter([1,5,8,3],3))
# print(letter([1,5,8,3],-1))

"""Write a Python program to create a histogram from a given list of integers."""

# def histogram(x, y):
#     for i in y:
#         print(i)
#         return str(x) * i, end("\n")
#
#
# print(histogram("#", [2, 3, 6, 5]))

"""Write a Python program that concatenates all elements in a list into a string and returns it."""

# def con(concatinate):
#     result = ""
#     for i in concatinate:
#         result += str(i)
#     return result
#
# print(con([1,2,3,5,4]))

"""Write a Python program to print all even numbers from a given list 
of numbers in the same order and stop printing any after 237 in the sequence."""

#
# def n(number, stop):
#     for i in number:
#         if i == stop:
#             print(i)
#             break
#
#         if (i % 2) == 0:
#             print(i)
#
#
# numbers = [
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
#     958, 743, 527
# ]
# n(numbers, 237)

"""Write a Python program that prints out all colors from 
color_list_1 that are not present in color_list_2"""

#
# def color(a, b):
#     Differenct1_2 = []
#     Differenct2_1 = []
#
#     for i in a:
#         for j in b:
#             if i != j:
#                 Differenct1_2.append(i)
#             else:
#                 Differenct2_1.append(j)
#     d1 = []
#     d2 = []
#     for d in Differenct1_2:
#         for k in Differenct2_1:
#             if d != k:
#                 d1.append(d)
#             else:
#                 d2.append(d)
#
#     print("Differenct1_2 : ", set(Differenct1_2))
#     print("Differenct2_1 : ", set(Differenct2_1))
#     print()
#     print("Differenct1_2 : ", set(d1))
#     print("Differenct2_1 : ", set(d2))
#
#
# color_list_1 = ["White", "Black", "Red"]
# color_list_2 = ["Red", "Green"]
#
# color(color_list_1, color_list_2)
#
# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])
# print("Original set elements:")
# print(color_list_1)
# print(color_list_2)
# print("\nDifferenct of color_list_1 and color_list_2:")
# print(color_list_1.difference(color_list_2))
# print("\nDifferenct of color_list_2 and color_list_1:")
# print(color_list_2.difference(color_list_1))

"""Write a Python program that will accept the base and height of a triangle and compute its area."""

# b = int(input("Input the base : "))
# h = int(input("Input the height : "))
#
# area = b*h/2
#
# print("area = ", area)

"""Write a Python program that computes the greatest common divisor (GCD) of two positive integers."""

# def gcd(x, y):
#    gcd = 1
#    if x % y == 0:
#        return y
#    for k in range(int(y / 2), 0, -1):
#        if x % k == 0 and y % k == 0:
#            gcd = k
#            break
#    return gcd
# print("GCD of 12 & 17 =",gcd(12, 17))
# print("GCD of 4 & 6 =",gcd(4, 6))
# print("GCD of 336 & 360 =",gcd(336, 360))

"""Write a Python program to sum three given integers. However, if two values are equal, the sum will be zero."""
# def n(a,b,c):
#     sum = 0
#     if a==b or b==c or c == a:
#         sum = 0
#
#     else:
#         sum = a+b+c
#     return sum
# print(n(10,10,30))

"""Write a Python program to sum two given integers.
However, if the sum is between 15 and 20 it will return 20."""

# def s(n, m, a, b):
#     sum = n + m
#     if sum <= a and sum >= b:
#         return 20
#     return sum
#
#
# print(s(10, 15, 15, 20))


"""Write a Python program that returns true if the two given integer values are equal or their sum or difference is 5"""

# def diff(x, y):
#     sum = x + y
#     dif = x - y
#
#     if sum == 5 or dif == 5 or x == y:
#         return True
#     else:
#         return False
#
#
# print(diff(35, 35))


"""Write a Python program to add two objects if both objects are integers"""

# def add_numbers(a, b):
#     if not (isinstance(a, int) and isinstance(b, int)):
#         return "Inputs must be integers!"
#     return a + b
#
#
# print(add_numbers(10, 20))
# print(add_numbers(10, 20.23))
# print(add_numbers('5', 6))
# print(add_numbers('5', '6'))

"""Write a Python program that displays your name, age, and address on three different lines"""

# def personal_details():
#     name, age = "Simon", 19
#     address = "Bangalore, Karnataka, India"
#     print("Name: {}\nAge: {}\nAddress: {}".format(name, age, address))
#
# personal_details()

"""Write a Python program to solve (x + y) * (x + y)"""

# def s(x, y):
#     print((x + y) ** 2)
# s(4, 3)

"""Write a Python program to compute the future value of a specified principal amount, rate of interest, and number of years."""

# amt = 10000
# int = 3.5
# years = 7
# future_value = amt * ((1 + (0.01 * int)) ** years)
# print(round(future_value, 2))

"""Write a Python program to calculate the distance between the points (x1, y1) and (x2, y2)."""
# import math
#
# p1 = [4, 0]
# p2 = [6, 6]
# distance = math.sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))
#
# print(distance)


"""Write a Python program to check whether a file exists"""
# import os.path
# print(os.path.isfile('main.txt'))
# print(os.path.isfile('main.py'))

"""Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS."""

# import struct
# print(struct.calcsize("P") * 8)

"""Write a Python program to get OS name, platform and release information."""

# import platform
# import os
# print("Name of the operating system:",os.name)
# print("\nName of the OS system:",platform.system())
# print("\nVersion of the operating system:",platform.release())

"""Write a Python program to locate Python site packages."""
# import site
# print(site.getsitepackages())

"""Write a Python program to retrieve the path and name of the file currently being executed."""
# import os
# print("Current File Name : ",os.path.realpath(__file__))


"""Write a Python program to find out the number of CPUs used"""
# import os
# print(os.cpu_count())

"""Write a Python program to parse a string to float or integer"""

# n = "246.2458"
# print(float(n))
# print(int(float(n)))

"""Write a Python program to list all files in a directory."""
# from os import listdir
# from os.path import isfile, join
# l = os.curdir
# files_list = [f for f in listdir(l) if isfile(join(l, f))]
# print(files_list)

"""Write a Python program to print without a newline or space"""

# for i in range(0, 10):
#     print('*', end="")
# print("\n")

"""Write a Python program to determine the profiling of Python programs. Go to the editor
Note: A profile is a set of statistics that describes how often and for how long various parts of the program executed.
These statistics can be formatted into reports via the pstats module."""

# import cProfile
# def sum():
#     print(1+2)
# cProfile.run('sum()')

"""Write a Python program to get the current username."""
# import getpass
# print(getpass.getuser())

"""Write a Python program to find local IP addresses using Python's stdlib."""
# import socket
#
# print([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2]
#                     if not ip.startswith("127.")][:1], [
#                        [(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in
#                         [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0])


"""Write a Python program to get the execution time of a Python method."""

# import time
#
#
# def sum_of_n_numbers(n):
#     start_time = time.time()
#     s = 0
#     for i in range(1, n + 1):
#         s = s + i
#     end_time = time.time()
#     return s, end_time - start_time
#
#
# n = 50
# print("\nTime to sum of 1 to ", n, " and required time to calculate is :", sum_of_n_numbers(n))

"""Write a Python program to sum the first n positive integers."""

n = int(input("Input a number: "))
sum_num = (n * (n + 1)) / 2
print("Sum of the first", n, "positive integers:", sum_num)



"""Write a Python program to convert height (in feet and inches) to centimeters."""

print("Input your height: ")
h_ft = int(input("Feet: "))
h_inch = int(input("Inches: "))

h_inch += h_ft * 12
h_cm = round(h_inch * 2.54, 1)

print("Your height is : %d cm." % h_cm)

"""Write a Python program to calculate the hypotenuse of a right angled triangle."""

from math import sqrt
print("Input lengths of shorter triangle sides:")
a = float(input("a: "))
b = float(input("b: "))
c = sqrt(a**2 + b**2)
print("The length of the hypotenuse is:", c )


"""Write a Python program to convert the distance (in feet) to inches, yards, and miles."""

d_ft = int(input("Input distance in feet: "))
d_inches = d_ft * 12
d_yards = d_ft / 3.0
d_miles = d_ft / 5280.0

print("The distance in inches is %i inches." % d_inches)
print("The distance in yards is %.2f yards." % d_yards)
print("The distance in miles is %.2f miles." % d_miles)


"""Write a Python program to convert all units of time into seconds. """

days = int(input("Input days: ")) * 3600 * 24
hours = int(input("Input hours: ")) * 3600
minutes = int(input("Input minutes: ")) * 60
seconds = int(input("Input seconds: "))

time = days + hours + minutes + seconds

print("The  amounts of seconds", time)

"""Write a Python program to get an absolute file path."""

def absolute_file_path(path_fname):
        import os
        return os.path.abspath('path_fname')        
print("Absolute file path: ",absolute_file_path("test.txt"))


"""Write a Python program that retrieves the date and time of file creation and modification."""

import os.path, time
print("Last modified: %s" % time.ctime(os.path.getmtime("test.txt")))
print("Created: %s" % time.ctime(os.path.getctime("test.txt")))


"""Write a Python program that converts seconds into days, hours, minutes, and seconds."""

time = float(input("Input time in seconds: "))
day = time // (24 * 3600)
time = time % (24 * 3600)
hour = time // 3600
time %= 3600
minutes = time // 60
time %= 60
seconds = time
print("d:h:m:s-> %d:%d:%d:%d" % (day, hour, minutes, seconds))


"""Write a Python program to calculate sum of digits of a number. """
num = int(input("Input a four digit numbers: "))
x  = num //1000
x1 = (num - x*1000)//100
x2 = (num - x*1000 - x1*100)//10
x3 = num - x*1000 - x1*100 - x2*10
print("The sum of digits in the number is", x+x1+x2+x3)


"""Write a Python program to sort three integers without using conditional statements and loops."""

x = int(input("Input first number: "))
y = int(input("Input second number: "))
z = int(input("Input third number: "))

a1 = min(x, y, z)
a3 = max(x, y, z)
a2 = (x + y + z) - a1 - a3
print("Numbers in sorted order: ", a1, a2, a3)

"""Write a Python program to sort files by date."""
import glob
import os

files = glob.glob("*.txt")
files.sort(key=os.path.getmtime)
print("\n".join(files))


"""Write a Python program to get the details of the math module."""
# Imports the math module
import math            
#Sets everything to a list of math module
math_ls = dir(math) # 
print(math_ls)

"""Write a Python program to calculate the midpoints of a line."""

print('\nCalculate the midpoint of a line :')

x1 = float(input('The value of x (the first endpoint) '))
y1 = float(input('The value of y (the first endpoint) '))

x2 = float(input('The value of x (the first endpoint) '))
y2 = float(input('The value of y (the first endpoint) '))

x_m_point = (x1 + x2)/2
y_m_point = (y1 + y2)/2
print()
print("The midpoint of line is :")
print( "The midpoint's x value is: ",x_m_point)
print( "The midpoint's y value is: ",y_m_point)
print()


"""Write a Python program to hash a word."""

soundex=[0,1,2,3,0,1,2,0,0,2,2,4,5,5,0,1,2,6,2,3,0,1,0,2,0,2]
 
word=input("Input the word be hashed: ")
 
word=word.upper()
 
coded=word[0]
 
for a in word[1:len(word)]:
    i=65-ord(a)
    coded=coded+str(soundex[i])
print() 
print("The coded word is: "+coded)
print()


"""Write a Python program to get the copyright information and write Copyright information in Python code."""
import sys
print("\nPython Copyright Information")
print(sys.copyright)
print()

"""Write a Python program to get the command-line arguments (name of the script, the number of arguments, arguments) passed to a script."""
import sys
print("This is the name/path of the script:"),sys.argv[0]
print("Number of arguments:",len(sys.argv))
print("Argument List:",str(sys.argv))

"""Write a Python program to test whether the system is a big-endian platform or a little-endian platform."""

import sys
print()
if sys.byteorder == "little":
    #intel, alpha
    print("Little-endian platform.")
else:
    #motorola, sparc
    print("Big-endian platform.")
print()



"""Write a Python program to find the available built-in modules."""
import sys
import textwrap
module_name = ', '.join(sorted(sys.builtin_module_names))
print(textwrap.fill(module_name, width=70))

"""Write a Python program to concatenate N strings"""
list_of_colors = ['Red', 'White', 'Black']  
colors = '-'.join(list_of_colors)
print()
print("All Colors: "+colors)
print()

"""Write a Python program to calculate the sum of all items of a container (tuple, list, set, dictionary). """

s = sum([10,20,30])
print("\nSum of the container: ", s)
print()

"""Write a Python program to test whether all numbers in a list are greater than a certain number."""
num = [2, 3, 4, 5]
print()
print(all(x > 1 for x in num))
print(all(x > 4 for x in num))
print()

"""Write a Python program to count the number of occurrences of a specific character in a string."""
s = "The quick brown fox jumps over the lazy dog."  
print("Original string:")
print(s)
print("Number of occurrence of 'o' in the said string:")
print(s.count("o"))

"""Write a Python program to check whether a file path is a file or a directory."""

import os  
path="abc.txt"  
if os.path.isdir(path):  
    print("\nIt is a directory")  
elif os.path.isfile(path):  
    print("\nIt is a normal file")  
else:  
    print("It is a special file (socket, FIFO, device file)" )
print()

"""Write a Python program to get the ASCII value of a character."""
print()
print(ord('a'))
print(ord('A'))
print(ord('1'))
print(ord('@'))
print()

"""Write a Python program to get the size of a file."""
import os
file_size = os.path.getsize("abc.txt")
print("\nThe size of abc.txt is :",file_size,"Bytes")
print()


"""Given variables x=30 and y=20, write a Python program to print "30+20=50"."""
x = 30
y = 20
print("\n%d+%d=%d" % (x, y, x+y))
print()


"""Write a Python program to create a copy of its own source code."""

def file_copy(src, dest):
    with open(src) as f, open(dest, 'w') as d:
        d.write(f.read())
        file_copy("untitled0.py", "z.py")
        with open('z.py', 'r') as filehandle:
            for line in filehandle:
                print(line, end = '')


"""Write a Python program to swap two variables."""

a = 30
b = 20
print("\nBefore swap a = %d and b = %d" %(a, b))
a, b = b, a
print("\nAfter swaping a = %d and b = %d" %(a, b))
print()


"""Write a Python program to define a string containing special characters in various forms."""
print()
print("\#{'}${\"}@/")
print("\#{'}${"'"'"}@/")
print(r"""\#{'}${"}@/""")
print('\#{\'}${"}@/')
print('\#{'"'"'}${"}@/')
print(r'''\#{'}${"}@/''')
print()


"""Write a Python program to get the Identity, Type, and Value of an object."""
x = 34
print("\nIdentity: ",x)
print("\nType: ",type(x))
print("\nValue: ",id(x))

"""Write a Python program to convert the bytes in a given string to a list of integers."""

x = b'Abc'
print()
print("\nConvert bytes of the said string to a list of integers:")
print(list(x))
print()


"""Write a Python program to check whether a string is numeric."""
str = 'a123'
#str = '123'
try:
    i = float(str)
except (ValueError, TypeError):
    print('\nNot numeric')
print()

"""Write a Python program to list the special variables used in the language."""
s_var_names = sorted((set(globals().keys()) | set(__builtins__.__dict__.keys())) - set('_ names i'.split()))
print()
print( '\n'.join(' '.join(s_var_names[i:i+8]) for i in range(0, len(s_var_names), 8)) )
print()

"""Write a Python program to get the name of the host on which the routine is running."""
import socket
host_name = socket.gethostname()
print("Host name:", host_name)

"""Write a Python program to access and print a URL's content to the console."""
from http.client import HTTPConnection
conn = HTTPConnection("example.com")
conn.request("GET", "/")  
result = conn.getresponse()
# retrieves the entire contents.  
contents = result.read() 
print(contents)


"""Write a Python program to get system command output."""

import subprocess
# file and directory listing
returned_text = subprocess.check_output("dir", shell=True, universal_newlines=True)
print("dir command to list file and directory")
print(returned_text)

"""Write a Python program to extract the filename from a given path."""
import os
print()
print(os.path.basename('/users/system1/student1/homework-1.py'))
print()


"""Write a Python program to get the users environment."""
import os
import pprint
# User's environment variables
u_env_var = os.environ
print("User's Environment variable:")
pprint.pprint(dict(u_env_var), width = 1)

"""Write a Python program to divide a path by the extension separator."""

import os.path
for path in [ 'test.txt', 'filename', '/user/system/test.txt', '/', '' ]:
    print('"%s" :' % path, os.path.splitext(path))
	

"""Write a Python program to retrieve file properties."""
import os.path
import time

print('File         :', __file__)
print('Access time  :', time.ctime(os.path.getatime(__file__)))
print('Modified time:', time.ctime(os.path.getmtime(__file__)))
print('Change time  :', time.ctime(os.path.getctime(__file__)))
print('Size         :', os.path.getsize(__file__))

"""Write a Python program to find the path to a file or directory when you encounter a path name."""
import os.path

for file in [ __file__, os.path.dirname(__file__), '/', './broken_link']:
    print('File        :', file)
    print('Absolute    :', os.path.isabs(file))
    print('Is File?    :', os.path.isfile(file))
    print('Is Dir?     :', os.path.isdir(file))
    print('Is Link?    :', os.path.islink(file))
    print('Exists?     :', os.path.exists(file))
    print('Link Exists?:', os.path.lexists(file))
	
"""Write a Python program to get numbers divisible by fifteen from a list using an anonymous function."""
num_list = [45, 55, 60, 37, 100, 105, 220]
# use anonymous function to filter
result = list(filter(lambda x: (x % 15 == 0), num_list))
print("Numbers divisible by 15 are",result)


"""Write a Python program to make file lists from the current directory using a wildcard."""
import glob
file_list = glob.glob('*.*')
print(file_list)
#Specific files
print(glob.glob('*.py'))
print(glob.glob('./[0-9].*'))

"""Write a Python program to remove the first item from a specified list."""
color = ["Red", "Black", "Green", "White", "Orange"]
print("Original list elements:")
print(color)
del color[0]
print("After removing the first color:")
print(color)


"""Write a Python program that inputs a number and generates an error message if it is not a number."""

while True:
    try:
        a = int(input("Input a number: "))
        break
    except ValueError:
        print("\nThis is not a number. Try again...")
        print()
		

"""Write a Python program to filter positive numbers from a list. """

nums = [34, 1, 0, -23, 12, -88]
print("Original numbers in the list: ",nums)
new_nums = list(filter(lambda x: x >0, nums))
print("Positive numbers in the said list: ",new_nums)

"""Write a Python program to compute the product of a list of integers (without using a for loop)."""

from functools import reduce
nums = [10, 20, 30,]
print("Original list numbers:")
print(nums)
nums_product = reduce( (lambda x, y: x * y), nums)
print("\nProduct of the said numbers (without using for loop):",nums_product)


"""Write a Python program to print Unicode characters."""
str = u'\u0050\u0079\u0074\u0068\u006f\u006e \u0045\u0078\u0065\u0072\u0063\u0069\u0073\u0065\u0073 \u002d \u0077\u0033\u0072\u0065\u0073\u006f\u0075\u0072\u0063\u0065'
print()
print(str)
print()

""" Write a Python program to prove that two string variables of the same value point to the same memory location."""

str1 = "Python"
str2 = "Python"
 
print("\nMemory location of str1 =", hex(id(str1)))
print("Memory location of str2 =", hex(id(str2)))
print()


"""Write a Python program to create a bytearray from a list."""

print()
nums = [10, 20, 56, 35, 17, 99]
# Create bytearray from list of integers.
values = bytearray(nums)
for x in values: print(x)
print()


"""Write a Python program to round a floating-point number to a specified number of decimal places."""
order_amt = 212.374
print('\nThe total order amount comes to %f' % order_amt)
print('The total order amount comes to %.2f' % order_amt)
print()

"""Write a Python program to format a specified string and limit the length of a string."""
str_num = "1234567890"
print("Original string:",str_num)
print('%.6s' % str_num)
print('%.9s' % str_num)
print('%.10s' % str_num)

""" Write a Python program to determine if a variable is defined or not"""
try:
  x = 1
except NameError:
  print("Variable is not defined....!")
else:
  print("Variable is defined.")
try:
  y
except NameError:
  print("Variable is not defined....!")
else:
  print("Variable is defined.")
  
"""Write a Python program to empty a variable without destroying it"""
n = 20
d = {"x":200}
l = [1,3,5]
t= (5,7,8)
print(type(n)())
print(type(d)())
print(type(l)())
print(type(t)())

"""Write a Python program to determine the largest and smallest integers, longs, and floats."""
import sys
print("Float value information: ",sys.float_info)
print("\nInteger value information: ",sys.int_info)
print("\nMaximum size of an integer: ",sys.maxsize) 

"""Write a Python program to check whether multiple variables have the same value."""

x = 20
y = 20
z = 20
if x == y == z == 20:
    print("All variables have same value!")  
	

"""Write a Python program to sum all counts in a collection."""
import collections
num = [2,2,4,6,6,8,6,10,4]
print(sum(collections.Counter(num).values()))

"""Write a Python program to get the actual module object for a given object."""
from inspect import getmodule
from math import sqrt
print(getmodule(sqrt))

"""Write a Python program to check whether an integer fits in 64 bits."""
int_val = 30
if int_val.bit_length() <= 63:
    print((-2 ** 63).bit_length())
    print((2 ** 63).bit_length())
	
"""Write a Python program to check whether lowercase letters exist in a string."""
str1 = 'A8238i823acdeOUEI'
print(any(c.islower() for c in str1))

"""Write a Python program to add leading zeroes to a string."""
str1='122.22'
print("Original String: ",str1)
print("\nAdded trailing zeros:")
str1 = str1.ljust(8, '0')
print(str1)
str1 = str1.ljust(10, '0')
print(str1)
print("\nAdded leading zeros:")
str1='122.22'
str1 = str1.rjust(8, '0')
print(str1)
str1 = str1.rjust(10, '0')
print(str1)


"""Write a Python program that uses double quotes to display strings."""
import json
print(json.dumps({'Alex': 1, 'Suresh': 2, 'Agnessa': 3}))


"""Write a Python program to split a variable length string into variables."""
var_list = ['a', 'b', 'c']
x, y, z = (var_list + [None] * 3)[:3]
print(x, y, z)
var_list = [100, 20.25]
x, y = (var_list + [None] * 2)[:2]
print(x, y)

"""Write a Python program to list the home directory without an absolute path."""

import os.path
print(os.path.expanduser('~'))




