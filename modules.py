# Module is nothing but a python file having some classes and functions inside
# Module can also be code written by someelse and we can use them by installing in our code
# We can also create our own Modules and then allow others to use them


import math

print(int(math.pow(16, 2)))

# print(help(math))

# print(dir(math))

print(math.ceil(2.3))

print(math.floor(2.3))

print(math.log(100))

print(math.log10(100))






import calendar

cal = calendar.month(2016, 1)    # month function shows the whole calender

# print(help(calendar.month))

print(cal)

print(calendar.isleap(2016))    # true if leap otherwise false

print(calendar.isleap(2019))    # true if leap otherwise false

# print(help(calendar.isleap))






# import inspect

# string = inspect.getsource(calendar.isleap)

# print(string)






# --------------------- Now I will be importing my own functions that I have created in functions.py file -------------------------

# import inspect

# from functions import sum, cal_total

# sum(4,5)

# print(inspect.getsource(cal_total))







# import sys

# sys.path.append("C://Users/sajja/Documents")    # this is how we can add our file directory to path and then import the file when required

# import functions

# functions.cal_total([1,2,5])