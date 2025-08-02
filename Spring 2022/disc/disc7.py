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
        if link.first == value:
            link.rest = link.rest.rest
            remove_all(link, value)
        else:
            remove_all(link.rest, value)
    