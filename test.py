"""
Generalization
"""
from math import pi, sqrt


# def area_constant(r, shape_cons):
#     assert r > 0, 'r MUST be a positive'
#     return r * r * shape_cons
#
#
# def area_square(r):
#     return area_constant(r, 1)
#
#
# def area_circle(r):
#     return area_constant(r, pi)
#
#
# def area_hexagon(r):
#     return area_constant(r, 3 * sqrt(3) / 2)
#
# def identity(k):
#     return k
#
#
# def cube(k):
#     return pow(k, 3)
#
#
# def summaration(n, term):
#     """ Sum the first n terms of numbers"""
#     total, k = 0, 1
#     while k <= n:
#         total, k = total + term(k), k + 1
#     return total
#
#
# def sum_natural(n):
#     """
#     sum the first n numbers
#     """
#     return summaration(n, identity)
#
#
# def sum_cube(n):
#     """
#     sum of the first n cube numbers
#
#     """
#     return summaration(n, cube)
#
#
# aa = summaration(5, cube)
# print(aa)
# print(1 + 1)


def make_adder(n):
    """
    Return a function that takes another parameter k and return k+n
    >>> add_three = make_adder(3)
    >>>make_adder(4)
    7
    """

    def adder(k):
        return k + n

    return adder

def square(x):
    print("here!")
    return x * x

def so_slow(num):
    x = num
    while x > 0:
        x = x + 1
    return x / 0

square(so_slow(5))