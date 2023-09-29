"""
it is usually good to use short name wisely
n,k,i -> integers
x,y,z -> real numbers
f,g,h -> functions
"""

a = lambda x: x * 2 + 1


def b(b, x):
    return b(x + a(x))


x = 3
x = b(a, x)
