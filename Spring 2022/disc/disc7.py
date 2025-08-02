# Q1: WWPD: Linked Lists
'''
>>> link = Link(1, Link(2, Link(3)))
>>> link.first
1
>>> link.rest.first
2
>>> link.rest.rest.rest is Link.empty
True
>>> link.rest = link.rest.rest
>>> link.rest.first
3
>>> link = Link(1)
>>> link.rest = link
>>> link.rest.rest.rest.rest.first
1
>>> link = Link(2, Link(3, Link(4)))
>>> link2 = Link(1, link)
>>> link2.first
1
>>> link2.rest.first
2
'''

# Q2: Remove All
def remove_all(link, value):
    """Remove all the nodes containing value in link. Assume that the
    first element is never removed.

    >>> l1 = Link(0, Link(2, Link(2, Link(3, Link(1, Link(2, Link(3)))))))
    >>> print(l1)
    <0 2 2 3 1 2 3>
    >>> remove_all(l1, 2)
    >>> print(l1)
    <0 3 1 3>
    >>> remove_all(l1, 3)
    >>> print(l1)
    <0 1>
    >>> remove_all(l1, 3)
    >>> print(l1)
    <0 1>
    """
    "*** YOUR CODE HERE ***"
    if link.rest is not None:
        if link.rest.first == value:
            link.rest = link.rest.rest
            remove_all(link, value)
        else:
            remove_all(link.rest, value)
    
# Q3: WWPD: Iterators
'''
>>> s = [[1, 2, 3, 4]]
>>> i = iter(s)
>>> j = iter(next(i))
>>> next(j)
1
>>> s.append(5)
>>> next(i)
5
>>> next(j)
2
>>> list(j)
[3, 4]
>>> next(i)
StopIteration
'''

# Q4: Filter-Iter
def filter_iter(iterable, f):
    """
    >>> is_even = lambda x: x % 2 == 0
    >>> list(filter_iter(range(5), is_even)) # a list of the values yielded from the call to filter_iter
    [0, 2, 4]
    >>> all_odd = (2*y-1 for y in range(5))
    >>> list(filter_iter(all_odd, is_even))
    []
    >>> naturals = (n for n in range(1, 100))
    >>> s = filter_iter(naturals, is_even)
    >>> next(s)
    2
    >>> next(s)
    4
    """
    "*** YOUR CODE HERE ***"
    for i in iterable:
        if f(i):
            yield i

# Q5: Infinite Hailstone
def hailstone(n):
    """Yields the elements of the hailstone sequence starting at n.
       At the end of the sequence, yield 1 infinitely.

    >>> hail_gen = hailstone(10)
    >>> [next(hail_gen) for _ in range(10)]
    [10, 5, 16, 8, 4, 2, 1, 1, 1, 1]
    >>> next(hail_gen)
    1
    """
    "*** YOUR CODE HERE ***"
    while n > 1:
        yield n
        n =  (lambda x: x // 2 if x % 2 == 0 else 3 * x + 1)(n)
    while True:
        yield 1

# Q6: Primes Generator
def is_prime(n):
    """Returns True if n is a prime number and False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    def helper(i):
        if i > (n ** 0.5): # Could replace with i == n
            return True
        elif n % i == 0:
            return False
        return helper(i + 1)
    return helper(2)

def primes_gen(n):
    """Generates primes in decreasing order.
    >>> pg = primes_gen(7)
    >>> list(pg)
    [7, 5, 3, 2]
    """
    if n < 2:
        return 
    if is_prime(n):
        yield n
    yield from primes_gen(n - 1)


    