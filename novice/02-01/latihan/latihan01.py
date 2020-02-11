#Using functions as first class objects means to use them in the same manner that you use data
print(list(map(int, ["1", "2", "3"])))

#You can assign them to variables and return them
def hello_world(h):
    def world(w):
        print(h,w)
    return world
h=hello_world
x=h("hello")
print(x)
print(x("world"))

#You can store functions in various data structures
function_list = [h, x]

# If you take this idea and apply it to the sequential execution of functions, you get the following construct.
def func1():
    pass

def func2():
    pass

def func3():
    pass

executing = lambda f: f()
print(map(executing, [func1, func2, func3]))

# Let us go through a small example where you try to refactor procedural code into functional.

starting_number = 96
square = starting_number ** 2
increment = square + 1
cube = increment ** 3
decrement = cube - 1
result = print(decrement)

# The same procedural code can be written functionally. Note that unlike the code above instead of giving explicit instructions on how to do it, you are giving instructions on what to do. The functions below operate at a higher plane of abstraction.

from functools import reduce
def call(x, f):
    return f(x)
square = lambda x : x*x
increment = lambda x : x+1
cube = lambda x : x*x*x
decrement = lambda x : x-1
funcs = [square, increment, cube, decrement]    

print(reduce(call, funcs, 96))