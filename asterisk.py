print(5 * 7)# Multiplication
print(2 ** 4)# Power operations(exponents)
zeros = [0, 1] * 10# Repeat elements in a list x times
print(zeros)
zeros = (0, 1) * 10# Also works with tuples and strings
print(zeros)
zeros = "ABC" * 10
print(zeros)

def foo(a,b,c, *args, **kwargs):# 1 asterisk for positional arguments, 2 asterisks for keyword arguments
    print(a,b,c)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key)
foo(1,2,3,4,5,6,7,8,nine=9, ten=10)
def func(a, b, *, c):# Also works for enforcing keyword arguments after the asterisk
    print(a,b,c)
func(1,2,c=3)

def unpack(a,b,c):# Unpacking a list into the arguments of a function
    print(a,b,c)
my_list = [0,1,2]# How many elements in the list must be the same as how many parameters are in the list
foo(*my_list)# Use one star for lists

def unpack(a,b,c):# Unpacking a list into the arguments of a function
    print(a,b,c)
my_dict = {'a' : 1, 'b' : 2, 'c' : 3}# You need to use the parameter names as keys while the values are what you would like to pass into the function.
# Number of elements must match number of parameters
foo(**my_dict)# Use two stars for dictionaries

numbers = [1, 2, 3, 4, 5, 6]# Unpacking multiple items in a list
# If you use a tuple, it will work but it will still look like a list
*beginning, last = numbers# Where you put the asterisk is where the list that is chopped off goes
print(beginning)
print(last)

beginning, *last = numbers
print(beginning)
print(last)

beginning, *middle, last = numbers
print(beginning)
print(middle)
print(last)

mytuple = (1,2,3)# Merging a list with an iterable
mylist = [4, 5, 6]# Works with lists, tuples, and sets
new_list = [*mytuple, *mylist]
print(new_list)

dict_a = {'a' : 1, 'b' : 2}# Merging multiple dictionaries to one dictionary
dict_b = {'c' : 3, 'd' : 4}
my_dict = {**dict_a, **dict_b}
print(my_dict)