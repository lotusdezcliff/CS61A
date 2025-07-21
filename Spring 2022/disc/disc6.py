# Q1: WWPD: Repr-esentation
# Note: This is not the typical way repr is used, nor is this way of writing repr recommended, this problem is mainly just to make sure you understand how repr and str work.
class A:
    def __init__(self, x):
        self.x = x

    def __repr__(self):
         return self.x

    def __str__(self):
         return self.x * 2

class B:
    def __init__(self):
         print('boo!')
         self.a = []

    def add_a(self, a):
         self.a.append(a)

    def __repr__(self):
         print(len(self.a))
         ret = ''
         for a in self.a:
             ret += str(a)
         return ret
'''
>>> A('one')
'one'
>>> print(A('one'))
oneone
>>> repr(A('two'))
'two'
>>> b = B()
'boo!'
>>> b.add_a(A('a'))
>>> b.add_a(A('b'))
>>> b
2
'ab'
'''

# Q2: Height
# Write a function that returns the height of a tree. Recall that the height of a tree is the length of the longest path from the root to a leaf.
def height(t):
    """Return the height of a tree.

    >>> t = Tree(3, [Tree(5, [Tree(1)]), Tree(2)])
    >>> height(t)
    2
    >>> t = Tree(3, [Tree(1), Tree(2, [Tree(5, [Tree(6)]), Tree(1)])])
    >>> height(t)
    3
    """
    "*** YOUR CODE HERE ***"
    if not t.branches:
         return 1
    else:
         return (max(height(b) for b in t.branches)) + 1


