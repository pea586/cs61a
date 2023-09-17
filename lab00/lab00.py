def twenty_twenty_two(a):
    """Come up with the most creative expression that evaluates to 2022,
    using only numbers and the +, *, and - operators.

    >>> ans = twenty_twenty_two(12)
    >>> ans
    1
    >>> ans = twenty_twenty_two(9)
    >>> ans
    1
    >>> ans = twenty_twenty_two(80)
    >>> 10
    """
    return a // 7

def abs_value(a):
    """Return absolute value of a"""
    if a > 0:
        return a
    elif a < 0:
        return -a
    else:
        return a

