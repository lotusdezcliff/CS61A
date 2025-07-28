def reverse_link(lnk):
    """
    Given a linked list lnk, return a new linked list which has all the
    elements of lnk but in reverse order.
    
    >>> s = Link(1, Link(2, Link(3, Link.empty)))
    >>> reverse_link(s)
    Link(3, Link(2, Link(1)))
    >>> s
    Link(1, Link(2, Link(3)))
    >>> k = Link(3, Link(5, Link(7, Link(9))))
    >>> reverse_link(k)
    Link(9, Link(7, Link(5, Link(3))))
    >>> k
    Link(3, Link(5, Link(7, Link(9))))
    """
    "*** YOUR CODE HERE ***"
# go all the way to the very bottom of the list, then hit the base case go back, while go back put all the node back to a new linked list.
    def append_to_end(lnk, val):
        if lnk.rest is Link.empty:
            lnk.rest = Link(val)
        else:
            append_to_end(lnk.rest, val)
        return lnk

    if lnk is Link.empty:
        return Link.empty
    if lnk.rest is Link.empty:
        return Link(lnk.first)
    else:
        return append_to_end(reverse_link(lnk.rest), lnk.first)



class Link:
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'
