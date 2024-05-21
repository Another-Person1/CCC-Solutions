def print_name(name):
    print(name)

print_name("Alex")

def unpack(a, b, c, *args):
    print(a,b,c, *args)
mydict = {'a':1, 'b':2, 'c':3}

def foo(a_list):
    a_list = [200,300,400]
    a_list.append(4)
    a_list[0] = -100

mylist=[1,2,3]
foo(mylist)
print(mylist)

