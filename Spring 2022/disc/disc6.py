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

# Q3: Maximum Path Sum
# Write a function that takes in a tree and returns the maximum sum of the values along any path in the tree. Recall that a path is from the tree's root to any leaf.
def max_path_sum(t):
    """Return the maximum path sum of the tree.

    >>> t = Tree(1, [Tree(5, [Tree(1), Tree(3)]), Tree(10)])
    >>> max_path_sum(t)
    11
    """
    "*** YOUR CODE HERE ***"
    if not t.branches:
          return t.label
    else:
         return max(max_path_sum(b) for b in t.branches) + t.label
    
# Q4: Find Path
'''
Write a function that takes in a tree and a value x and returns a list containing the nodes along the path required to get from the root of the tree to a node containing x.

If x is not present in the tree, return None. Assume that the entries of the tree are unique.

For the following tree, find_path(t, 5) should return [2, 7, 6, 5]
'''
def find_path(t, x):
    """
    >>> t = Tree(2, [Tree(7, [Tree(3), Tree(6, [Tree(5), Tree(11)])]), Tree(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 10)  # returns None
    """
    if t.label == x:
        return [t.label]
    for b in t.branches:
          subpath = find_path(b, x)
          if subpath is not None:
               return [t.label] + subpath
     
    return None

          

# Q5: Prune Small
# Complete the function prune_small that takes in a Tree t and a number n and prunes t mutatively. If t or any of its branches has more than n branches, the n branches with the smallest labels should be kept and any other branches should be pruned, or removed, from the tree.
def prune_small(t, n):
    """Prune the tree mutatively, keeping only the n branches
    of each node with the smallest label.

    >>> t1 = Tree(6)
    >>> prune_small(t1, 2)
    >>> t1
    Tree(6)
    >>> t2 = Tree(6, [Tree(3), Tree(4)])
    >>> prune_small(t2, 1)
    >>> t2
    Tree(6, [Tree(3)])
    >>> t3 = Tree(6, [Tree(1), Tree(3, [Tree(1), Tree(2), Tree(3)]), Tree(5, [Tree(3), Tree(4)])])
    >>> prune_small(t3, 2)
    >>> t3
    Tree(6, [Tree(1), Tree(3, [Tree(1), Tree(2)])])
    """
    while ___________________________:
        largest = max(_______________, key=____________________)
        _________________________
    for __ in _____________:
        ___________________
