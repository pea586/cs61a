"""
it is usually good to use short name wisely
n,k,i -> integers
x,y,z -> real numbers
f,g,h -> functions
"""
import collections


def trace1(fn):
    def traced(x):
        print('Calling', fn, 'on argument', x)
        return fn(x)

    return traced


@trace1
def square(x):
    return x * x


@trace1
def triple(x):
    return x * 3


# print(triple(5))

def increment(x):
    return x + 1


def double(x):
    return double(x + x)


first = double


def double(y):
    return y + y


result = first(10)
print(result)  # 40
