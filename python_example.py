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


#####This New Line#####


"Mehul"