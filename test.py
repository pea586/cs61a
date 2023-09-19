"""
Environments for Higher-order Func
"""


def apply_twice(f, x):
    return f(f(x))


# def square(x):
#     return x ** 2


def add(a, b, c):
    return a + b + c


def currying_add(func):
    def wrapper(a, c, b=666):
        return func(a, b, c)

    return wrapper


# result = currying_add(add)(1, 2)
# print(result)

from operator import add, mul

square = lambda x: x * x

identity = lambda x: x

triple = lambda x: 3 * x

increment = lambda x: x + 1


def product(n, term):
    start = 1
    ans = 1
    while start <= n:
        ans *= term(start)
        start += 1
    return ans


def accumulate(merger, start, n, term):
    step = 1
    while step <= n:
        curr = merger(start, term(step))
        start = curr
        step += 1
    return start


def product_using_accumulate(n, term):
    return product(n, term)


ans = product_using_accumulate(6, triple)
print(ans)