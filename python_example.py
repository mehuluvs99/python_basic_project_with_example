# https://www.w3resource.com/python-exercises/python-basic-exercises.php
import datetime
print(datetime.datetime.now())

"""Write a Python program that accepts the user's first
and last name and prints them in reverse order with a space between them."""
import os

print(input("First name"), input("Last Name"))

"""Write a Python program that accepts a sequence of 
comma-separated numbers from the user and generates a list and a tuple of those numbers"""

x = input("Enter Number using comma").split(",")
z = tuple(x)
print(x, z)

"""8. Write a Python program to display the first and last colors from the 
following list. color_list = ["Red","Green","White" ,"Black"]"""

color_list = ["Red","Green","White" ,"Black"]
print("%s %s"%(color_list[0],color_list[-1]))

"""
9. Write a Python program to display the examination schedule. (extract the date from exam_st_date). 
"""

exam_st_date = (11, 12, 2014)
print("%i/%i/%i"%(exam_st_date))

"""10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
Sample value of n is 5 """

a = int(input("Input an integer : "))
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
print (n1+n2+n3)

"""Write a Python program to calculate the number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)"""

from datetime import date
Sample_dates = date(2014, 7, 2)
Sample_dates1 = date(2014, 7, 11)
delta = Sample_dates - Sample_dates1

print(delta.days)

"""Write a Python program to calculate the difference between a given number and 17.
If the number is greater than 17, return twice the absolute difference."""

x = int(input("Enter Number:"))

if x <= 17:
    print(17-x)
else:
    print((x-17)*2)

"""Write a Python program to test whether a number is within 100 of 1000 or 2000."""
def near_thousand(n):
      return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))
print(near_thousand(1000))
print(near_thousand(900))
print(near_thousand(800))   
print(near_thousand(2200))


"""Write a Python program to calculate the sum of three given numbers.
If the values are equal, return three times their sum."""

a,b,c = int(input("Enter Number 1 : ")), int(input("Enter Number 2 : ")), int(input("Enter Number 3 : "))
if a==b==c:
    print((a+b+c)*3)
else:
    print(a+b+c)

def x(a,b,c):
    sum = a+b+c

    if a==b==c:
        sum = sum*3
    return sum

print(x(1,2,3)) 

""" Write a Python program to get a newly-generated string from a given string where "Is" has been added to the front.
 Return the string unchanged if the given string already begins with "Is"""

def s(st):
    if st[:2] == "Is":
        return st
    return "Is"+st
print(s("IsEmply"))
print(s("Array"))

"""Write a Python program that returns a string that is n (non-negative integer) copies of a given string."""

def large_string(s,n):
    result = ''
    for i in range(n):
        result = result+s
    return result

print(large_string("abc",2))
print(large_string(".py",3))


"""Write a Python program that determines whether a given number (accepted from the user) is even or odd, and prints an appropriate message to the user."""

n = int(input("Enter Number  "))
if (n % 2) < 0:
    print("Even")
else:
    print("odd")

"""Write a Python program to count the number 4 in a given list."""

def l(search,arr):
    count = 0
    for i in arr:
        if search == i:
            count +=1
    return count
m = l(4,[1,4,1,2,4,6,7,9,4])
print(m)


"""Write a Python program to get n (non-negative integer) copies of the first 2 characters of a given string.
Return n copies of the whole string if the length is less than 2"""

def substring_copy(text, n):
  flen = 2
  if flen > len(text):
    flen = len(text)
  substr = text[:flen]
  result = ""
  for i in range(n):
    result = result + substr
  return result
print(substring_copy('abcdef', 2))
print(substring_copy('p', 3))


"""Write a Python program to test whether a passed letter is a vowel or not"""

def letter(search):
    text = "aeiou"
    for i in text:
        if search == i:
            return True
    return False


print(letter("i"))
print(letter("c"))

"""Write a Python program that checks whether a specified value is contained within a group of values."""

def letter(text, search):

    for i in text:
        if search == i:
            return True
    return False


print(letter([1,5,8,3],3))
print(letter([1,5,8,3],-1))

"""Write a Python program to create a histogram from a given list of integers."""

def histogram(x, y):
    for i in y:
        print(i)
        return str(x) * i, end("\n")
#
#
print(histogram("#", [2, 3, 6, 5]))

"""Write a Python program that concatenates all elements in a list into a string and returns it."""

def con(concatinate):
    result = ""
    for i in concatinate:
        result += str(i)
    return result
#
print(con([1,2,3,5,4]))

"""Write a Python program to print all even numbers from a given list 
of numbers in the same order and stop printing any after 237 in the sequence."""

#
def n(number, stop):
    for i in number:
        if i == stop:
            print(i)
            break
#
        if (i % 2) == 0:
            print(i)
#
#
numbers = [
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 743, 527
]
n(numbers, 237)

"""Write a Python program that prints out all colors from 
color_list_1 that are not present in color_list_2"""

#
def color(a, b):
    Differenct1_2 = []
    Differenct2_1 = []
#
    for i in a:
        for j in b:
            if i != j:
                Differenct1_2.append(i)
            else:
                Differenct2_1.append(j)
    d1 = []
    d2 = []
    for d in Differenct1_2:
        for k in Differenct2_1:
            if d != k:
                d1.append(d)
            else:
                d2.append(d)
#
    print("Differenct1_2 : ", set(Differenct1_2))
    print("Differenct2_1 : ", set(Differenct2_1))
    print()
    print("Differenct1_2 : ", set(d1))
    print("Differenct2_1 : ", set(d2))
#
#
color_list_1 = ["White", "Black", "Red"]
color_list_2 = ["Red", "Green"]
#
color(color_list_1, color_list_2)
#
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
print("Original set elements:")
print(color_list_1)
print(color_list_2)
print("\nDifferenct of color_list_1 and color_list_2:")
print(color_list_1.difference(color_list_2))
print("\nDifferenct of color_list_2 and color_list_1:")
print(color_list_2.difference(color_list_1))

"""Write a Python program that will accept the base and height of a triangle and compute its area."""

b = int(input("Input the base : "))
h = int(input("Input the height : "))
#
area = b*h/2
#
print("area = ", area)

"""Write a Python program that computes the greatest common divisor (GCD) of two positive integers."""

def gcd(x, y):
   gcd = 1
   if x % y == 0:
       return y
   for k in range(int(y / 2), 0, -1):
       if x % k == 0 and y % k == 0:
           gcd = k
           break
   return gcd
print("GCD of 12 & 17 =",gcd(12, 17))
print("GCD of 4 & 6 =",gcd(4, 6))
print("GCD of 336 & 360 =",gcd(336, 360))

"""Write a Python program to sum three given integers. However, if two values are equal, the sum will be zero."""
def n(a,b,c):
    sum = 0
    if a==b or b==c or c == a:
        sum = 0
#
    else:
        sum = a+b+c
    return sum
print(n(10,10,30))

"""Write a Python program to sum two given integers.
However, if the sum is between 15 and 20 it will return 20."""

def s(n, m, a, b):
    sum = n + m
    if sum <= a and sum >= b:
        return 20
    return sum
#
#
print(s(10, 15, 15, 20))


"""Write a Python program that returns true if the two given integer values are equal or their sum or difference is 5"""

def diff(x, y):
    sum = x + y
    dif = x - y
#
    if sum == 5 or dif == 5 or x == y:
        return True
    else:
        return False
#
#
print(diff(35, 35))


"""Write a Python program to add two objects if both objects are integers"""

def add_numbers(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
        return "Inputs must be integers!"
    return a + b
#
#
print(add_numbers(10, 20))
print(add_numbers(10, 20.23))
print(add_numbers('5', 6))
print(add_numbers('5', '6'))

"""Write a Python program that displays your name, age, and address on three different lines"""

def personal_details():
    name, age = "Simon", 19
    address = "Bangalore, Karnataka, India"
    print("Name: {}\nAge: {}\nAddress: {}".format(name, age, address))
#
personal_details()

"""Write a Python program to solve (x + y) * (x + y)"""

def s(x, y):
    print((x + y) ** 2)
s(4, 3)

"""Write a Python program to compute the future value of a specified principal amount, rate of interest, and number of years."""

amt = 10000
int = 3.5
years = 7
future_value = amt * ((1 + (0.01 * int)) ** years)
print(round(future_value, 2))

"""Write a Python program to calculate the distance between the points (x1, y1) and (x2, y2)."""
import math
#
p1 = [4, 0]
p2 = [6, 6]
distance = math.sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))
#
print(distance)


"""Write a Python program to check whether a file exists"""
import os.path
print(os.path.isfile('main.txt'))
print(os.path.isfile('main.py'))

"""Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS."""

import struct
print(struct.calcsize("P") * 8)

"""Write a Python program to get OS name, platform and release information."""

import platform
import os
print("Name of the operating system:",os.name)
print("\nName of the OS system:",platform.system())
print("\nVersion of the operating system:",platform.release())

"""Write a Python program to locate Python site packages."""
import site
print(site.getsitepackages())

"""Write a Python program to retrieve the path and name of the file currently being executed."""
import os
print("Current File Name : ",os.path.realpath(__file__))


"""Write a Python program to find out the number of CPUs used"""
import os
print(os.cpu_count())

"""Write a Python program to parse a string to float or integer"""

n = "246.2458"
print(float(n))
print(int(float(n)))

"""Write a Python program to list all files in a directory."""
from os import listdir
from os.path import isfile, join
l = os.curdir
files_list = [f for f in listdir(l) if isfile(join(l, f))]
print(files_list)

"""Write a Python program to print without a newline or space"""

for i in range(0, 10):
    print('*', end="")
print("\n")

"""Write a Python program to determine the profiling of Python programs. 
Note: A profile is a set of statistics that describes how often and for how long various parts of the program executed.
These statistics can be formatted into reports via the pstats module."""

import cProfile
def sum():
    print(1+2)
cProfile.run('sum()')

"""Write a Python program to get the current username."""
import getpass
print(getpass.getuser())

