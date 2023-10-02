"""
it is usually good to use short name wisely
n,k,i -> integers
x,y,z -> real numbers
f,g,h -> functions
"""
import collections


def split(num):
    return num // 10, num % 10


def merge(m, n):
    s = ''
    if m == 0 or n == 0:
        return str(m+n) + s
    else:
        m1,n1 = m%10,n%10
        if m1 < n1:
            return merge(m//10,n) + str(m1) + s
        else:
            return merge(m,n//10) + str(n1) + s



print(merge(31, 42))
