#1
count = 0
def bump():
    global count
    count += 1
def value():
    return count

#2
def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

#3
x = 'global'
def outer():
    x = 'enclosing'
    def inner():
        x = 'local'
        print(x)
    inner()
    print(x)
outer()
print(x)

#4
_list = [1, 2, 3] 
print(list(range(5)))

#7
from datetime import datetime as dt
print(dt.now())

#8
def pablic_names(module):
    return [name for name in dir(module) if not name.startswith('_')]

#9
def add_item(item, bag=[]): 
    bag.append(item) 
    return bag
print(add_item('apple'))
print(add_item('banana'))

