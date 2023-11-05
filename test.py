"""
it is usually good to use short name wisely
n,k,i -> integers
x,y,z -> real numbers
f,g,h -> functions
"""
import collections


# def test(colors: str):
#     if len(colors) < 3:
#         return False
#     a, b = 'AAA', 'BBB'
#     cnt1, cnt2 = 0, 0
#     for i in range(len(colors) - 2):
#         cur = colors[i:i+3]
#         if cur == a:
#             cnt1 += 1
#         elif cur == b:
#             cnt2 += 1
#     return cnt1 > cnt2

def num_eights(pos):
    if pos == 0:
        return 0
    return 1 * (pos % 10 == 8) + num_eights(pos // 10)


class LinkedList:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


# a = LinkedList(1, b)
# b = LinkedList(2, c)
c = LinkedList()
d = LinkedList()
e = LinkedList()
f = LinkedList()
g = LinkedList()
h = LinkedList()
i = LinkedList()
j = LinkedList()
k = LinkedList()