"""Write a Python program to find local IP addresses using Python's stdlib."""
import socket
#
print([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2]
                    if not ip.startswith("127.")][:1], [
                       [(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in
                        [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0])


"""Write a Python program to get the execution time of a Python method."""

import time
#
#
def sum_of_n_numbers(n):
    start_time = time.time()
    s = 0
    for i in range(1, n + 1):
        s = s + i
    end_time = time.time()
    return s, end_time - start_time
#
#
n = 50
print("\nTime to sum of 1 to ", n, " and required time to calculate is :", sum_of_n_numbers(n))

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
Imports the math module
import math            
#Sets everything to a list of math module
math_ls = dir(math) 
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
retrieves the entire contents.  
contents = result.read() 
print(contents)


"""Write a Python program to get system command output."""

import subprocess
file and directory listing
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
User's environment variables
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
use anonymous function to filter
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
Create bytearray from list of integers.
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

"""Write a Python program to calculate the time runs (difference between start and current time) of a program."""

from timeit import default_timer
def timer(n):
    start = default_timer()
    some code here
    for row in range(0,n):
        print(row)
    print(default_timer() - start)

timer(5)
timer(15)

"""Write a Python program to input two integers on a single line."""
print("Input the value of x & y")
x, y = map(int, input().split())
print("The value of x & y are: ",x,y)

"""Write a Python program to print a variable without spaces between values.
Sample value : x =30
Expected output : Value of x is "30"""


x = 30
print('Value of x is "{}"'.format(x))

"""Write a Python program to find files and skip directories in a given directory."""

import os
print([f for f in os.listdir('/home/students') if os.path.isfile(os.path.join('/home/students', f))])

"""Write a Python program to extract a single key-value pair from a dictionary into variables."""

d = {'Red': 'Green'}
(c1, c2), = d.items()
print(c1)
print(c2)


"""Write a Python program to convert true to 1 and false to 0"""
x = 'true'
x = int(x == 'true')
print(x)
x = 'abcd'
x = int(x == 'true')
print(x)


"""Write a Python program to validate an IP address."""
import socket
addr = '127.0.0.2561'
try:
    socket.inet_aton(addr)
    print("Valid IP")
except socket.error:
    print("Invalid IP")


"""Write a Python program to convert an integer to binary that keeps leading zeros.
Sample data : x=12
Expected output : 00001100
0000001100"""

x = 12
print(format(x, '08b'))
print(format(x, '010b'))


"""Write a python program to convert decimal to hexadecimal.
Sample decimal number: 30, 4
Expected output: 1e, 04"""

x = 30
print(format(x, '02x'))
x = 4
print(format(x, '02x'))

"""Write a Python program to check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones of same length in a given string. Return True/False. 
Original sequence: 01010101
Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:
True
Original sequence: 00
Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:
False
Original sequence: 000111000111
Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:
True
Original sequence: 00011100011
Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:
False"""

def test(str1):
    while '01' in str1:
        str1 = str1.replace('01', '')
    return len(str1) == 0

str1 = "01010101"
print("Original sequence:",str1)
print("Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:")
print(test(str1))
str1 = "00"
print("\nOriginal sequence:",str1)
print("Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:")
print(test(str1))
str1 = "000111000111"
print("\nOriginal sequence:",str1)
print("Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:")
print(test(str1))
str1 = "00011100011"
print("\nOriginal sequence:",str1)
print("Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:")
print(test(str1))

"""Write a Python program to determine if the Python shell is executing in 32-bit or 64-bit mode on the operating system."""
import struct
print(struct.calcsize("P") * 8)

"""Write a Python program to check whether a variable is an integer or string."""
print(isinstance(25,int) or isinstance(25,str))
print(isinstance([25],int) or isinstance([25],str))
print(isinstance("25",int) or isinstance("25",str))

"""Write a Python program to test if a variable is a list, tuple, or set."""
#x = ['a', 'b', 'c', 'd']
#x = {'a', 'b', 'c', 'd'}
x = ('tuple', False, 3.2, 1)
if type(x) is list:
    print('x is a list')
elif type(x) is set:
    print('x is a set')
elif type(x) is tuple:
    print('x is a tuple')    
else:
    print('Neither a list or a set or a tuple.')

"""Write a Python program to find the location of Python module sources."""
import imp
print("Location of Python os module sources:")
print(imp.find_module('os'))
print("\nLocation of Python sys module sources:")
print(imp.find_module('datetime'))

"""Write a Python function to check whether a number is divisible by another number. Accept two integer values from the user."""
def multiple(m, n):
	return True if m % n == 0 else False

print(multiple(20, 5))
print(multiple(7, 2))

"""Write a Python function to find the maximum and minimum numbers from a sequence of numbers."""
def max_min(data):
  l = data[0]
  s = data[0]
  for num in data:
    if num> l:
      l = num
    elif num< s:
        s = num
  return l, s

print(max_min([0, 10, 15, 40, -5, 42, 17, 28, 75]))

"""Write a Python function that takes a positive integer and returns the sum of the cube of all positive integers smaller than the specified number."""
def sum_of_cubes(n):
 n -= 1
 total = 0
 while n > 0:
   total += n * n * n
   n -= 1
 return total
print("Sum of cubes smaller than the specified number: ",sum_of_cubes(3))

"""Write a Python function to check whether a distinct pair of numbers whose product is odd is present in a sequence of integer values."""
def odd_product(nums):
  for i in range(len(nums)):
    for j in range(len(nums)):
      if  i != j:
        product = nums[i] * nums[j]
        if product & 1:
          return True
  return False          
dt1 = [2, 4, 6, 8]
dt2 = [1, 6, 4, 7, 8]
dt3 = [1, 3, 5, 7, 9]
print(dt1, odd_product(dt1))
print(dt2, odd_product(dt2))
print(dt3, odd_product(dt3))


#https://www.w3resource.com/python-exercises/basic/#EDITOR
############___________________Python_Example________##############
"""Write a Python function that takes a sequence of numbers and determines whether all 
the numbers are different from each other."""

def test_distinct(data):
  if len(data) == len(set(data)):
    return True
  else:
    return False;
print(test_distinct([1,5,7,9]))
print(test_distinct([2,4,5,5,7,9]))

"""Write a Python program that creates all possible strings using the letters 'a', 'e', 'i', 'o', and 'I'.
Ensure that each character is used only once."""

import random
char_list = ['a','e','i','o','u']
random.shuffle(char_list)
print(''.join(char_list))


"""Write a Python program that removes and prints every third number from a list of numbers until the list is empty."""

def remove_nums(int_list):
  #list starts with 0 index
  position = 3 - 1 
  idx = 0
  len_list = (len(int_list))
  while len_list>0:
    idx = (position+idx)%len_list
    print(int_list.pop(idx))
    len_list -= 1
nums = [10,20,30,40,50,60,70,80,90]
remove_nums(nums)


"""Write a Python program to identify unique triplets whose three elements sum to zero from an array of n integers."""

def three_sum(nums):
  result = []
  nums.sort()
  for i in range(len(nums)-2):
    if i> 0 and nums[i] == nums[i-1]:
      continue
    l, r = i+1, len(nums)-1
    while l < r:
      s = nums[i] + nums[l] + nums[r]
      if s > 0:
        r -= 1
      elif s < 0:
          l += 1
      else:
        found three sum
        result.append((nums[i], nums[l], nums[r]))
        remove duplicates
        while l < r and nums[l] == nums[l+1]:
          l+=1
          while l < r and nums[r] == nums[r-1]:
            r -= 1
            l += 1
            r -= 1
          return result

x = [1, -6, 4, 2, -1, 2, 0, -2, 0 ]
print(three_sum(x))


#Write a Python program to make combinations of 3 digits.

numbers = []
for num in range(1000):
  num=str(num).zfill(3)
print(num)
numbers.append(num)


"""Write a Python program that prints long text, converts it to a list, and prints all the words and the frequency of each word."""
string_words = '''United States Declaration of Independence
From Wikipedia, the free encyclopedia
The United States Declaration of Independence is the statement
adopted by the Second Continental Congress meeting at the Pennsylvania State
House (Independence Hall) in Philadelphia on July 4, 1776, which announced
that the thirteen American colonies, then at war with the Kingdom of Great
Britain, regarded themselves as thirteen independent sovereign states, no longer
under British rule. These states would found a new nation - the United States of
America. John Adams was a leader in pushing for independence, which was passed
on July 2 with no opposing vote cast. A committee of five had already drafted the
formal declaration, to be ready when Congress voted on independence.

John Adams persuaded the committee to select Thomas Jefferson to compose the original
draft of the document, which Congress would edit to produce the final version.
The Declaration was ultimately a formal explanation of why Congress had voted on July
2 to declare independence from Great Britain, more than a year after the outbreak of
the American Revolutionary War. The next day, Adams wrote to his wife Abigail: "The
Second Day of July 1776, will be the most memorable Epocha, in the History of America."
But Independence Day is actually celebrated on July 4, the date that the Declaration of
Independence was approved.

After ratifying the text on July 4, Congress issued the Declaration of Independence in
several forms. It was initially published as the printed Dunlap broadside that was widely
distributed and read to the public. The source copy used for this printing has been lost,
and may have been a copy in Thomas Jefferson's hand.[5] Jefferson's original draft, complete
with changes made by John Adams and Benjamin Franklin, and Jefferson's notes of changes made
by Congress, are preserved at the Library of Congress. The best-known version of the Declaration
is a signed copy that is displayed at the National Archives in Washington, D.C., and which is
popularly regarded as the official document. This engrossed copy was ordered by Congress on
July 19 and signed primarily on August 2.

The sources and interpretation of the Declaration have been the subject of much scholarly inquiry.
The Declaration justified the independence of the United States by listing colonial grievances against
King George III, and by asserting certain natural and legal rights, including a right of revolution.
Having served its original purpose in announcing independence, references to the text of the
Declaration were few in the following years. Abraham Lincoln made it the centerpiece of his rhetoric
(as in the Gettysburg Address of 1863) and his policies. Since then, it has become a well-known statement
on human rights, particularly its second sentence:

We hold these truths to be self-evident, that all men are created equal, that they are endowed by their
Creator with certain unalienable Rights, that among these are Life, Liberty and the pursuit of Happiness.

This has been called "one of the best-known sentences in the English language", containing "the most potent
and consequential words in American history". The passage came to represent a moral standard to which
the United States should strive. This view was notably promoted by Abraham Lincoln, who considered the
Declaration to be the foundation of his political philosophy and argued that it is a statement of principles
through which the United States Constitution should be interpreted.

The U.S. Declaration of Independence inspired many other similar documents in other countries, the first
being the 1789 Declaration of Flanders issued during the Brabant Revolution in the Austrian Netherlands
(modern-day Belgium). It also served as the primary model for numerous declarations of independence across
Europe and Latin America, as well as Africa (Liberia) and Oceania (New Zealand) during the first half of the
19th century.'''

word_list = string_words.split()

word_freq = [word_list.count(n) for n in word_list]

print("String:\n {} \n".format(string_words))
print("List:\n {} \n".format(str(word_list)))
print("Pairs (Words and Frequencies:\n {}".format(str(list(zip(word_list, word_freq)))))


"""Write a Python program to count the number of each character in a text file."""

import collections
import pprint
file_input = input('File Name: ')
with open(file_input, 'r') as info:
  count = collections.Counter(info.read().upper())
  value = pprint.pformat(count)
print(value)


"""Write a Python program that retrieves the top stories from Google News."""

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

news_url="https://news.google.com/news/rss"
Client=urlopen(news_url)
xml_page=Client.read()
Client.close()

soup_page=soup(xml_page,"xml")
news_list=soup_page.findAll("item")
Print news title, url and publish date
for news in news_list:
  print(news.title.text)
  print(news.link.text)
  print(news.pubDate.text)
  print("-"*60)

"""Write a Python program to get a list of locally installed Python modules."""
import pkg_resources
installed_packages = pkg_resources.working_set
installed_packages_list = sorted(["%s==%s" % (i.key, i.version) for i in installed_packages])
for m in installed_packages_list:
    print(m)

"""Write a Python program to display some information about the OS where the script is running."""
import platform as pl

os_profile = [
        'architecture',
        'linux_distribution',
        'mac_ver',
        'machine',
        'node',
        'platform',
        'processor',
        'python_build',
        'python_compiler',
        'python_version',
        'release',
        'system',
        'uname',
        'version',
    ]
for key in os_profile:
  if hasattr(pl, key):
    print(key +  ": " + str(getattr(pl, key)()))

"""Write a Python program to check the sum of three elements (each from an array) from three arrays is equal to a target value.
Print all those three-element combinations.
Sample data:
/*
X = [10, 20, 20, 20]
Y = [10, 20, 30, 40]
Z = [10, 30, 40, 20]
target = 70
*/"""
 
import itertools
from functools import partial
X = [10, 20, 20, 20]
Y = [10, 20, 30, 40]
Z = [10, 30, 40, 20]
T = 70

def check_sum_array(N, *nums):
  if sum(x for x in nums) == N:
    return (True, nums)
  else:
      return (False, nums)
pro = itertools.product(X,Y,Z)
func = partial(check_sum_array, T)
sums = list(itertools.starmap(func, pro))

result = set()
for s in sums:
    if s[0] == True and s[1] not in result:
      result.add(s[1])
      print(result)


"""Write a Python program that generates a list of all possible permutations from a given collection of distinct numbers."""

def permute(nums):
  result_perms = [[]]
  for n in nums:
    new_perms = []
    for perm in result_perms:
      for i in range(len(perm)+1):
        new_perms.append(perm[:i] + [n] + perm[i:])
        result_perms = new_perms
  return result_perms

my_nums = [1,2,3]
print("Original Cofllection: ",my_nums)
print("Collection of distinct numbers:\n",permute(my_nums))

"""Write a Python program to get all possible two-digit letter combinations from a 1-9 digit string."""

def letter_combinations(digits):
    if digits == "":
        return []
    string_maps = {
                  "1": "abc",
                  "2": "def",
                  "3": "ghi",
                  "4": "jkl",
                  "5": "mno",
                  "6": "pqrs",
                  "7": "tuv",
                  "8": "wxy",
                  "9": "z"
                  }
    result = [""]
    for num in digits:
        temp = []
        for an in result:
            for char in string_maps[num]:
                temp.append(an + char)
        result = temp
    return result

digit_string = "47"
print(letter_combinations(digit_string))
digit_string = "29"
print(letter_combinations(digit_string))

"""Write a Python program to add two positive integers without using the '+' operator"""
def add_without_plus_operator(a, b):
    while b != 0:
        data = a & b
        a = a ^ b
        b = data << 1
    return a
print(add_without_plus_operator(2, 10))
print(add_without_plus_operator(-20, 10))
print(add_without_plus_operator(-10, -20))

"""Write a Python program to check the priority of the four operators (+, -, *, /). """

from collections import deque
import re

__operators__ = "+-/*"
__parenthesis__ = "()"
__priority__ = {
    '+': 0,
    '-': 0,
    '*': 1,
    '/': 1,
}

def test_higher_priority(operator1, operator2):
    return __priority__[operator1] >= __priority__[operator2]

print(test_higher_priority('*','-'))
print(test_higher_priority('+','-'))
print(test_higher_priority('+','*'))
print(test_higher_priority('+','/'))
print(test_higher_priority('*','/'))

"""Write a Python program to get the third side of a right-angled triangle from two given sides."""

def pythagoras(opposite_side,adjacent_side,hypotenuse):
        if opposite_side == str("x"):
            return ("Opposite = " + str(((hypotenuse**2) - (adjacent_side**2))**0.5))
        elif adjacent_side == str("x"):
            return ("Adjacent = " + str(((hypotenuse**2) - (opposite_side**2))**0.5))
        elif hypotenuse == str("x"):
            return ("Hypotenuse = " + str(((opposite_side**2) + (adjacent_side**2))**0.5))
        else:
            return "You know the answer!"
    
print(pythagoras(3,4,'x'))
print(pythagoras(3,'x',5))
print(pythagoras('x',4,5))
print(pythagoras(3,4,5))

"""Write a Python program to get all strobogrammatic numbers that are of length n.
A strobogrammatic number is a number whose numeral is rotationally symmetric, so that it appears the same when rotated 180 degrees.
In other words, the numeral looks the same right-side up and upside down (e.g., 69, 96, 1001).
For example,
Given n = 2, return ["11", "69", "88", "96"].
Given n = 3, return ['818', '111', '916', '619', '808', '101', '906', '609', '888', '181', '986', '689']"""

#https://github.com/keon/algorithms/blob/master/math/generate_strobogrammtic.py
def gen_strobogrammatic(n):
    """
    :type n: int
    :rtype: List[str]
    """
    result = helper(n, n)
    return result


def helper(n, length):
    if n == 0:
        return [""]
    if n == 1:
        return ["1", "0", "8"]
    middles = helper(n-2, length)
    result = []
    for middle in middles:
        if n != length:
            result.append("0" + middle + "0")
        result.append("8" + middle + "8")
        result.append("1" + middle + "1")
        result.append("9" + middle + "6")
        result.append("6" + middle + "9")
    return result

print("n = 2: \n",gen_strobogrammatic(2))
print("n = 3: \n",gen_strobogrammatic(3))
print("n = 4: \n",gen_strobogrammatic(4))

"""Write a Python program to find the median among three given numbers."""

x = input("Input the first number")
y = input("Input the second number")
z = input("Input the third number")
print("Median of the above three numbers -")

if y < x and x < z:
    print(x)
elif z < x and x < y:
    print(x)
    
elif z < y and y < x:
    print(y)
elif x < y and y < z:
    print(y)
    
elif y < z and z < x:
    print(z)    
elif x < z and z < y:
    print(z)

"""Write a Python program that finds the value of n when n degrees of number 2 are written sequentially on a line without spaces between them."""

def ndegrees(num):
  ans = True
  n, tempn, i = 2, 2, 2
  while ans:
    if str(tempn) in num:
      i += 1
      tempn = pow(n, i)
    else:
      ans = False
  return i-1;
print(ndegrees("2481632"))
print(ndegrees("248163264"))

"""Write a Python program to find the number of zeros at the end of a factorial of a given positive number."""
"""Range of the number(n): (1 <= n <= 2*109)."""
def factendzero(n):
  x = n // 5
  y = x 
  while x > 0:
    x /= 5
    y += int(x)
  return y
       
print(factendzero(5))
print(factendzero(12))
print(factendzero(100))

"""Write a Python program to find the number of notes (Samples of notes: 10, 20, 50, 100, 200, 500) against an amount."""

def no_notes(a):
  Q = [500, 200, 100, 50, 20, 10]
  x = 0
  for i in range(6):
    q = Q[i]
    x += int(a / q)
    a = int(a % q)
  if a > 0:
    x = -1
  return x
print(no_notes(880))
print(no_notes(1000))

"""Write a Python program to create a sequence where the first four members of the sequence are equal to one.
Each successive term of the sequence is equal to the sum of the four previous ones.
Find the Nth member of the sequence."""

def new_seq(n):
    if n==1 or n==2 or n==3 or n==4:
        return 1
    return new_seq(n-1) + new_seq(n-2) + new_seq(n-3) + new_seq(n-4)
print(new_seq(5))
print(new_seq(6))
print(new_seq(7))

"""Write a Python program that accepts a positive number and subtracts from it the sum of its digits, and so on.
Continue this operation until the number is positive."""

def repeat_times(n):
  n_str = str(n)
  while (n > 0):
    n -= sum([int(i) for i in list(n_str)])
    n_str = list(str(n))
  return n
print(repeat_times(9))
print(repeat_times(20))
print(repeat_times(110))
print(repeat_times(5674))


"""Write a Python program to find the total number of even or odd divisors of a given integer."""
def divisor(n):
  x = len([i for i in range(1,n+1) if not n % i])
  return x
print(divisor(15))
print(divisor(12))
print(divisor(9))
print(divisor(6))
print(divisor(3))

"""Write a Python program to find the digits that are missing from a given mobile number."""

def absent_digits(n):
  all_nums = set([0,1,2,3,4,5,6,7,8,9])
  n = set([int(i) for i in n])
  n = n.symmetric_difference(all_nums)
  n = sorted(n)
  return n
print(absent_digits([9,8,3,2,2,0,9,7,6,3]))

"""Write a Python program to compute the summation of the absolute difference of all distinct pairs in a given array (non-decreasing order)."""

def sum_distinct_pairs(arr):
    result = 0
    i = 0
    while i<len(arr):
        result+=i*arr[i]-(len(arr)-i-1)*arr[i]
        i+=1
    return result
print(sum_distinct_pairs([1,2,3]))
print(sum_distinct_pairs([1,4,5]))



"""Write a Python program to print the length of the series and the series from the given 3rd term, 3rd last term and the sum of a series."""

tn = int(input("Input third term of the series:"))
tltn = int(input("Input 3rd last term:"))
s_sum = int(input("Sum of the series:"))
n = int(2*s_sum/(tn+tltn))
print("Length of the series: ",n)


if n-5==0:
  d = (s_sum-3*tn)//6
else:
  d = (tltn-tn)/(n-5)

a = tn-2*d
j = 0
print("Series:")
for j in range(n-1):
  print(int(a),end=" ")
  a+=d
print(int(a),end=" ")

"""Write a Python program to find common divisors between two numbers in a given pair."""

def ngcd(x, y):
    i=1
    while(i<=x and i<=y):
        if(x%i==0 and y%i == 0):
            gcd=i;
        i+=1
    return gcd;
def num_comm_div(x, y):
  n = ngcd(x, y)
  result = 0
  z = int(n**0.5)
  i = 1
  while( i <= z ):
    if(n % i == 0):
      result += 2 
      if(i == n/i):
        result-=1
    i+=1
  return result

print("Number of common divisors: ",num_comm_div(2, 4))
print("Number of common divisors: ",num_comm_div(2, 8))
print("Number of common divisors: ",num_comm_div(12, 24))


"""Find common divisors between two numbers in a given pair"""

def ngcd(x, y):
    i=1
    while(i<=x and i<=y):
        if(x%i==0 and y%i == 0):
            gcd=i;
        i+=1
    return gcd;
def num_comm_div(x, y):
  n = ngcd(x, y)
  result = 0
  z = int(n**0.5)
  i = 1
  while( i <= z ):
    if(n % i == 0):
      result += 2 
      if(i == n/i):
        result-=1
    i+=1
  return result

print("Number of common divisors: ",num_comm_div(2, 4))
print("Number of common divisors: ",num_comm_div(2, 8))
print("Number of common divisors: ",num_comm_div(12, 24))


"""Write a Python program to reverse the digits of a given number and add them to the original. Repeat this procedure if the sum is not a palindrome."""

def rev_number(n):
  s = 0
  while True:
    k = str(n)
    if k == k[::-1]:
      break
    else:
      m = int(k[::-1])
      n += m
      s += 1
  return n 

print(rev_number(1234))
print(rev_number(1473))


"""Write a Python program to find the heights of the top three buildings in descending order from eight given buildings."""

"""Input:
0 <= height of building (integer) <= 10,000
Input the heights of eight buildings:
25
35
15
16
30
45
37
39
Heights of the top three buildings:
45
39
37"""

print("Input the heights of eight buildings:")
l = [int(input()) for i in range(8)]
print("Heights of the top three buildings:")
l = sorted(l)
print(*l[:4:-1], sep='\n')


"""Write a Python program to compute the digit number of the sum of two given integers"""

"""Each test case consists of two non-negative integers x and y which are separated by a space in a line.
0 <= x, y <= 1,000,000
Input two integers(a b):
5 7
Sum of two integers a and b.:
2"""

"""Write a Python program to compute the digit number of the sum of two given integers.
Each test case consists of two non-negative integers x and y which are separated by a space in a line.
0 ≤ x, y ≤ 1,000,000"""


print("Input two integers(a b): ")
a,b = map(int,input().split(" "))
print("Number of digit of a and b.:")
print(len(str(a+b)))

"""Write a Python program to check whether three given lengths (integers) of three sides form a right triangle.
Print "Yes" if the given sides form a right triangle otherwise print "No"."""

"""Input:
Integers separated by a single space.
1 <= length of the side <= 1,000
Input three integers(sides of a triangle)
8 6 7
No"""


print("Input three integers(sides of a triangle)")
int_num = list(map(int,input().split()))
x,y,z = sorted(int_num)
if x**2+y**2==z**2:
    print('Yes')
else:
    print('No')

"""Write a Python program which solve the equation: 
ax+by=c
dx+ey=f
Print the values of x, y where a, b, c, d, e and f are given.
Input:
a,b,c,d,e,f separated by a single space.
(-1,000 <= a,b,c,d,e,f <= 1,000)
Input the value of a, b, c, d, e, f:
5 8 6 7 9 4
Values of x and y:
-2.000 2.000"""

print("Input the value of a, b, c, d, e, f:")
a, b, c, d, e, f = map(float, input().split())
n = a*e - b*d
print("Values of x and y:")
if n != 0:
    x = (c*e - b*f) / n
    y = (a*f - c*d) / n
    print('{:.3f} {:.3f}'.format(x+0, y+0))

"""Write a Python program to compute the amount of debt in n months.
Each month, the loan adds 5% interest to the $100,000 debt and rounds to the nearest 1,000 above.

Input:
An integer n (0 <= n <= 100)
Input number of months: 7
Amount of debt: $144000"""

def round_n(n):
    if n%1000:
        return (1+n//1000)*1000
    else:
        return n
     
def compute_debt(n):
    if n==0: return 100000
    return int(round_n(compute_debt(n-1)*1.05))

print("Input number of months:")
result = compute_debt(int(input()))
print("Amount of debt: ","$"+str(result).strip())

"""Write a Python program that reads an integer n and finds the number of combinations of a,b,c and d (0 = a,b,c,d = 9) where (a + b + c + d) will be equal to n.
Input:
n (1 <= n <= 50)
Input the number(n): 15
Number of combinations: 592"""

import itertools
print("Input the number(n):")
n=int(input())
result=0
for (i,j,k) in itertools.product(range(10),range(10),range(10)):
    result+=(0<=n-(i+j+k)<=9)
print("Number of combinations:",result)


"""Write a Python program to print the number of prime numbers that are less than or equal to a given number.
Input:
n (1 <= n <= 999,999)
Input the number(n): 35
Number of prime numbers which are less than or equal to n.: 11"""

primes = [1] * 500000
primes[0] = 0
 
for i in range(3, 1000, 2):
    if primes[i // 2]:
        primes[(i * i) // 2::i] = [0] * len(primes[(i * i) // 2::i])
 
print("Input the number(n):")
n=int(input())
if n < 4:
    print("Number of prime numbers which are less than or equal to n.:",n - 1)
else:
    print("Number of prime numbers which are less than or equal to n.:",sum(primes[:(n + 1) // 2]) + 1)

"""Write a program to compute the radius and the central coordinate (x, y) of a circle which is constructed from three given points on the plane surface.
Input:
x1, y1, x2, y2, x3, y3 separated by a single space.
Input three coordinate of the circle:
9 3 6 8 3 6
Radius of the said circle:
3.358
Central coordinate (x, y) of the circle:
6.071 4.643"""

print("Input three coordinate of the circle:")
x1, y1, x2, y2, x3, y3 = map(float, input().split())
c = (x1-x2)**2 + (y1-y2)**2
a = (x2-x3)**2 + (y2-y3)**2
b = (x3-x1)**2 + (y3-y1)**2
s = 2*(a*b + b*c + c*a) - (a*a + b*b + c*c) 
px = (a*(b+c-a)*x1 + b*(c+a-b)*x2 + c*(a+b-c)*x3) / s
py = (a*(b+c-a)*y1 + b*(c+a-b)*y2 + c*(a+b-c)*y3) / s 
ar = a**0.5
br = b**0.5
cr = c**0.5 
r = ar*br*cr / ((ar+br+cr)*(-ar+br+cr)*(ar-br+cr)*(ar+br-cr))**0.5
print("Radius of the said circle:")
print("{:>.3f}".format(r))
print("Central coordinate (x, y) of the circle:")
print("{:>.3f}".format(px),"{:>.3f}".format(py))


"""Write a Python program to check if a point (x,y) is in a triangle or not. A triangle is formed by three points. 
Input:
x1,y1,x2,y2,x3,y3,xp,yp separated by a single space.
Input three coordinate of the circle:
9 3 6 8 3 6
Radius of the said circle:
3.358
Central coordinate (x, y) of the circle:
6.071 4.643"""

print("Input x1,y1,x2,y2,x3,y3,xp,yp:")
x1,y1,x2,y2,x3,y3,xp,yp = map(float, input().split())
c1 = (x2-x1)*(yp-y1)-(y2-y1)*(xp-x1)
c2 = (x3-x2)*(yp-y2)-(y3-y2)*(xp-x2)
c3 = (x1-x3)*(yp-y3)-(y1-y3)*(xp-x3)
if (c1<0 and c2<0 and c3<0) or (c1>0 and c2>0 and c3>0):
    print("The point is in the triangle.")
else:
    print("The point is outside the triangle.")

"""Write a Python program to compute and print the sum of two given integers (greater or equal to zero). 
In the event that the given integers or the sum exceed 80 digits, print "overflow". 
Input first integer:
25
Input second integer:
22
Sum of the two integers: 47"""

print("Input first integer:")
x = int(input())
print("Input second integer:")
y = int(input())
if x >= 10 ** 80 or y >= 10 ** 80 or x + y >= 10 ** 80:
    print("Overflow!")
else:
    print("Sum of the two integers: ",x + y)

"""Write a Python program that accepts six numbers as input and sorts them in descending order. 
Input:
Input consists of six numbers n1, n2, n3, n4, n5, n6 (-100000 <= n1, n2, n3, n4, n5, n6 <= 100000).
The six numbers are separated by a space.
Input six integers:
15 30 25 14 35 40
After sorting the said integers:
40 35 30 25 15 14"""

print("Input six integers:")
nums = list(map(int, input().split()))
nums.sort()
nums.reverse()
print("After sorting the said ntegers:")
print(*nums)


"""Write a Python program to test whether two lines PQ and RS are parallel.
The four points are P(x1, y1), Q(x2, y2), R(x3, y3), S(x4, y4).
Input:
x1,y1,x2,y2,x3,y3,xp,yp separated by a single space
Input x1,y1,x2,y2,x3,y3,xp,yp:
2 5 6 4 8 3 9 7
PQ and RS are not parallel"""

print("Input x1,y1,x2,y2,x3,y3,xp,yp:")
x1, y1,x2, y2, x3, y3, x4, y4 = map(float, input().split())
print('PQ and RS are parallel.' if abs((x2 - x1)*(y4 - y3) - (x4 - x3)*(y2 - y1)) < 1e-10 else 'PQ and RS are not parallel')

"""Write a Python program to find the maximum sum of a contiguous subsequence from a given sequence of numbers a1, a2, a3, ... an.
A subsequence of one element is also a continuous subsequence. 
Input:
You can assume that 1 <= n <= 5000 and -100000 <= ai <= 100000.
Input numbers are separated by a space.
Input 0 to exit.
Input number of sequence of numbers you want to input (0 to exit):
3
Input numbers:
2
4
6
Maximum sum of the said contiguous subsequence: 12
Input number of sequence of numbers you want to input (0 to exit):
0"""

while True:
    print("Input number of sequence of numbers you want to input (0 to exit):")
    n = int(input())
    if n == 0:
        break
    else:
        A = []
        Sum = []
        print("Input numbers:") 
        for i in range(n):
            A.append(int(input()))
        Wa = 0
        for i in range(0,n):
            Wa += A[i]
            Sum.append(Wa)
        for i in range(0 , n):
            for j in range(0 , i):
                Num = Sum[i] - Sum[j]
                Sum.append(Num)
        print("Maximum sum of the said contiguous subsequence:")
        print(max(Sum))

"""
There are two circles C1 with radius r1, central coordinate (x1, y1) and C2 with radius r2 and central coordinate (x2, y2). Go to the editor

Write a Python program to test the followings -

"C2 is in C1" if C2 is in C1
"C1 is in C2" if C1 is in C2
"Circumference of C1 and C2 intersect" if circumference of C1 and C2 intersect
"C1 and C2 do not overlap" if C1 and C2 do not overlap and
"Circumference of C1 and C2 will touch" if C1 and C2 touch
Input:
Input numbers (real numbers) are separated by a space.
Input x1, y1, r1, x2, y2, r2:
5 4 2 3 9 2
C1 and C2 do not overlap
Input x1, y1, r1, x2, y2, r2:
5 4 3 5 10 3
Circumference of C1 and C2 will touch
Input x1, y1, r1, x2, y2, r2:
6 4 3 10 4 2
Circumference of C1 and C2 intersect
Input x1, y1, r1, x2, y2, r2:
5 4 3 5 4 2
C2 is in C1
Input x1, y1, r1, x2, y2, r2:
5 4 2 5 4 3
C1 is in C2
"""

import math
print("Input x1, y1, r1, x2, y2, r2:")
x1,y1,r1,x2,y2,r2 = [float(i) for i in input().split()]
d = math.sqrt((x1-x2)**2 + (y1-y2)**2)
if d <= r1-r2:
    print("C2  is in C1")
elif d <= r2-r1:
    print("C1  is in C2")
elif d < r1+r2:
    print("Circumference of C1  and C2  intersect")
elif d == r1+r2:
    print("Circumference of C1 and C2 will touch")
else:
    print("C1 and C2  do not overlap")



"""Write a Python program that reads a date (from 2016/1/1 to 2016/12/31) and prints the day of the date. Jan. 1, 2016, is Friday. Note that 2016 is a leap year. Go to the editor
Input:
Two integers m and d separated by a single space in a line, m ,d represent the month and the day.
Input month and date (separated by a single space):
5 15
Name of the date: Sunday"""

from datetime import date
print("Input month and date (separated by a single space):")
m, d = map(int, input().split())
weeks = {1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday',6:'Saturday',7:'Sunday'}
w = date.isoweekday(date(2016, m, d))
print("Name of the date: ",weeks[w])

"""
Write a Python program that reads text (only alphabetical characters and spaces) and prints two words.
The first word is the one that appears most often in the text. The second one is the word with the most letters.
Note: A word is a sequence of letters which is separated by the spaces.

Input:
A text is given in a line with following condition:
a. The number of letters in the text is less than or equal to 1000.
b. The number of letters in a word is less than or equal to 32.
c. There is only one word which is arise most frequently in given text.
d. There is only one word which has the maximum number of letters in given text.
Input text: Thank you for your comment and your participation.
Output: your participation.
"""

import collections
print("Input a text in a line.")
text_list = list(map(str, input().split()))
sc = collections.Counter(text_list)
common_word = sc.most_common()[0][0]
max_char = ""
for s in text_list:
    if len(max_char) < len(s):
        max_char = s
print("\nMost frequent text and the word which has the maximum number of letters.")
print(common_word, max_char)


"""
Write a Python program that reads n digits (given) chosen from 0 to 9 and prints the number of combinations where the sum of the digits equals another given number (s).
Do not use the same digits in a combination.
Input:
Two integers as number of combinations and their sum by a single space in a line. Input 0 0 to exit.
Input number of combinations and sum, input 0 0 to exit:
5 6
2 4
0 0
2
"""

import itertools
print("Input number of combinations and sum, input 0 0 to exit:")
while True:
  x, y = map(int, input(). split())
  if x == 0 and y == 0:
    break
  s = list(itertools.combinations(range(10), x))
  ctr = 0
  for i in s:
    if sum(i) == y:
            ctr += 1
 
print(ctr)

"""
Write a Python program that reads the two adjoining sides and the diagonal of a parallelogram and checks whether the parallelogram is a rectangle or a rhombus. Go to the editor
According to Wikipedia-
parallelograms: In Euclidean geometry, a parallelogram is a simple (non-self-intersecting) quadrilateral with two pairs of parallel sides. The opposite or facing sides of a parallelogram are of equal length and the opposite angles of a parallelogram are of equal measure.
rectangles: In Euclidean plane geometry, a rectangle is a quadrilateral with four right angles. It can also be defined as an equiangular quadrilateral, since equiangular means that all of its angles are equal (360°/4 = 90°). It can also be defined as a parallelogram containing a right angle.
rhombus: In plane Euclidean geometry, a rhombus (plural rhombi or rhombuses) is a simple (non-self-intersecting) quadrilateral whose four sides all have the same length. Another name is equilateral quadrilateral, since equilateral means that all of its sides are equal in length. The rhombus is often called a diamond, after the diamonds suit in playing cards which resembles the projection of an octahedral diamond, or a lozenge, though the former sometimes refers specifically to a rhombus with a 60° angle, and the latter sometimes refers specifically to a rhombus with a 45° angle.
Input:
Two adjoined sides and the diagonal.
1 <= ai, bi, ci <= 1000, ai + bi > ci
Input two adjoined sides and the diagonal of a parallelogram (comma separated):
3,4,5
This is a rectangle.
"""

print("Input two adjoined sides and the diagonal of a parallelogram (comma separated):")
a,b,c = map(int, input().split(","))
if c**2 == a**2+b**2 :
    print("This is a rectangle.")
if a == b:
    print("This is a rhombus.")


"""
Write a Python program to replace a string "Python" with "Java" and "Java" with "Python" in a given string. 
Input:
English letters (including single byte alphanumeric characters, blanks, symbols) are given on one line.
The length of the input character string is 1000 or less.
Input a text with two words 'Python' and 'Java'
Python is popular than Java
Java is popular than Python
"""

print("Input a text with two words 'Python' and 'Java'")
text = input().split()
for i in range(len(text)):
    if "Python" in text[i]:n = text[i].index("Python")text[i] = text[i][:n] + "Java" + text[i][n + 6:]
    elif "Java" in text[i]:n = text[i].index("Java")text[i] = text[i][:n] + "Python" + text[i][n + 4:]
print(*text)


"""
Write a Python program that determines the difference between the largest and smallest integers created by 8 numbers from 0 to 9. 
The number that can be rearranged shall start with 0 as in 00135668.
Input:
Input an integer created by 8 numbers from 0 to 9.:
2345
Difference between the largest and the smallest integer from the given integer:
3087
"""

print("Input an integer created by 8 numbers from 0 to 9.:")
num = list(input())
print("Difference between the largest and the smallest integer from the given integer:")
print(int("".join(sorted(num,reverse=True))) - int("".join(sorted(num))))

"""
Write a Python program to compute the sum of the first n prime numbers. Go to the editor
Input:
n ( n <= 10000). Input 0 to exit the program.
Input a number (n<=10000) to compute the sum:(0 to exit)
25
Sum of first 25 prime numbers:
1060
"""

MAX = 105000
print("Input a number (n≤10000) to compute the sum:(0 to exit)") 
is_prime = [True for _ in range(MAX)]
is_prime[0] = is_prime[1] = False
for i in range(2, int(MAX ** (1 / 2)) + 1):
  if is_prime[i]:
    for j in range(i ** 2, MAX, i):
      is_prime[j] = False 
primes = [i for i in range(MAX) if is_prime[i]] 
while True:
  n = int(input())
  if not n:
    break
  print("Sum of first",n,"prime numbers:")
  print(sum(primes[:n]))

"""
Write a Python program which accepts an even number (>=4, Goldbach number) from the user and creates combinations which express the given number as a sum of two prime numbers. Print the number of combinations. Go to the editor
Goldbach number: A Goldbach number is a positive even integer that can be expressed as the sum of two odd primes.[4] Since four is the only even number greater than two that requires the even prime 2 in order to be written as the sum of two primes, another form of the statement of Goldbach's conjecture is that all even integers greater than 4 are Goldbach numbers.
The expression of a given even number as a sum of two primes is called a Goldbach partition of that number. The following are examples of Goldbach partitions for some even numbers:
6 = 3 + 3
8 = 3 + 5
10 = 3 + 7 = 5 + 5
12 = 7 + 5
...
100 = 3 + 97 = 11 + 89 = 17 + 83 = 29 + 71 = 41 + 59 = 47 + 53
Input an even number (0 to exit):
100
Number of combinations:
6
"""

import sys
from bisect import bisect_right
from itertools import chain, compress
print("Input an even number (0 to exit):") 
ub = 50000
is_prime = [0, 0, 1, 1] + [0]*(ub-3)
is_prime[5::6] = is_prime[7::6] = [1]*int(ub/6)
primes = [2, 3]
append = primes.append
 
for n in chain(range(5, ub, 6), range(7, ub, 6)):
    if is_prime[n]:
        append(n)
        is_prime[n*3::n*2] = [0]*((ub-n)//(n*2))
primes.sort()

for n in map(int, sys.stdin):
    if not n:
        break
    if n%2:
        print("Number of combinations:")  
        print(is_prime[n-2])
    else:
        print("Number of combinations:")  
        print(len([1 for p in primes[:bisect_right(primes, n/2)] if is_prime[n-p]]))

"""
If you draw a straight line on a plane, the plane is divided into two regions.
For example, if you draw two straight lines in parallel, you get three areas, and if you draw vertically one to the other you get 4 areas.
Write a Python program to create the maximum number of regions obtained by drawing n given straight lines.
Input:
(1 <= n <= 10,000)
Input number of straight lines (o to exit):
5
Number of regions:
16
"""

while True:
    print("Input number of straight lines (o to exit): ")
    n=int(input())
    if n<=0:
        break
    print("Number of regions:") 
    print((n*n+n+2)//2)

"""
There are four different points on a plane, P(xp,yp), Q(xq, yq), R(xr, yr) and S(xs, ys).
Write a Python program to determine whether AB and CD are orthogonal.
Input:
xp,yp, xq, yq, xr, yr, xs and ys are -100 to 100 respectively and each value can be up to 5 digits after the decimal point It is given as a real number including the number of. Output:
Output AB and CD are not orthogonal! or AB and CD are orthogonal!.
"""

"""Write a Python program to sum all numerical values (positive integers) embedded in a sentence. Go to the editor
Input:
Sentences with positive integers are given over multiple lines.
Each line is a character string containing one-byte alphanumeric characters, symbols, spaces, or an empty line. However the input is 80 characters or less per line and the sum is 10,000 or less.
Input some text and numeric values ( to exit):
Sum of the numeric values: 80
None
Input some text and numeric values ( to exit):
Sum of the numeric values: 17
None
Input some text and numeric values ( to exit):
Sum of the numeric values: 10
None"""

import sys,re
def test(stri):
  print("Input some text and numeric values (<ctrl-d> to exit):")
  print("Sum of the numeric values: ",sum([sum(map(int,re.findall(r"[0-9]{1,5}",stri)))]))

print(test("sd1fdsfs23 dssd56"))
print(test("15apple2banana"))
print(test("flowers5fruit5"))


"""There are 10 vertical and horizontal squares on a plane. Each square is painted blue and green. Blue represents the sea, and green represents the land. When two green squares are in contact with the top and bottom, or right and left, they are said to be ground. The area created by only one green square is called "island". For example, there are five islands in the figure below.
Write a Python program to read the mass data and find the number of islands. Go to the editor
Input:
Input 10 rows of 10 numbers representing green squares (island) as 1 and blue squares (sea) as zeros
1100000111
1000000111
0000000111
0010001000
0000011100
0000111110
0001111111
1000111110
1100011100
1110001000
Number of islands:
5"""

c=0
def f(x,y,z):
    if 0<=y<10 and 0<=z<10 and x[z][y]=='1':
        x[z][y]='0'
        for dy,dz in [[-1,0],[1,0],[0,-1],[0,1]]:f(x,y+dy,z+dz)
print("Input 10 rows of 10 numbers representing green squares (island) as 1 and blue squares (sea) as zeros") 
while 1:
    try:
        if c:input()
    except:break
    x = [list(input()) for _ in [0]*10]
    c=1;b=0
    for i in range(10):
        for j in range(10):
            if x[j][i]=='1':
                b+=1;f(x,i,j)
    print("Number of islands:")     
    print(b)


"""When character are consecutive in a string , it is possible to shorten the character string by replacing the character with a certain rule. For example, in the case of the character string YYYYY, if it is expressed as 5 Y, it is compressed by one character.
Write a Python program to restore the original string by entering the compressed string with this rule. However, the character does not appear in the restored character string. Go to the editor
Input:
The restored character string for each character on one line.
Original text: XY#6Z1#4023
XYZZZZZZ1000023
Original text: #39+1=1#30
999+1=1000"""

def restore_original_str(a1):
  result = ""
  ind = 0
  end = len(a1)
  while ind < end:
    if a1[ind] == "#":
      result += a1[ind + 2] * int(a1[ind + 1])
      ind += 3
    else:
      result += a1[ind]
      ind += 1
  return result
print("Original text:","XY#6Z1#4023")
print(restore_original_str("XY#6Z1#4023"))
print("Original text:","#39+1=1#30")
print(restore_original_str("#39+1=1#30"))


"""A convex polygon is a simple polygon in which no line segment between two points on the boundary ever goes outside the polygon. Equivalently, it is a simple polygon whose interior is a convex set. In a convex polygon, all interior angles are less than or equal to 180 degrees, while in a strictly convex polygon all interior angles are strictly less than 180 degrees.
Write a Python program that compute the area of the polygon . The vertices have the names vertex 1, vertex 2, vertex 3, ... vertex n according to the order of edge connections Go to the editor
Note: The original sentences are uppercase letters, lowercase letters, numbers, symbols, less than 100 letters, and consecutive letters are not more than 9 letters.
Input:
Input number of sides: 5
Side: 1
Input the Coordinate:
Input Coordinate x: 1
Input Coordinate y: 0
Side: 2
Input the Coordinate:
Input Coordinate x: 0
Input Coordinate y: 0
Side: 3
Input the Coordinate:
Input Coordinate x: 1
Input Coordinate y: 1
Side: 4
Input the Coordinate:
Input Coordinate x: 2
Input Coordinate y: 0
Side: 5
Input the Coordinate:
Input Coordinate x: -1
Input Coordinate y: 1
Area of the Polygon: 0.5
"""

def poly_area(c):
  add = []
  for i in range(0, (len(c) - 2), 2):
    add.append(c[i] * c[i + 3] - c[i + 1] * c[i + 2])
    add.append(c[len(c) - 2] * c[1] - c[len(c) - 1] * c[0])
    return abs(sum(add) / 2)
no_sides = int(input('Input number of sides: '))
cord_data = []
for z in range(no_sides):
    print("Side:",z+1)
    print("Input the Coordinate:")
    x = int(input('Input Coordinate x:'))
    y = int(input('Input Coordinate y:'))
    cord_data.append(x)
    cord_data.append(y)
print("\nArea of the Polygon:",poly_area(cord_data))


"""
Internet search engine giant, such as Google accepts web pages around the world and classify them, creating a huge database. The search engines also analyze the search keywords entered by the user and create inquiries for database search. In both cases, complicated processing is carried out in order to realize efficient retrieval, but basics are all cutting out words from sentences.
Write a Python program to cut out words of 3 to 6 characters length from a given sentence not more than 1024 characters. Go to the editor
Input:
English sentences consisting of delimiters and alphanumeric characters are given on one line.
Input a sentence (1024 characters. max.)
The quick brown fox
3 to 6 characters length of words:
The quick brown fox
"""

print("Input a sentence (1024 characters. max.)")
yy = input()
yy = yy.replace(",", " ")
yy = yy.replace(".", " ")
print("3 to 6 characters length of words:")
print(*[y for y in yy.split() if 3 <= len(y) <= 6])


"""
Arrange integers (0 to 99) as narrow hilltop, as illustrated in Figure 1. Reading such data representing huge, when starting from the top and proceeding according to the next rule to the bottom. Write a Python program that compute the maximum value of the sum of the passing integers. Go to the editor
Input:
A series of integers separated by commas are given in diamonds. No spaces are included in each line. The input example corresponds to Figure 1. The number of lines of data is less than 100 lines.
Output:
The maximum value of the sum of integers passing according to the rule on one line.
Input the numbers (ctrl+d to exit):
8
4, 9
9, 2, 1
3, 8, 5, 5
5, 6, 3, 7, 6
3, 8, 5, 5
9, 2, 1
4, 9
8
Maximum value of the sum of integers passing according to the rule on one line.
64
"""

import sys
print("Input the numbers (ctrl+d to exit):")
nums = [list(map(int, l.split(","))) for l in sys.stdin]
mvv = nums[0]

for i in range(1, (len(nums)+1)//2):
    rvv = [0]*(i+1)
    for j in range(i):
        rvv[j] = max(rvv[j], mvv[j]+nums[i][j])
        rvv[j+1] = max(rvv[j+1], mvv[j]+nums[i][j+1])
    mvv = rvv

for i in range((len(nums)+1)//2, len(nums)):
    rvv = [0]*(len(mvv)-1)
    for j in range(len(rvv)):
        rvv[j] = max(mvv[j], mvv[j+1]) + nums[i][j]
    mvv = rvv
print("Maximum value of the sum of integers passing according to the rule on one line.") 
print(mvv[0])


"""
Write a Python program to find the number of combinations that satisfy p + q + r + s = n where n is a given number <= 4000 and p, q, r, s are between 0 to 1000. Go to the editor
Input a positive integer: (ctrl+d to exit)
252
Number of combinations of a,b,c,d: 2731135
"""

from collections import Counter
print("Input a positive integer: (ctrl+d to exit)") 
pair_dict = Counter()
for i in range(2001):
  pair_dict[i] = min(i, 2000 - i) + 1 
 
while True:
  try:
    n = int(input())
    ans = 0
    for i in range(n + 1):
      ans += pair_dict[i] * pair_dict[n - i]
    print("Number of combinations of a,b,c,d:",ans) 
  except EOFError:
    break


"""
Write a Python program that adds up the columns and rows of the given table as shown in the specified figure. Go to the editor
Input number of rows/columns (0 to exit)
4
Input cell value:
25 69 51 26
68 35 29 54
54 57 45 63
61 68 47 59
Result:
25 69 51 26 171
68 35 29 54 186
54 57 45 63 219
61 68 47 59 235
208 229 172 202 811
Input number of rows/columns (0 to exit)
"""

while True:
    print("Input number of rows/columns (0 to exit)")
    n = int(input())
    if n == 0:
        break
    print("Input cell value:")
    x = []
    for i in range(n):
        x.append([int(num) for num in input().split()])

    for i in range(n):
        sum = 0
        for j in range(n):
            sum += x[i][j]
        x[i].append(sum)

    x.append([])
    for i in range(n + 1):
        sum = 0
        for j in range(n):
            sum += x[j][i]
        x[n].append(sum)
    print("Result:")
    for i in range(n + 1):
        for j in range(n + 1):
            print('{0:>5}'.format(x[i][j]), end="")
        print()

"""
Given a list of numbers and a number k, write a Python program to check whether the sum of any two numbers from the list is equal to k or not. Go to the editor
For example, given [1, 5, 11, 5] and k = 16, return true since 11 + 5 is 16.
Sample Input:
([12, 5, 0, 5], 10)
([20, 20, 4, 5], 40)
([1, -1], 0)
([1, 1, 0], 0)
Sample Output:
True
True
True
False
"""

def check_sum(nums, k):   
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == k:
                return True
    return False
print(check_sum([12, 5, 0, 5], 10))
print(check_sum([20, 20, 4, 5], 40))
print(check_sum([1, -1], 0))
print(check_sum([1, 1, 0], 0))


"""
In mathematics, a subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements. For example, the sequence (A,B,D) is a subsequence of (A,B,C,D,E,F) obtained after removal of elements C, E, and F. The relation of one sequence being the subsequence of another is a preorder.
The subsequence should not be confused with substring (A,B,C,D) which can be derived from the above string (A,B,C,D,E,F) by deleting substring (E,F). The substring is a refinement of the subsequence.
The list of all subsequences for the word "apple" would be "a", "ap", "al", "ae", "app", "apl", "ape", "ale", "appl", "appe", "aple", "apple", "p", "pp", "pl", "pe", "ppl", "ppe", "ple", "pple", "l", "le", "e", "".
Write a Python program to find the longest word in a set of words which is a subsequence of a given string. Go to the editor
Sample Input:
("Green", {"Gn", "Gren", "ree", "en"})
("pythonexercises", {"py", "ex", "exercises"})
Sample Output:
Gren
exercises
"""

def longest_word_sequence(s, d):
	long_word = ""
	
	for word in d: 
		temp_word = ''	
		j = 0
		for letter in word: 

			for i in range(j, len(s)): 

				if letter == s[i]: 
					temp_word += letter 
					j = i                  
					break
				else:				
					continue        

		if (temp_word) == word and len(long_word) < len(temp_word):
			long_word = temp_word

		else:
			continue
	return long_word


print(longest_word_sequence("Green", {"Gn", "Gren", "ree", "en"}))
print(longest_word_sequence("pythonexercises", {"py", "ex", "exercises"}))


"""
From Wikipedia, the free encyclopaedia:
A happy number is defined by the following process:
Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers, while those that do not end in 1 are unhappy numbers.
Write a Python program to check whether a number is "happy" or not. Go to the editor
Sample Input:
(7)
(932)
(6)
Sample Output:
True
True
False
"""

def is_Happy_num(n):
  past = set()
  while n != 1:
        n = sum(int(i)**2 for i in str(n))
        if n in past:
            return False
        past.add(n)
  return True
print(is_Happy_num(7))
print(is_Happy_num(932))
print(is_Happy_num(6))

"""
From Wikipedia,
A happy number is defined by the following process:
Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers, while those that do not end in 1 are unhappy numbers.
Write a Python program to find and print the first 10 happy numbers. Go to the editor
Sample Input:
[:10]
Sample Output:
[1, 7, 10, 13, 19, 23, 28, 31, 32, 44]
"""

def happy_numbers(n):
    past = set()			
    while n != 1:
        n = sum(int(i)**2 for i in str(n))
        if n in past:
            return False
        past.add(n)
    return True
print([x for x in range(500) if happy_numbers(x)][:10])



"""
Write a Python program that counts the number of prime numbers that are less than a given non-negative number. Go to the editor
Sample Input:
(10)
(100)
Sample Output:
4
25
"""

def count_Primes_nums(n):
    ctr = 0
    
    for num in range(n):
        if num <= 1:
            continue
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            ctr += 1

    return ctr

print(count_Primes_nums(10))
print(count_Primes_nums(100))


"""
In abstract algebra, a group isomorphism is a function between two groups that sets up a one-to-one correspondence between the elements of the groups in a way that respects the given group operations. If there exists an isomorphism between two groups, then the groups are called isomorphic.
Two strings are isomorphic if the characters in string A can be replaced to get string B
Given "foo", "bar", return false.
Given "paper", "title", return true.
Write a Python program to check if two given strings are isomorphic to each other or not. Go to the editor
Sample Input:
("foo", "bar")
("bar", "foo")
("paper", "title")
("title", "paper")
("apple", "orange")
("aa", "ab")
("ab", "aa")
Sample Output:
False
False
True
True
False
False
False
"""

def isIsomorphic(str1, str2):          
    dict_str1 = {}
    dict_str2 = {}
    
    for i, value in enumerate(str1):
        dict_str1[value] = dict_str1.get(value, []) + [i]
            
    for j, value in enumerate(str2):
        dict_str2[value] = dict_str2.get(value, []) + [j]
    
    if sorted(dict_str1.values()) == sorted(dict_str2.values()):
        return True
    else:
        return False

print(isIsomorphic("foo", "bar"))   
print(isIsomorphic("bar", "foo")) 
print(isIsomorphic("paper", "title")) 
print(isIsomorphic("title", "paper"))
print(isIsomorphic("apple", "orange"))
print(isIsomorphic("aa", "ab"))
print(isIsomorphic("ab", "aa"))


"""
Write a Python program to find the longest common prefix string among a given array of strings. Return false if there is no common prefix.
For Example, longest common prefix of "abcdefgh" and "abcefgh" is "abc". Go to the editor
Sample Input:
["abcdefgh","abcefgh"]
["w3r","w3resource"]
["Python","PHP", "Perl"]
["Python","PHP", "Java"]
Sample Output:
abc
w3r
P
"""

def longest_Common_Prefix(str1):
    
    if not str1:
        return ""

    short_str = min(str1,key=len)

    for i, char in enumerate(short_str):
        for other in str1:
            if other[i] != char:
                return short_str[:i]

    return short_str 

print(longest_Common_Prefix(["abcdefgh","abcefgh"]))
print(longest_Common_Prefix(["w3r","w3resource"]))
print(longest_Common_Prefix(["Python","PHP", "Perl"]))
print(longest_Common_Prefix(["Python","PHP", "Java"]))


"""
Write a Python program to reverse only the vowels of a given string. Go to the editor
Sample Input:
("w3resource")
("Python")
("Perl")
("USA")
Sample Output:
w3resuorce
Python
Perl
ASU
"""

def reverse_vowels(str1):
	vowels = ""
	for char in str1:
		if char in "aeiouAEIOU":
			vowels += char
	result_string = ""
	for char in str1:
		if char in "aeiouAEIOU":
			result_string += vowels[-1]
			vowels = vowels[:-1]
		else:
			result_string += char
	return result_string
print(reverse_vowels("w3resource"))
print(reverse_vowels("Python"))
print(reverse_vowels("Perl"))
print(reverse_vowels("USA"))


"""
Write a Python program to check whether a given integer is a palindrome or not. Go to the editor
Note: An integer is a palindrome when it reads the same backward as forward. Negative numbers are not palindromic.
Sample Input:
(100)
(252)
(-838)
Sample Output:
False
True
False
"""

def is_Palindrome(n):
    return str(n) == str(n)[::-1]
print(is_Palindrome(100))
print(is_Palindrome(252))
print(is_Palindrome(-838)) 


"""
Write a Python program that removes duplicate elements from a given array of numbers so that each element appears only once and returns the new length of the array. Go to the editor
Sample Input:
[0,0,1,1,2,2,3,3,4,4,4]
[1, 2, 2, 3, 4, 4]
Sample Output:
5
4
"""

def remove_duplicates(nums):
    for i in range (len(nums)-1, 0, -1):
        if nums[i] == nums[i-1]:
            del nums[i-1]
    return len(nums)

print(remove_duplicates([0,0,1,1,2,2,3,3,4,4,4]))
print(remove_duplicates([1, 2, 2, 3, 4, 4]))


"""
Write a Python program to calculate the maximum profit from selling and buying values of stock. An array of numbers represent the stock prices in chronological order. Go to the editor
For example, given [8, 10, 7, 5, 7, 15], the function will return 10, since the buying value of the stock is 5 dollars and sell value is 15 dollars.
Sample Input:
([8, 10, 7, 5, 7, 15])
([1, 2, 8, 1])
([])
Sample Output:
10
7
0
"""

def buy_and_sell(stock_price):
    max_profit_val, current_max_val = 0, 0 
    for price in reversed(stock_price):                       
        current_max_val = max(current_max_val, price)          
        potential_profit = current_max_val - price          
        max_profit_val = max(potential_profit, max_profit_val)

    return max_profit_val

print(buy_and_sell([8, 10, 7, 5, 7, 15]))
print(buy_and_sell([1, 2, 8, 1]))
print(buy_and_sell([]))


"""
Write a Python program to remove all instances of a given value from a given array of integers and find the length of the newly created array. Go to the editor
Sample Input:
([1, 2, 3, 4, 5, 6, 7, 5], 5)
([10,10,10,10,10], 10)
([10,10,10,10,10], 20)
([], 1)
Sample Output:
6
0
5
0
"""

def remove_element(array_nums, val):
    i = 0
    while i < len(array_nums):
        if array_nums[i] == val:
            array_nums.remove(array_nums[i])

        else:
            i += 1

    return len(array_nums)
print(remove_element([1, 2, 3, 4, 5, 6, 7, 5], 5))
print(remove_element([10,10,10,10,10], 10)) 
print(remove_element([10,10,10,10,10], 20)) 
print(remove_element([], 1))


"""
Write a Python program to find the starting and ending position of a given value in a given array of integers, sorted in ascending order. Go to the editor
If the target is not found in the array, return [0, 0].
Input: [5, 7, 7, 8, 8, 8] target value = 8
Output: [0, 5]
Input: [1, 3, 6, 9, 13, 14] target value = 4
Output: [0, 0]
"""

def search_Range(array_nums, target_val):
  result_arra = []
  start_pos = 0
  end_pos = 0
  for i in range(len(array_nums)):
      if target_val == array_nums[i] and start_pos == -1:
          start_pos = i
          end_pos = i
      elif target_val == array_nums[i] and start_pos != -1:
          end_pos = i
  result_arra.append(start_pos)
  result_arra.append(end_pos)
  return result_arra
print(search_Range([5, 7, 7, 8, 8, 8], 8))
print(search_Range([1, 3, 6, 9, 13, 14], 4))
print(search_Range([5, 7, 7, 8, 10], 8))


"""
The price of a given stock on each day is stored in an array.
Write a Python program to find the maximum profit in one transaction i.e., buy one and sell one share of the stock from the given price value of the said array. You cannot sell a stock before you buy one. Go to the editor
Input (Stock price of each day): [224, 236, 247, 258, 259, 225]
Output: 35
Explanation:
236 - 224 = 12
247 - 224 = 23
258 - 224 = 34
259 - 224 = 35
225 - 224 = 1
247 - 236 = 11
258 - 236 = 22
259 - 236 = 23
225 - 236 = -11
258 - 247 = 11
259 - 247 = 12
225 - 247 = -22
259 - 258 = 1
225 - 258 = -33
225 - 259 = -34
"""

def max_profit(stock_price):
	max_profit_amt = 0

	for i in range(len(stock_price)):
		profit_amt = 0
		for j in range(i+1, len(stock_price)):
			profit_amt = stock_price[j] - stock_price[i]
			if  profit_amt > max_profit_amt:
				max_profit_amt = profit_amt
	return max_profit_amt
print(max_profit([224, 236, 247, 258, 259, 225]))



"""
Write a Python program to print a given N by M matrix of numbers line by line in forward > backwards > forward >... order. Go to the editor
Input matrix:
[[1, 2, 3,4],
[5, 6, 7, 8],
[0, 6, 2, 8],
[2, 3, 0, 2]]
Output:
1
2
3
4
8
7
6
5
0
6
2
8
2
0
3
2
"""

def print_matrix(nums):
    flag = True 
    
    for line in nums:

        if flag == True: 
            i = 0
            while i < len(line):
                print(line[i])
                i += 1
            flag = False

        else: 
            i = -1
            while i > -1 * len(line) - 1:
                print(line[i])
                i = i - 1
            flag = True
print_matrix([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [0, 6, 2, 8],
              [2, 3, 0, 2]])


"""
Write a Python program to compute the largest product of three integers from a given list of integers. Go to the editor
Sample Input:
[-10, -20, 20, 1]
[-1, -1, 4, 2, 1]
[1, 2, 3, 4, 5, 6]
Sample Output:
4000
8
120
"""

def largest_product_of_three(nums):
    max_val = nums[1]

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                max_val = max(nums[i] * nums[j] * nums[k], max_val)
                
    return max_val
    
print(largest_product_of_three([-10, -20, 20, 1]))
print(largest_product_of_three([-1, -1, 4, 2, 1]))
print(largest_product_of_three([1, 2, 3, 4, 5, 6]))

"""
Write a Python program to find the first missing positive integer that does not exist in a given list. Go to the editor
Sample Input:
[2, 3, 7, 6, 8, -1, -10, 15, 16]
[1, 2, 4, -7, 6, 8, 1, -10, 15]
[1, 2, 3, 4, 5, 6, 7]
[-2, -3, -1, 1, 2, 3]
Sample Output:
4
3
8
4
"""

def first_missing_number(nums):
    if len(nums) == 0:
        return 1
        
    nums.sort()
    smallest_int_num = 0
    
    for i in range(len(nums) - 1):

        if nums[i] <= 0 or nums[i] == nums[i + 1]:
            continue
        else:
            if nums[i + 1] - nums[i] != 1:
                smallest_int_num = nums[i] + 1
                return smallest_int_num    
    if smallest_int_num == 0:
        smallest_int_num = nums[-1] + 1
    return smallest_int_num

print(first_missing_number([2, 3, 7, 6, 8, -1, -10, 15, 16])) 
print(first_missing_number([1, 2, 4, -7, 6, 8, 1, -10, 15]))
print(first_missing_number([1, 2, 3, 4, 5, 6, 7]))
print(first_missing_number([-2, -3, -1, 1, 2, 3]))


"""
Write a Python program to randomly generate a list of 10 even numbers between 1 and 100 inclusive. Go to the editor
Note: Use random.sample() to generate a list of random values.
Sample Input:
(1,100)
Sample Output:
[4, 22, 8, 20, 24, 12, 30, 98, 28, 48]
"""

import random
print(random.sample([i for i in range(1,100) if i%2==0], 10))

"""
Write a Python program to calculate the median from a list of numbers. Go to the editor
Sample Input:
[1,2,3,4,5]
[1,2,3,4,5,6]
[6,1,2,4,5,3]
[1.0,2.11,3.3,4.2,5.22,6.55]
[1.0,2.11,3.3,4.2,5.22]
[2.0,12.11,22.3,24.12,55.22]
Sample Output:
3
3.5
3.5
3.75
3.3
22.3
"""

def cal_median(nums):
  nums.sort()
  n = len(nums)
  m = n // 2
  if n % 2 == 0:
    return (nums[m - 1] + nums[m]) / 2
  else:
    return nums[m]
print(cal_median([1,2,3,4,5]))
print(cal_median([1,2,3,4,5,6]))
print(cal_median([6,1,2,4,5,3]))
print(cal_median([1.0,2.11,3.3,4.2,5.22,6.55]))
print(cal_median([1.0,2.11,3.3,4.2,5.22]))
print(cal_median([2.0,12.11,22.3,24.12,55.22]))


"""
Write a Python program to test whether a given number is symmetrical or not. A number is symmetrical when it is equal to its reverse. Go to the editor
A number is symmetrical when it is equal of its reverse.
Sample Input:
(121)
(0)
(122)
(990099)
Sample Output:
True
True
False
True
"""

def is_symmetrical_num(n):
  return str(n) == str(n)[::-1]
print(is_symmetrical_num(121))
print(is_symmetrical_num(0))
print(is_symmetrical_num(122))
print(is_symmetrical_num(990099))


"""
Write a Python program that accepts a list of numbers. Count the negative numbers and compute the sum of the positive numbers of the said list. Return these values through a list. Go to the editor
Original list: [1, 2, 3, 4, 5]
Number of negative of numbers and sum of the positive numbers of the said list: [0, 15]
Original list: [-1, -2, -3, -4, -5]
[5, 0]
Number of negative of numbers and sum of the positive numbers of the said list: [5, 0]
Original list: [1, 2, 3, -4, -5]
[2, 6]
Number of negative of numbers and sum of the positive numbers of the said list: [2, 6]
Original list: [1, 2, -3, -4, -5]
[3, 3]
Number of negative of numbers and sum of the positive numbers of the said list: [3, 3]
"""

def count_sum(nums):
   if not nums: return []
   return [len([n for n in nums if n < 0]), sum(n for n in nums if n > 0)]
nums = [1, 2, 3, 4, 5]
print("Original list:",nums)
print("Number of negative of numbers and sum of the positive numbers of the said list:",count_sum(nums))
nums = [-1, -2, -3, -4, -5]
print("Original list:",nums)
print(count_sum(nums))
print("Number of negative of numbers and sum of the positive numbers of the said list:",count_sum(nums))
nums = [1, 2, 3, -4, -5]
print("Original list:",nums)
print(count_sum(nums))
print("Number of negative of numbers and sum of the positive numbers of the said list:",count_sum(nums))
nums = [1, 2, -3, -4, -5]
print("Original list:",nums)
print(count_sum(nums))
print("Number of negative of numbers and sum of the positive numbers of the said list:",count_sum(nums)) 


"""
From Wikipedia:
An isogram (also known as a "nonpattern word") is a logological term for a word or phrase without a repeating letter. It is also used by some people to mean a word or phrase in which each letter appears the same number of times, not necessarily just once. Conveniently, the word itself is an isogram in both senses of the word, making it autological.
Write a Python program to check whether a given string is an "isogram" or not. Go to the editor
Sample Input:
("w3resource")
("w3r")
("Python")
("Java")
Sample Output:
False
True
True
False
"""

def check_isogram(str1):
    return len(str1) == len(set(str1.lower()))

print(check_isogram("w3resource"))
print(check_isogram("w3r"))
print(check_isogram("Python"))
print(check_isogram("Java"))


"""
Write a Python program to count the number of equal numbers from three given integers. Go to the editor
Sample Input:
(1, 1, 1)
(1, 2, 2)
(-1, -2, -3)
(-1, -1, -1)
Sample Output:
3
2
0
3
"""

def test_three_equal(x, y, z):
  result= set([x, y, z])
  if len(result)==3:
    return 0
  else:
    return (4 - len(result))

print(test_three_equal(1, 1, 1))
print(test_three_equal(1, 2, 2))
print(test_three_equal(-1, -2, -3))
print(test_three_equal(-1, -1, -1))


"""
Write a Python program to check whether a given employee code is exactly 8 digits or 12 digits. Return True if the employee code is valid and False if it's not. Go to the editor
Sample Input:
('12345678')
('1234567j')
('12345678j')
('123456789123')
('123456abcdef')
Sample Output:
True
False
False
True
False
"""

def is_valid_emp_code(emp_code):
  return len(emp_code) in [8, 12] and emp_code.isdigit()
print(is_valid_emp_code('12345678'))
print(is_valid_emp_code('1234567j'))
print(is_valid_emp_code('12345678j'))
print(is_valid_emp_code('123456789123'))
print(is_valid_emp_code('123456abcdef'))


"""
Write a Python program that accepts two strings and determines whether the letters in the second string are present in the first string. Go to the editor
Sample Input:
["python", "ypth"]
["python", "ypths"]
["python", "ypthon"]
["123456", "01234"]
["123456", "1234"]
Sample Output:
True
False
True
False
True
"""

def string_letter_check(str1, str2):
  return all([char in str1.lower() for char in str2.lower()])
print(string_letter_check("python", "ypth"))
print(string_letter_check("python", "ypths"))
print(string_letter_check("python", "ypthon"))
print(string_letter_check("123456", "01234"))
print(string_letter_check("123456", "1234"))


"""
Write a Python program to compute the sum of the three lowest positive numbers from a given list of numbers. Go to the editor
Original list of numbers: [10, 20, 30, 40, 50, 60, 7]
Sum of the three lowest positive numbers of the said array: 37
Original list of numbers: [1, 2, 3, 4, 5]
Sum of the three lowest positive numbers of the said array: 6
Original list of numbers: [0, 1, 2, 3, 4, 5]
Sum of the three lowest positive numbers of the said array: 6
"""

def sum_three_smallest_nums(lst):
	return sum(sorted([x for x in lst if x > 0])[:3])
nums = [10, 20, 30, 40, 50, 60, 7]
print("Original list of numbers: ",nums)
print("Sum of the three lowest positive numbers of the said array: ",sum_three_smallest_nums(nums))
nums = [1, 2, 3, 4, 5]
print("\nOriginal list of numbers: ",nums)
print("Sum of the three lowest positive numbers of the said array: ",sum_three_smallest_nums(nums))
nums = [0, 1, 2, 3, 4, 5]
print("\nOriginal list of numbers: ",nums)
print("Sum of the three lowest positive numbers of the said array: ",sum_three_smallest_nums(nums))


"""
Write a Python program that replaces all but the last five characters of a string with "*" and returns the modified string. Go to the editor
Original String: kdi39323swe
new string: ******23swe
Original String: 12345abcdef
new string: ******bcdef
Original String: 12345
new string: 12345
"""

def new_string(str1):
 return '*'*(len(str1)-5) + str1[-5:]
text = "kdi39323swe"
print("Original String: ",text)
print("new string: ",new_string(text))
text = "12345abcdef"
print("\nOriginal String: ",text)
print("new string: ",new_string(text))
text = "12345"
print("\nOriginal String: ",text)
print("new string: ",new_string(text))


"""
Write a Python program to count the number of arguments in a given function. Go to the editor
Sample Input:
()
(1)
(1, 2)
(1, 2, 3)
(1, 2, 3, 4)
[1, 2, 3, 4]
Sample Output:
0
1
2
3
4
1
"""

def num_of_args(*args):
	return(len(args))
print(num_of_args())
print(num_of_args(1))
print(num_of_args(1, 2))
print(num_of_args(1, 2, 3))
print(num_of_args(1, 2, 3, 4))
print(num_of_args([1, 2, 3, 4]))


"""
Write a Python program to compute the cumulative sum of numbers in a given list. Go to the editor
Note: Cumulative sum = sum of itself + all previous numbers in the said list.
Sample Input:
[10, 20, 30, 40, 50, 60, 7]
[1, 2, 3, 4, 5]
[0, 1, 2, 3, 4, 5]
Sample Output:
[10, 30, 60, 100, 150, 210, 217]
[1, 3, 6, 10, 15]
[0, 1, 3, 6, 10, 15]
"""

def nums_cumulative_sum(nums_list):
  return [sum(nums_list[:i+1]) for i in range(len(nums_list))]

print(nums_cumulative_sum([10, 20, 30, 40, 50, 60, 7]))
print(nums_cumulative_sum([1, 2, 3, 4, 5]))
print(nums_cumulative_sum([0, 1, 2, 3, 4, 5]))


"""
Write a Python program to find the central character(s) of a given string. Return the two middle characters if the length of the string is even. Return the middle character if the length of the string is odd. Go to the editor
Original string: Python
Middle character(s) of the said string: th
Original string: PHP
Middle character(s) of the said string: H
Original string: Java
Middle character(s) of the said string: av
"""

def middle_char(txt):
  return txt[(len(txt)-1)//2:(len(txt)+2)//2]
text = "Python"
print("Original string: ",text)
print("Middle character(s) of the said string: ",middle_char(text))
text = "PHP"
print("Original string: ",text)
print("Middle character(s) of the said string: ",middle_char(text))
text = "Java"
print("Original string: ",text)
print("Middle character(s) of the said string: ",middle_char(text))


"""
Write a Python program to find the largest product of a pair of adjacent elements from a given list of integers. Go to the editor
Original list: [1, 2, 3, 4, 5, 6]
Largest product of the pair of adjacent elements of the said list: 30
Original list: [1, 2, 3, 4, 5]
Largest product of the pair of adjacent elements of the said list: 20
Original list: [2, 3]
Largest product of the pair of adjacent elements of the said list: 6
"""

def adjacent_num_product(list_nums):
   return max(a*b for a, b in zip(list_nums, list_nums[1:]))
nums = [1,2,3,4,5,6]
print("Original list: ",nums)
print("Largest product of the pair of adjacent elements of the said list:", adjacent_num_product(nums))
nums = [1,2,3,4,5]
print("\nOriginal list: ",nums)
print("Largest product of the pair of adjacent elements of the said list:", adjacent_num_product(nums))
nums = [2,3]
print("\nOriginal list: ",nums)
print("Largest product of the pair of adjacent elements of the said list:", adjacent_num_product(nums))


"""
Write a Python program that checks whether every even index contains an even number and every odd index contains an odd number of a given list. Go to the editor
Original list of numbers: [2, 1, 4, 3, 6, 7, 6, 3]
Check whether every even index contains an even number and every
odd index contains odd number of a given list:
True
Original list of numbers: [2, 1, 4, 3, 6, 7, 6, 4]
Check whether every even index contains an even number and every
odd index contains odd number of a given list:
False
Original list of numbers: [2, 1, 4, 3, 6, 7, 6, 4]
Check whether every even index contains an even number and every
odd index contains odd number of a given list:
True
"""

def odd_even_position(nums):
           return all(nums[i]%2==i%2 for i in range(len(nums)))
nums = [2, 1, 4, 3, 6, 7, 6, 3]
print("Original list of numbers:", nums)
print("Check whether every even index contains an even number and every \nodd index contains odd number of a given list:")
print(odd_even_position(nums))
nums = [2, 1, 4, 3, 6, 7, 6, 4]
print("\nOriginal list of numbers:", nums)
print("Check whether every even index contains an even number and every \nodd index contains odd number of a given list:")
print(odd_even_position(nums))
print("\nOriginal list of numbers:", nums)
nums = [4, 1, 2]
print("Check whether every even index contains an even number and every \nodd index contains odd number of a given list:")
print(odd_even_position(nums))



"""
 Write a Python program to check whether a given number is a narcissistic number or not. Go to the editor

If you are a reader of Greek mythology, then you are probably familiar with Narcissus. He was a hunter of exceptional beauty that he died because he was unable to leave a pool after falling in love with his own reflection. That's why I keep myself away from pools these days (kidding).
In mathematics, he has kins by the name of narcissistic numbers - numbers that can't get enough of themselves. In particular, they are numbers that are the sum of their digits when raised to the power of the number of digits.
For example, 371 is a narcissistic number; it has three digits, and if we cube each digits 33 + 73 + 13 the sum is 371. Other 3-digit narcissistic numbers are
153 = 13 + 53 + 33
370 = 33 + 73 + 03
407 = 43 + 03 + 73.
There are also 4-digit narcissistic numbers, some of which are 1634, 8208, 9474 since
1634 = 14+64+34+44
8208 = 84+24+04+84
9474 = 94+44+74+44
It has been proven that there are only 88 narcissistic numbers (in the decimal system) and that the largest of which is
115,132,219,018,763,992,565,095,597,973,971,522,401
has 39 digits.

Ref.: //https://bit.ly/2qNYxo2
Sample Input:
(153)
(370)
(407)
(409)
(1634)
(8208)
(9474)
(9475)
Sample Output:
True
True
True
False
True
True
True
False
"""

def is_narcissistic_num(num):
	return num == sum([int(x) ** len(str(num)) for x in str(num)])

print(is_narcissistic_num(153))
print(is_narcissistic_num(370))
print(is_narcissistic_num(407))
print(is_narcissistic_num(409))
print(is_narcissistic_num(1634))
print(is_narcissistic_num(8208))
print(is_narcissistic_num(9474))
print(is_narcissistic_num(9475))

"""
Write a Python program to find the highest and lowest number from a given string of space-separated integers. Go to the editor
Original string: 1 4 5 77 9 0
Highest and lowest number of the said string: (77, 0)
Original string: -1 -4 -5 -77 -9 0
Highest and lowest number of the said string: (0, -77)
Original string: 0 0
Highest and lowest number of the said string: (0, 0)
"""

def highest_lowest_num(str1):
 num_list = list(map(int, str1.split()))
 return max(num_list), min(num_list)
text = "1 4 5 77 9 0"
print("Original string:", text)
print("Highest and lowest number of the said string:",highest_lowest_num(text))
text = "-1 -4 -5 -77 -9 0"
print("\nOriginal string:", text)
print("Highest and lowest number of the said string:",highest_lowest_num(text))
text = "0 0"
print("\nOriginal string:", text)
print("Highest and lowest number of the said string:",highest_lowest_num(text))


"""
Write a Python program to check whether a sequence of numbers has an increasing trend or not. Go to the editor
Sample Input:
[1,2,3,4]
[1,2,5,3,4]
[-1,-2,-3,-4]
[-4,-3,-2,-1]
[1,2,3,4,0]
Sample Output:
True
False
False
True
False
"""

def increasing_trend(nums):
    if (sorted(nums) == nums):
        return True
    else:
        return False

print(increasing_trend([1,2,3,4]))
print(increasing_trend([1,2,5,3,4]))
print(increasing_trend([-1,-2,-3,-4]))
print(increasing_trend([-4,-3,-2,-1]))
print(increasing_trend([1,2,3,4,0]))


"""
Write a Python program to find the position of the second occurrence of a given string in another given string. If there is no such string return -1. Go to the editor
Sample Input:
("The quick brown fox jumps over the lazy dog", "the")
("the quick brown fox jumps over the lazy dog", "the")
Sample Output:
-1
31
"""

def find_string(txt, str1):
	return txt.find(str1, txt.find(str1)+1)

print(find_string("The quick brown fox jumps over the lazy dog", "the"))
print(find_string("the quick brown fox jumps over the lazy dog", "the"))


"""
Write a Python program to compute the sum of all items in a given array of integers where each integer is multiplied by its index. Return 0 if there is no number.
"""

def sum_index_multiplier(nums):
	return sum(j*i for i, j in enumerate(nums))

print(sum_index_multiplier([1,2,3,4]))
print(sum_index_multiplier([-1,-2,-3,-4]))
print(sum_index_multiplier([]))


"""
Write a Python program to find the name of the oldest student in a given dictionary containing the names and ages of a group of students. Go to the editor
Sample Input:
{"Bernita Ahner": 12, "Kristie Marsico": 11, "Sara Pardee": 14, "Fallon Fabiano": 11, "Nidia Dominique": 15}
{"Nilda Woodside": 12, "Jackelyn Pineda": 12.2, "Sofia Park": 12.4, "Joannie Archibald": 12.6, "Becki Saunder": 12.7}
Sample Output:
Nidia Dominique
Becki Saunder
"""

def oldest_student(students):
	return max(students, key=students.get)

print(oldest_student({"Bernita Ahner": 12, "Kristie Marsico": 11, 
                      "Sara Pardee": 14, "Fallon Fabiano": 11, 
                      "Nidia Dominique": 15})) 
print(oldest_student({"Nilda Woodside": 12, "Jackelyn Pineda": 12.2, 
                      "Sofia Park": 12.4, "Joannie Archibald": 12.6, 
                      "Becki Saunder": 12.7})) 


"""
Write a Python program to create a string with no duplicate consecutive letters from a given string. Go to the editor
Sample Input:
("PPYYYTTHON")
("PPyyythonnn")
("Java")
("PPPHHHPPP")
Sample Output:
PYTHON
Python
Java
PHP
"""

def no_consecutive_letters (txt):
    return txt[0] + ''.join(txt[i] for i in range(1,len(txt)) if txt[i] != txt[i-1])

print(no_consecutive_letters("PPYYYTTHON"))
print(no_consecutive_letters("PPyyythonnn"))
print(no_consecutive_letters("Java"))
print(no_consecutive_letters("PPPHHHPPP")) 


"""
Write a Python program to check whether two given lines are parallel or not. Go to the editor
Note: Parallel lines are two or more lines that never intersect. Parallel Lines are like railroad tracks that never intersect.
The General Form of the equation of a straight line is: ax + by = c
The said straight line is represented in a list as [a, b, c]
Example of two parallel lines:
x + 4y = 10 and x + 4y = 14
Sample Input:
([2,3,4], [2,3,8])
([2,3,4], [4,-3,8])
Sample Output:
True
False
"""

def parallel_lines(line1, line2):
  return line1[0]/line1[1] == line2[0]/line2[1]
#2x + 3y = 4, 2x + 3y = 8
print(parallel_lines([2,3,4], [2,3,8]))
#2x + 3y = 4, 4x - 3y = 8
print(parallel_lines([2,3,4], [4,-3,8])) 


"""
Write a Python program to find a number in a given matrix that is maximum in its column and minimum in its row. Go to the editor
Sample Input:
Original matrix: [[1, 2], [2, 3]]
Number in the said matrix which is maximum in its column and minimum in its row:
[2]
Original matrix: [[1, 2, 3], [3, 4, 5]]
Number in the said matrix which is maximum in its column and minimum in its row:
[3]
Original matrix: [[7, 5, 6], [3, 4, 4], [6, 5, 7]]
Number in the said matrix which is maximum in its column and minimum in its row:
[5]
"""

Number in a Matrix: Maximum in its column and minimum in its row.
def matrix_number(matrix):
   result = set(map(min, matrix)) & set(map(max, zip(*matrix)))
   return list(result)
m1 = [[1,2], [2,3]]
print("Original matrix:",m1)
print("Number in the said matrix which is maximum in its column and minimum in its row:")
print(matrix_number(m1))
m1 = [[1,2,3], [3,4,5]]
print("\nOriginal matrix:",m1)
print("Number in the said matrix which is maximum in its column and minimum in its row:")
print(matrix_number(m1))
m1 = [[7,5,6], [3,4,4], [6,5,7]]
print("\nOriginal matrix:",m1)
print("Number in the said matrix which is maximum in its column and minimum in its row:")
print(matrix_number(m1))


"""
Write a Python program to check whether a given sequence is linear, quadratic or cubic. Go to the editor
Sequences are sets of numbers that are connected in some way.
Linear sequence:
A number pattern which increases or decreases by the same amount each time is called a linear sequence. The amount it increases or decreases by is known as the common difference.
Quadratic sequence:
In quadratic sequence, the difference between each term increases, or decreases, at a constant rate.
Cubic sequence:
Sequences where the 3rd difference are known as cubic sequence.
Sample Output:
Original Sequence: [0, 2, 4, 6, 8, 10]
Check the said sequence is Linear, Quadratic or Cubic?
Linear Sequence
Original Sequence: [1, 4, 9, 16, 25]
Check the said sequence is Linear, Quadratic or Cubic?
Quadratic Sequence
Original Sequence: [0, 12, 10, 0, -12, -20]
Check the said sequence is Linear, Quadratic or Cubic?
Cubic Sequence
Original Sequence: [1, 2, 3, 4, 5]
Check the said sequence is Linear, Quadratic or Cubic?
Linear Sequence
"""

def Seq_Linear_Quadratic_Cubic(seq_nums):
  seq_nums = [seq_nums[x] - seq_nums[x-1] for x in range(1, len(seq_nums))]
  if len(set(seq_nums)) == 1: return "Linear Sequence"
  seq_nums = [seq_nums[x] - seq_nums[x-1] for x in range(1, len(seq_nums))]
  if len(set(seq_nums)) == 1: return "Quadratic Sequence"
  seq_nums = [seq_nums[x] - seq_nums[x-1] for x in range(1, len(seq_nums))]
  if len(set(seq_nums)) == 1: return "Cubic Sequence"

nums = [0,2,4,6,8,10]
print("Original Sequence:",nums)
print("Check the said sequence is Linear, Quadratic or Cubic?")
print(Seq_Linear_Quadratic_Cubic(nums))
nums = [1,4,9,16,25]
print("\nOriginal Sequence:",nums)
print("Check the said sequence is Linear, Quadratic or Cubic?")
print(Seq_Linear_Quadratic_Cubic(nums))
nums = [0,12,10,0,-12,-20]
print("\nOriginal Sequence:",nums)
print("Check the said sequence is Linear, Quadratic or Cubic?")
print(Seq_Linear_Quadratic_Cubic(nums))
nums = [1,2,3,4,5]
print("\nOriginal Sequence:",nums)
print("Check the said sequence is Linear, Quadratic or Cubic?")
print(Seq_Linear_Quadratic_Cubic(nums))


"""
Write a Python program to test whether a given integer is a Pandigital number or not. Go to the editor
From Wikipedia,
In mathematics, a pandigital number is an integer that in a given base has among its significant digits each digit used in the base at least once.
For example,
1223334444555556666667777777888888889999999990 is a pandigital number in base 10.
The first few pandigital base 10 numbers are given by:
1023456789, 1023456798, 1023456879, 1023456897, 1023456978, 1023456987, 1023457689

Sample Output:
Original number: 1023456897 Check the said number is Pandigital number or not? True Original number: 1023456798 Check the said number is Pandigital number or not? True Original number: 1023457689 Check the said number is Pandigital number or not? True Original number: 1023456789 Check the said number is Pandigital number or not? True Original number: 102345679 Check the said number is Pandigital number or not? False
"""

def is_pandigital_num(n):
    return len(set(str(n))) == 10

n = 1023456897
print("Original number:",n)
print("Check the said number is Pandigital number or not?")
print(is_pandigital_num(n))
n = 1023456798
print("Original number:",n)
print("Check the said number is Pandigital number or not?")
print(is_pandigital_num(n))
n = 1023457689
print("Original number:",n)
print("Check the said number is Pandigital number or not?")
print(is_pandigital_num(n))
n = 1023456789
print("Original number:",n)
print("Check the said number is Pandigital number or not?")
print(is_pandigital_num(n))
n = 102345679
print("Original number:",n)
print("Check the said number is Pandigital number or not?")
print(is_pandigital_num(n))


"""
Write a Python program to check whether a given number is odd or even. Go to the editor
A number is called "Oddish" if the sum of all of its digits is odd, and a number is called "Evenish" if the sum of all of its digits is even.
Sample Output:
Original Number 120
Check whether the sum of all digits of the said number is odd or even!
Oddish
Original Number 321
Check whether the sum of all digits of the said number is odd or even!
Evenish
Original Number 43
Check whether the sum of all digits of the said number is odd or even!
Oddish
Original Number 4433
Check whether the sum of all digits of the said number is odd or even!
Evenish
Original Number 373
Check whether the sum of all digits of the said number is odd or even!
Oddish
"""

def oddish_evenish_num(n):
	return 'Oddish' if sum(map(int, str(n))) % 2 else 'Evenish'
n = 120
print("Original Number",n)
print("Check whether the sum of all digits of the said number is odd or even!")
print(oddish_evenish_num(120))
n = 321
print("Original Number",n)
print("Check whether the sum of all digits of the said number is odd or even!")
print(oddish_evenish_num(321))
n = 43 
print("Original Number",n)
print("Check whether the sum of all digits of the said number is odd or even!")
print(oddish_evenish_num(43))
n = 4433
print("Original Number",n)
print("Check whether the sum of all digits of the said number is odd or even!")
print(oddish_evenish_num(4433))
n = 373
print("Original Number",n)
print("Check whether the sum of all digits of the said number is odd or even!")
print(oddish_evenish_num(373))


"""
Write a Python program that takes three integers and checks whether the sum of the last digit of the first number and the last digit of the second number equals the last digit of the third number. Go to the editor
Sample Input:
(12, 26, 44)
(145, 122, 1010)
(0, 20, 40)
(1, 22, 40)
(145, 129, 104)
Sample Output:
True
False
True
False
True
"""

def check_last_digit(x, y, z):
  return str(x+z)[-1] == str(y)[-1]
print(check_last_digit(12, 26, 44))
print(check_last_digit(145, 122, 1010))
print(check_last_digit(0, 20, 40))
print(check_last_digit(1, 22, 40))
print(check_last_digit(145, 129, 104))


"""
Write a Python program to find the indices of all occurrences of a given item in a given list. Go to the editor
Sample Input:
([1,2,3,4,5,2], 2)
([3,1,2,3,4,5,6,3,3], 3)
([1,2,3,-4,5,2,-4], -4)
Sample Output:
Original list of numbers: [1, 2, 3, 4, 5, 2]
Given Number 2
Indices of all occurrences of the said item in the given list:
[1, 5]
Original list of numbers: [3, 1, 2, 3, 4, 5, 6, 3, 3]
Given Number 3
Indices of all occurrences of the said item in the given list:
[0, 3, 7, 8]
Original list of numbers: [1, 2, 3, -4, 5, 2, -4]
Given Number -4
Indices of all occurrences of the said item in the given list:
[3, 6]
Original list of numbers: [1, 2, 3, 4, 5, 2]
Given Number 7
Indices of all occurrences of the said item in the given list:
[]
"""

def indices_in_list(nums_list, n):
           return [idx for idx, i in enumerate(nums_list) if i == n]
nums = [1,2,3,4,5,2]
print("Original list of numbers:",nums)
n = 2
print("Given Number",n)
print("Indices of all occurrences of the said item in the given list:")
print(indices_in_list(nums, n))
nums = [3,1,2,3,4,5,6,3,3]
print("\nOriginal list of numbers:",nums)
n = 3
print("Given Number",n)
print("Indices of all occurrences of the said item in the given list:")
print(indices_in_list(nums, n))
nums = [1,2,3,-4,5,2,-4]
print("\nOriginal list of numbers:",nums)
n = -4
print("Given Number",n)
print("Indices of all occurrences of the said item in the given list:")
print(indices_in_list(nums, n))
nums = [1,2,3,4,5,2]
print("\nOriginal list of numbers:",nums)
n = 7
print("Given Number",n)
print("Indices of all occurrences of the said item in the given list:")
print(indices_in_list(nums, n))


"""
Write a Python program to remove duplicate numbers from a given list of numbers. Go to the editor
Sample Input:
([1,2,3,2,3,4,5])
([1,2,3,2,4,5])
([1,2,3,4,5])
Sample Output:
Original list of numbers: [1, 2, 3, 2, 3, 4, 5]
After removing the duplicate numbers from the said list:
[1, 4, 5]
Original list of numbers: [1, 2, 3, 2, 4, 5]
After removing the duplicate numbers from the said list:
[1, 3, 4, 5]
Original list of numbers: [1, 2, 3, 4, 5]
After removing the duplicate numbers from the said list:
[1, 2, 3, 4, 5]
"""

def unique_nums(nums):
 return [i for i in nums if nums.count(i)==1]
nums = [1,2,3,2,3,4,5]
print("Original list of numbers:",nums)
print("After removing the duplicate numbers from the said list:")
print(unique_nums(nums))
nums = [1,2,3,2,4,5]
print("\nOriginal list of numbers:",nums)
print("After removing the duplicate numbers from the said list:")
print(unique_nums(nums))
nums = [1,2,3,4,5]
print("\nOriginal list of numbers:",nums)
print("After removing the duplicate numbers from the said list:")
print(unique_nums(nums))



"""
111. Write a Python program which checks whether two circles in the same plane (with the same center (x,y) and radius) intersect. If intersection occurs, return true, otherwise return false. Go to the editor
Sample Input:
([1,2, 4], [1,2, 8])
([0,0, 2], [10,10, 5])
Sample Output:
True
False
Click me to see the sample solution
"""
def is_circle_collision(circle1, circle2):
   x1, y1, r1 = circle1
   x2, y2, r2 = circle2
   distance = ((x1-x2)**2 + (y1-y2)**2)**0.5
   return distance <= r1 + r2
print(is_circle_collision([1,2, 4], [1,2, 8]))
print(is_circle_collision([0,0, 2], [10,10, 5]))

"""
112. Write a Python program to compute the digit distance between two integers. Go to the editor
The digit distance between two numbers is the absolute value of the difference of those numbers.
For example, the distance between 3 and -3 on the number line given by the |3 - (-3) | = |3 + 3 | = 6 units
Digit distance of 123 and 256 is
Since |1 - 2| + |2 - 5| + |3 - 6| = 1 + 3 + 3 = 7
Sample Input:
(123, 256)
(23, 56)
(1, 2)
(24232, 45645)
Sample Output:
7
6
1
11
Click me to see the sample solution
"""

def digit_distance_nums(num1: int, num2: int) -> int:
  return(sum(abs(i - j) for i, j in
  zip(map(int, str(num1)), map(int, str(num2)))))
print(digit_distance_nums(509, 510))
print(digit_distance_nums(123, 256))
print(digit_distance_nums(23, 56))
print(digit_distance_nums(1, 2))
print(digit_distance_nums(24232, 45645))

"""
113. Write a Python program to reverse all words of odd lengths. Go to the editor
Sample Input:
("The quick brown fox jumps over the lazy dog")
("Python Exercises")
Sample Output:
The quick brown fox jumps revo the yzal dog
nohtyP Exercises
Click me to see the sample solution
"""
def reverse_even(txt):
         return ' '.join(i[::-1] if not len(i)%2 else i for i in txt.split())
print(reverse_even("The quick brown fox jumps over the lazy dog"))
print(reverse_even("Python Exercises"))

"""
114. Write a Python program to print letters from the English alphabet from a-z and A-Z. Go to the editor
Sample Input:
("Alphabet from a-z:")
("\nAlphabet from A-Z:")
Sample Output:
Alphabet from a-z:
a b c d e f g h i j k l m n o p q r s t u v w x y z
Alphabet from A-Z:
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
Click me to see the sample solution
"""

import string
print("Alphabet from a-z:")
for letter in string.ascii_lowercase:
   print(letter, end =" ")
print("\nAlphabet from A-Z:")
for letter in string.ascii_uppercase:
   print(letter, end =" ")


"""
115. Write a Python program to generate and print a list of numbers from 1 to 10. Go to the editor
Sample Input:
range(1,10)
Sample Output:
[1, 2, 3, 4, 5, 6, 7, 8, 9]
['1', '2', '3', '4', '5', '6', '7', '8', '9']
Click me to see the sample solution
"""
nums = range(1,10)
print(list(nums))
print(list(map(str, nums)))


"""
116. Write a Python program to identify non-prime numbers between 1 and 100 (integers). Print the non-prime numbers. Go to the editor
Sample Input:
range(1, 101)
Sample Output:
Nonprime numbers between 1 to 100:
4
6
8
9
10
..
96
98
99
100
Click me to see the sample solution
"""

import math
def is_not_prime(n):
    ans = False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            ans = True
    return ans
print("Nonprime numbers between 1 to 100:")
for x in filter(is_not_prime, range(1, 101)):
    print(x)


"""
117. Write a Python program to make a request to a web page, and test the status code, and display the HTML code of the specified web page. Go to the editor
Sample Output:
Web page status: <Response [200]>
HTML code of the above web page:
<!doctype html>
<html>
<head>
<title>Example Domain</title>
<meta charset="utf-8" />
<meta http-equiv="Content-type" content="text/html; charset=utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
</head>
<body>
<div>
<h1>Example Domain</h1>
<p>This domain is for use in illustrative examples in documents. You may use this
domain in literature without prior coordination or asking for permission.</p>
<p><a href="https://www.iana.org/domains/example">More information...</a></p>
</div>
</body>
</html>

Click me to see the sample solution
"""

import requests
url = 'http://www.example.com/'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh) Gecko/20100101 Firefox/38.0'}
request = requests.get(url, headers=headers)
print("Web page status: ", request)
print("\nHTML code of the above web page:")
if request.ok:
    print(request.text)

"""
118. In multiprocessing, processes are spawned by creating a Process object. Write a Python program to show the individual process IDs (parent process, process ID etc.) involved. Go to the editor
Sample Output:
Main line
module name: __main__
parent process: 23967
process id: 27986
function f
module name: __main__
parent process: 27986
process id: 27987
hello bob
Click me to see the sample solution
"""

from multiprocessing import Process
import os
def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())
def f(name):
    info('function f')
    print('hello', name)
if __name__ == '__main__':
    info('Main line')
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()

"""
119. Write a Python program to check if two given numbers are Co Prime or not. Return True if two numbers are Co Prime otherwise return false. Go to the editor
Sample Input:
(17, 13)
(17, 21)
(15, 21)
(25, 45)
Sample Output:
True
True
False
False
Click me to see the sample solution

"""
def gcd(p,q):
Create the gcd of two positive integers.
    while q != 0:
        p, q = q, p%q
    return p
def is_coprime(x, y):
    return gcd(x, y) == 1
print(is_coprime(17, 13))
print(is_coprime(17, 21))
print(is_coprime(15, 21))
print(is_coprime(25, 45))


"""
120. Write a Python program to calculate Euclid's totient function for a given integer. Use a primitive method to calculate Euclid's totient function. Go to the editor
Sample Input:
(10)
(15)
(33)
Sample Output:
4
8
20
Click me to see the sample solution
"""
def gcd(p,q):
Create the gcd of two positive integers.
    while q != 0:
        p, q = q, p%q
    return p

def is_coprime(x, y):
    return gcd(x, y) == 1

def phi_func(x):
    if x == 1:
        return 1
    else:
        n = [y for y in range(1,x) if is_coprime(x,y)]
        return len(n)
print(phi_func(10))
print(phi_func(15))
print(phi_func(33))


"""
121. Write a Python program to create a coded string from a given string, using a specified formula. Go to the editor
Replace all 'P' with '9', 'T' with '0', 'S' with '1', 'H' with '6' and 'A' with '8'
Original string: PHP
Coded string: 969
Original string: JAVASCRIPT
Coded string: J8V81CRI90
Click me to see the sample solution"""

def test(str):
	return str.translate(str.maketrans('PTSHA', '90168'))
str = "PHP"
print("Original string: ",str)
print("Coded string: ",test(str))
str = "JAVASCRIPT"
print("\nOriginal string: ",str)
print("Coded string: ",test(str))


"""
122. Write a Python program to check if a given string contains only lowercase or uppercase characters. Go to the editor
Original string: PHP
Coded string: True
Original string: javascript
Coded string: True
Original string: JavaScript
Coded string: False
Click me to see the sample solution"""

def test(str):
    return str.islower() or str.isupper()

str = "PHP"
print("Original string: ",str)
print("Coded string: ",test(str))
str = "javascript"
print("\nOriginal string: ",str)
print("Coded string: ",test(str))
str = "JavaScript"
print("\nOriginal string: ",str)
print("Coded string: ",test(str))


"""123. Write a Python program to remove the first and last elements from a given string. Go to the editor
Original string: PHP
Removing the first and last elements from the said string: H
Original string: Python
Removing the first and last elements from the said string: ytho
Original string: JavaScript
Removing the first and last elements from the said string: avaScrip
Click me to see the sample solution"""

def test(str):
    return str if len(str) < 3 else str[1:-1]
str = "PHP"
print("Original string: ",str)
print("Removing the first and last elements from the said string: ",test(str))
str = "Python"
print("\nOriginal string: ",str)
print("Removing the first and last elements from the said string: ",test(str))
str = "JavaScript"
print("\nOriginal string: ",str)
print("Removing the first and last elements from the said string: ",test(str))


"""124. Write a Python program to check if a given string contains two similar consecutive letters. Go to the editor
Original string: PHP
Check for consecutive similar letters! False
Original string: PHHP
Check for consecutive similar letters! True
Original string: PHPP
Check for consecutive similar letters! True
Click me to see the sample solution"""

def test(str1):
    return any(c1 == c2 for c1, c2 in zip(str1, str1[1:]))
str = "PHP"
print("Original string: ",str)
print("Check for consecutive similar letters! ",test(str))
str = "PHHP"
print("\nOriginal string: ",str)
print("Check for consecutive similar letters! ",test(str))
str = "PHPP"
print("\nOriginal string: ",str)
print("Check for consecutive similar letters! ",test(str))


"""125. Write a Python program to reverse a given string in lower case. Go to the editor
Original string: PHP
Reverse the said string in lower case: php
Original string: JavaScript
Reverse the said string in lower case: tpircsavaj
Original string: PHPP
Reverse the said string in lower case: pphp
Click me to see the sample solution"""

def test(str1):
    return str1[::-1].lower()
str = "PHP"
print("Original string:",str)
print("Reverse the said string in lower case:",test(str))
str = "JavaScript"
print("\nOriginal string:",str)
print("Reverse the said string in lower case:",test(str))
str = "PHPP"
print("\nOriginal string:",str)
print("Reverse the said string in lower case:",test(str)) 


"""126. Write a Python program to convert the letters of a given string (same case-upper/lower) into alphabetical order. Go to the editor
Original string: PHP
Convert the letters of the said string into alphabetical order: HPP
Original string: javascript
Convert the letters of the said string into alphabetical order: aacijprstv
Original string: python
Convert the letters of the said string into alphabetical order: hnopty
Click me to see the sample solution"""

def test(str1):
    return ''.join(sorted(str1))

str1 = "PHP"
print("Original string:",str1)
print("Convert the letters of the said string into alphabetical order:",test(str1))
str1 = "javascript"
print("\nOriginal string:",str1)
print("Convert the letters of the said string into alphabetical order:",test(str1))
str1 = "python"
print("\nOriginal string:",str1)
print("Convert the letters of the said string into alphabetical order:",test(str1)) 


"""127. Write a Python program to check whether the average value of the elements of a given array of numbers is a whole number or not. Go to the editor
Original array:
1 3 5 7 9
Check the average value of the elements of the said array is a whole number or not: True
Original array:
2 4 2 6 4 8
Check the average value of the elements of the said array is a whole number or not:
False
Click me to see the sample solution"""

import array as arr
def test(nums):
    return sum(nums) % len(nums) == 0
array_num = arr.array('i', [1, 3, 5, 7, 9])
print("Original array:")
for i in range(len(array_num)):    
    print(array_num[i], end=' ')
print("\nCheck the average value of the elements of the said array is a whole number or not:\n",test(array_num))
array_num = arr.array('i', [2, 4, 2, 6, 4, 8])
print("\nOriginal array:")
for i in range(len(array_num)):    
    print(array_num[i], end=' ')
print("\nCheck the average value of the elements of the said array is a whole number or not:\n",test(array_num)) 


"""128. Write a Python program to remove all vowels from a given string. Go to the editor
Original string: Python
After removing all the vowels from the said string: Pythn
Original string: C Sharp
After removing all the vowels from the said string: C Shrp
Original string: JavaScript
After removing all the vowels from the said string: JvScrpt
Click me to see the sample solution"""

import re
def test(text):
    return re.sub(r'[aeiou]+', '', text, flags=re.IGNORECASE)
text = "Python";
print("Original string:",text)
print("After removing all the vowels from the said string: " + test(text))
text = "C Sharp"
print("\nOriginal string:",text)
print("After removing all the vowels from the said string: " + test(text))
text = "JavaScript"
print("\nOriginal string:",text)
print("After removing all the vowels from the said string: " + test(text))


"""129. Write a Python program to get the index number of all lower case letters in a given string. Go to the editor
Original string: Python
Indices of all lower case letters of the said string: [1, 2, 3, 4, 5] Original string: JavaScript
Indices of all lower case letters of the said string: [1, 2, 3, 5, 6, 7, 8, 9] Original string: PHP
Indices of all lower case letters of the said string: []
Click me to see the sample solution"""

def test(text):
   return [x for x in range(len(text)) if text[x].islower()]
text = "Python";
print("Original string:",text)
print("Indices of all lower case letters of the said string:\n",test(text))
text = "JavaScript";
print("Original string:",text)
print("Indices of all lower case letters of the said string:\n",test(text))
text = "PHP";
print("Original string:",text)
print("Indices of all lower case letters of the said string:\n",test(text))


"""130. Write a Python program to check whether a given month and year contains a Monday 13th. Go to the editor
Month No.: 11 Year: 2022
Check whether the said month and year contains a Monday 13th.: False
Month No.: 6 Year: 2022
Check whether the said month and year contains a Monday 13th.: True
Click me to see the sample solution"""

from datetime import date
def test(month, year): 
    return str(date(year,month,13).strftime("%A")=='Monday')

month = 11;
year = 2022;            
print("Month No.: ", month, " Year: ", year)
print("Check whether the said month and year contains a Monday 13th.: " + test(month, year))
month = 6;
year = 2022;            
print("\nMonth No.: ", month, " Year: ", year)
print("Check whether the said month and year contains a Monday 13th.: " + test(month, year)) 


"""131. Write a Python program to count the number of zeros and ones in the binary representation of a given integer. Go to the editor
Original number: 12
Number of ones and zeros in the binary representation of the said number: Number of zeros: 2, Number of ones: 2
Original number: 1234
Number of ones and zeros in the binary representation of the said number: Number of zeros: 6, Number of ones: 5
Click me to see the sample solution"""

def test(num):
    ones =  bin(num). replace("0b", "").count('1')
    zeros = bin(num). replace("0b", "").count('0')
    return "Number of zeros: " + str(zeros) + ", Number of ones: " + str(ones)

n = 12; 
print("Original number: ",n)
print("Number of ones and zeros in the binary representation of the said number:")
print(test(n))
n = 1234;
print("\nOriginal number: ",n)
print("Number of ones and zeros in the binary representation of the said number:")
print(test(n))


"""132. Write a Python program to find all the factors of a given natural number. Go to the editor
Factors:
The factors of a number are the numbers that divide into it exactly. The number 12 has six factors:
1, 2, 3, 4, 6 and 12 If 12 is divided by any of the six factors then the answer will be a whole number. For example:
12 / 3 = 4
Original Number: 1
Factors of the said number: {1}
Original Number: 12
Factors of the said number: {1, 2, 3, 4, 6, 12}
Original Number: 100
Factors of the said number: {1, 2, 4, 100, 5, 10, 50, 20, 25}
Click me to see the sample solution"""

#Source https://bit.ly/3w492zp

from functools import reduce

def test(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

'''
sqrt(x) * sqrt(x) = x. So if the two factors are the same, they're both 
the square root. If you make one factor bigger, you have to make the other 
factor smaller. This means that one of the two will always be less than or 
equal to sqrt(x), so you only have to search up to that point to find one 
of the two matching factors. You can then use x / fac1 to get fac2.

The reduce(list.__add__, ...) is taking the little lists of [fac1, fac2] 
and joining them together in one long list.

The [i, n/i] for i in range(1, int(sqrt(n)) + 1) if n % i == 0 returns 
a pair of factors if the remainder when you divide n by the smaller one 
is zero (it doesn't need to check the larger one too; it just gets that 
by dividing n by the smaller one.)

The set(...) on the outside is getting rid of duplicates, which only 
happens for perfect squares. For n = 4, this will return 2 twice, so 
set gets rid of one of them.
'''
n = 1
print("\nOriginal Number:",n)
print("Factors of the said number:",test(n))
n = 12
print("\nOriginal Number:",n)
print("Factors of the said number:",test(n))
n = 100
print("\nOriginal Number:",n)
print("Factors of the said number:",test(n))


"""133. Write a Python program to compute the sum of the negative and positive numbers in an array of integers and display the largest sum. Go to the editor
Original array elements: {0, 15, 16, 17, -14, -13, -12, -11, -10, 18, 19, 20}
Largest sum - Positive/Negative numbers of the said array: 105
Original array elements: {0, 3, 4, 5, 9, -22, -44, -11}
Largest sum - Positive/Negative numbers of the said array: -77
Click me to see the sample solution"""

def test(lst):
  pos_sum = 0
  neg_sum = 0
  for n in lst:
    if n > 0:
      pos_sum += n
    elif n < 0:
      neg_sum += n
  return max(pos_sum, neg_sum, key=abs)

nums = { 0, -10, -11, -12, -13, -14, 15, 16, 17, 18, 19, 20 };
print("Original array elements:")
print(nums)
print("Largest sum - Positive/Negative numbers of the said array: ", test(nums))
nums = { -11, -22, -44, 0, 3, 4 , 5, 9 };
print("\nOriginal array elements:")
print(nums)
print("Largest sum - Positive/Negative numbers of the said array: ", test(nums))


"""134. Write a Python program that alternates the case of each letter in a given string, with the first letter in the string being uppercase. Go to the editor
Original string: Python Exercises
After alternating the case of each letter of the said string: PyThOn ExErCiSeS
Original string: Cis used to develop web apps, desktop apps, mobile apps, games and much more.
After alternating the case of each letter of the said string: CiS uSeD tO dEvElOp WeB aPpS, dEsKtOp ApPs, MoBiLe ApPs, GaMeS aNd MuCh MoRe.
Click me to see the sample solution"""

def test(txt):
    result_str = ""
    s = True
    for i in txt:
        result_str += i.upper() if s else i.lower()
        if i.isalpha():
            s = not s
    return result_str
str1 = "Python Exercises";
print("Original string: ", str1)
print("After alternating the case of each letter of the said string:")
print(test(str1))
str1 = "Cis used to develop web apps, desktop apps, mobile apps, games and much more.";
print("\nOriginal string: ", str1)
print("After alternating the case of each letter of the said string:")
print(test(str1))  


"""135. Write a Python program that calculates the Least Common Multiple (LCM) of more than two numbers. The numbers should be taken from a given list of positive integers. Go to the editor
From Wikipedia,
In arithmetic and number theory, the least common multiple, lowest common multiple, or smallest common multiple of two integers a and b, usually denoted by lcm(a, b), is the smallest positive integer that is divisible by both a and b. Since division of integers by zero is undefined, this definition has meaning only if a and b are both different from zero. However, some authors define lcm(a,0) as 0 for all a, which is the result of taking the lcm to be the least upper bound in the lattice of divisibility.
Original list elements: [4, 6, 8]
LCM of the numbers of the said array of positive integers: 24
Original list elements: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
LCM of the numbers of the said array of positive integers: 2520
Original list elements: [48, 72, 108]
LCM of the numbers of the said array of positive integers: 432
Click me to see the sample solution"""

from functools import reduce
def test(nums):
    return reduce(lambda x,y:lcm(x,y),nums)
def gcd(a, b):
    while b:
        a, b = b, a%b
    return a
def lcm(a, b):
    return a*b // gcd(a, b)
nums = [ 4, 6, 8 ]
print("Original list elements:")
print(nums)
print("LCM of the numbers of the said array of positive integers: ", test(nums))
nums = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
print("\nOriginal list elements:")
print(nums)
print("LCM of the numbers of the said array of positive integers: ", test(nums))
nums = [ 48, 72, 108  ]
print("\nOriginal list elements:")
print(nums)
print("LCM of the numbers of the said array of positive integers: ", test(nums))


"""136. Write a Python program to reverse all words of odd lengths. Go to the editor
Original string: The quick brown fox jumps over the lazy dog
Reverse all the words of the said string which have odd length: ehT kciuq nworb xof spmuj over eht lazy god
Original string: Python Exercises
Reverse all the words of the said string which have odd length: Python sesicrexE
Click me to see the sample solution"""

def test(txt):
	return ' '.join(i[::-1] if len(i)%2 else i for i in txt.split())
 
text = "The quick brown fox jumps over the lazy dog"
print("Original string:")
print(text)
print("Reverse all the words of the said string which have odd length:")
print(test(text))
text = "Python Exercises"
print("\nOriginal string:")
print(text)
print("Reverse all the words of the said string which have odd length:")
print(test(text))


"""137. Write a Python program to find the longest common ending between two given strings. Go to the editor
Original strings: running ruminating
Common ending between said two strings: ing
Original strings: thisisatest testing123testing
Common ending between said two strings:
Click me to see the sample solution"""

def test(str1, str2):
    for i in range(len(str2)):
        while str2[i:] in str1 and str2[-1]==str1[-1]:
            return str2[i:]
    return ""

str1 = "running";
str2 = "ruminating";
print("Original strings: " + str1 + "  " + str2)
print("Common ending between said two strings: " + test(str1, str2))
str1 = "thisisatest";
str2 = "testing123testing";
print("\nOriginal strings: " + str1 + "  " + str2)
print("Common ending between said two strings: " + test(str1, str2))


"""138. Write a Python program to reverse the binary representation of a given number and convert the reversed binary number into an integer. Go to the editor
Original number: 13
Reverse the binary representation of the said integer and convert it into an integer: 11
Original number: 145
Reverse the binary representation of the said integer and convert it into an integer: 137
Original number: 1342
Reverse the binary representation of the said integer and convert it into an integer: 997
Click me to see the sample solution"""

def test(n):
    return int(bin(n)[::-1][:-2], 2)

n = 13
print("Original number: ", n)
print("Reverse the binary representation of the said integer and convert it into an integer:\n",test(n))
n = 145
print("Original number: ", n)
print("Reverse the binary representation of the said integer and convert it into an integer:\n",test(n))
n = 1342
print("Original number: ", n)
print("Reverse the binary representation of the said integer and convert it into an integer:\n",test(n))


"""139. Write a Python program to find the closest palindrome number to a given integer. If there are two palindrome numbers in absolute distance return the smaller number. Go to the editor
Original number: 120
Closest Palindrome number of the said number: 121
Original number: 321
Closest Palindrome number of the said number: 323
Original number: 43
Closest Palindrome number of the said number: 44
Original number: 1234
Closest Palindrome number of the said number: 1221
Click me to see the sample solution"""

def test(n):
    x = n
    y = n
    while True:
        if str(x) == str(x)[::-1]:
            return x
        x -=  1
        if str(y) == str(y)[::-1]:
            return y
        y += 1
    return int(bin(n)[::-1][:-2], 2)

n = 120;
print("Original number: ", n)
print("Closest Palindrome number of the said number: ",test(n))
n = 321;
print("Original number: ", n)
print("Closest Palindrome number of the said number: ",test(n))
n = 43;
print("Original number: ", n)
print("Closest Palindrome number of the said number: ",test(n))
n = 1234;
print("Original number: ", n)
print("Closest Palindrome number of the said number: ",test(n))


"""140. Write a Python program to convert all items in a given list to float values. Go to the editor
Original list:
['0.49', '0.54', '0.54', '0.54', '0.54', '0.54', '0.55', '0.54', '0.54', '0.54', '0.55', '0.55', '0.55', '0.54', '0.55', '0.55', '0.54', '0.55', '0.55', '0.54']
List of Floats:
[0.49, 0.54, 0.54, 0.54, 0.54, 0.54, 0.55, 0.54, 0.54, 0.54, 0.55, 0.55, 0.55, 0.54, 0.55, 0.55, 0.54, 0.55, 0.55, 0.54]
Click me to see the sample solution"""

nums = ['0.49', '0.54', '0.54', '0.54', '0.54', '0.54', '0.55', '0.54', '0.54',  '0.54', 
 '0.55', '0.55', '0.55', '0.54', '0.55', '0.55', '0.54', '0.55', '0.55', '0.54']
print("Original list:")
print(nums)
print("\nList of Floats:")
nums_of_floats = []
for item in nums:
    nums_of_floats.append(float(item))
print(nums_of_floats)


"""141. Write a Python program to get the domain name using PTR DNS records from a given IP address. Go to the editor
Domain name using PTR DNS:
dns.google
ec2-13-251-106-90.ap-southeast-1.compute.amazonaws.com
dns.google
ec2-23-23-212-126.compute-1.amazonaws.com
Click me to see the sample solution"""

def get_domain_name(ip_address):
  import socket
  result=socket.gethostbyaddr(ip_address)
  return list(result)[0]
print("Domain name using PTR DNS:")
print(get_domain_name("8.8.8.8"))
print(get_domain_name("13.251.106.90"))
print(get_domain_name("8.8.4.4"))
print(get_domain_name("23.23.212.126"))


"""142. Write a Python program to check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones of the same length in a given string. Return True/False. Go to the editor
Original sequence: 001011
Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:
False
Original sequence: 01010101
Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:
True
Original sequence: 00
Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:
False
Original sequence: 000111000111
Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:
True
Original sequence: 00011100011
Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:
False
Original sequence: 0011101
Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:
False"
Click me to see the sample solution"""

import re
def test(txt):
    return [len(i) for i in re.findall('0+',txt)]==[len(i) for i in re.findall('1+',txt)]
str1 = "001011"
print("\nOriginal sequence:",str1)
print("Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:")
print(test(str1))
str1 = "01010101"
print("\nOriginal sequence:",str1)
print("Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:")
print(test(str1))
str1 = "00"
print("\nOriginal sequence:",str1)
print("Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:")
print(test(str1))
str1 = "000111000111"
print("\nOriginal sequence:",str1)
print("Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:")
print(test(str1))
str1 = "00011100011"
print("\nOriginal sequence:",str1)
print("Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:")
print(test(str1))
str1 = "0011101"
print("\nOriginal sequence:",str1)
print("Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:")
print(test(str1))

"""143. Write a Python program to print Emojis using Unicode characters or CLDR (Common Locale Data Repository) short names. Go to the editor


Click me to see the sample solution"""

print("Smiling face with heart-eyes:")
print("\U0001F60D")
print("Unamused face:")
print("\U0001F612")
print("Beaming face with smiling eyes:")
print("\U0001F601")
print("Grinning face with sweat:")
print("\U0001F605")
print("Face with tears of joy:")
print("\U0001F602")
print("Slightly smiling face:")
print("\U0001F642")
print("Smiling face with halo:")
print("\U0001F607")
print("Zipper-mouth face:")
print("\U0001F910")
print("Grinning face:")
print("\U0001F600")
print("Rolling on the floor laughing:")
print("\U0001F923")



"""144. Write a Python program to convert integer to string. Go to the editor
Sample Input:
language = "Python"
version = 3.6
sample Output:
Language: Python, Version: 3.6
Click me to see the sample solution"""

language = "Python"
version = 3.6
print('Language: ' + language + ',' + ' Version: ' + str(version))

"""145. Write a Python program to find the largest and smallest digits of a given number. Go to the editor
Original Number: 9387422
Largest Digit of the said number: 9
Smallest Digit of the said number: 2
Original Number: 500
Largest Digit of the said number: 5
Smallest Digit of the said number: 0
Original Number: 231548
Largest Digit of the said number: 8
Smallest Digit of the said number: 1
Click me to see the sample solution"""

def Largest_Smallest_digit(n):
   largest_digit = 0
   smallest_digit = 9
   while (n):
       digit = n % 10
       largest digit
       largest_digit = max(digit, largest_digit)
       smallest digit
       smallest_digit = min(digit, smallest_digit)
       n = n // 10
   return largest_digit, smallest_digit
n = 9387422
print("Original Number:", n)
result = Largest_Smallest_digit(n)
print("Largest Digit of the said number:", result[0])
print("Smallest Digit of the said number:", result[1])
n = 500
print("\nOriginal Number:", n)
result = Largest_Smallest_digit(n)
print("Largest Digit of the said number:", result[0])
print("Smallest Digit of the said number:", result[1])
n = 231548
print("\nOriginal Number:", n)
result = Largest_Smallest_digit(n)
print("Largest Digit of the said number:", result[0])
print("Smallest Digit of the said number:", result[1])


"""146. A Python list contains two positive integers. Write a Python program to check whether the cube root of the first number is equal to the square root of the second number. Go to the editor
Sample Data:
([8, 4]) -> True
([64, 16]) -> True
([64, 36]) -> False
Click me to see the sample solution"""

def test(nums):
    x = nums[0]
    y = nums[1]
    t = y**0.5
    if(x == t*t*t):
        return True
    else:
        return False         
nums = [8, 4]
print("Original list of positive numbers:")
print(nums)
print(test(nums))
print("Check square root and cube root of the said numbers:")
nums = [64, 16]
print("Original list of positive numbers:")
print(nums)
print("Check square root and cube root of the said numbers:")
print(test(nums))
nums = [64, 36]
print("Original list of positive numbers:")
print(nums)
print("Check square root and cube root of the said numbers:")
print(test(nums)) 


"""147. A Python list contains three positive integers. Write a Python program to check whether the sum of the digits in each number is equal or not. Return true otherwise false. Go to the editor
Sample Data:
([13, 4, 22]) -> True
([-13, 4, 22]) -> False
([45, 63, 90]) -> True
Click me to see the sample solution"""

def test(nums):
    return nums[0] % 9 == nums[1] % 9 == nums[2] % 9 

nums = [13, 4, 22]
print("Original list of numbers:", nums)
print("Check sum of the digits in each number of the said list is equal or not!")
print(test(nums))
nums = [-13, 4, 22]
print("Original list of numbers:", nums)
print("Check sum of the digits in each number of the said list is equal or not!")
print(test(nums))
nums = [45, 63, 90]
print("Original list of numbers:", nums)
print("Check sum of the digits in each number of the said list is equal or not!")
print(test(nums))


"""148. A Python list contains some positive integers. Write a Python program to count the numbers that are greater than the previous number on the list.Go to the editor
Sample Data:
([1, 4, 7, 9, 11, 5]) -> 4
([1, 3, 3, 2, 2]) -> 1
([4, 3, 2, 1]) -> 0
Click me to see the sample solution"""

def test(nums):
    ctr = 0
    for i in range(1,len(nums)):
        if nums[i] > nums[i-1]:
            ctr += 1
    return ctr

nums = [1, 4, 7, 9, 11, 5]
print("Original list of numbers:", nums)
print("Count the numbers of the said list that are greater than the previous number!")
print(test(nums))
nums = [1, 3, 3, 2, 2]
print("Original list of numbers:", nums)
print("Count the numbers of the said list that are greater than the previous number!")
print(test(nums))
nums = [4, 3, 2, 1]
print("Original list of numbers:", nums)
print("Count the numbers of the said list that are greater than the previous number!")
print(test(nums))


"""149. Write a Python program that takes a positive integer and creates an N x N square filled with the integer N. Display the N x N square. Go to the editor
Sample Data:
(2) -> [[2, 2], [2, 2]]
(5) -> [[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]]
(-6) -> []
Click me to see the sample solution"""

def test(N):
    result = []
    for i in range(N):
        result.append([N]*N)
    return result

N = int(input("Input an integer : "))
print(test(N))

"""150. Write a Python program that takes a positive integer and calculates the cube root of the number until the number is less than three. Count the number of steps to complete the task. Go to the editor
Sample Data:
(3) -> 1
(39) -> 2
(10000) -> 2
Click me to see the sample solution"""

def test(n):
	ctr = 0
	while n >= 3:
	    n =  n ** (1./3.)
	    ctr = ctr + 1    
    return 'Not a positive number!' if n < 0 else ctr

n= int(input("Input a positive integer:"))
print(test(n))



