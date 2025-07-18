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

>>> A('one')

>>> print(A('one'))

>>> repr(A('two'))

>>> b = B()

>>> b.add_a(A('a'))
>>> b.add_a(A('b'))
>>> b