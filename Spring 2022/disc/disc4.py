def count_stair_ways(n):
    """Returns the number of ways to climb up a flight of
    n stairs, moving either 1 step or 2 steps at a time.
    >>> count_stair_ways(4)
    5
    """
    "*** YOUR CODE HERE ***"
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        return count_stair_ways(n - 1) + count_stair_ways(n - 2)

def count_k(n, k):
    """ Counts the number of paths up a flight of n stairs
    when taking up to and including k steps at a time.
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # Only one step at a time
    1
    """
    "*** YOUR CODE HERE ***"
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        return sum(count_k(n - m, k) for m in range(1, k + 1))
    
# What would Python display?

# >>> a = [1, 5, 4, [2, 3], 3]
# >>> print(a[0], a[-1])
# (1, 3)
# >>> len(a)
# 5
# >>> 2 in a
# False
# >>> a[3][0]
# 2

# Q4: Even weighted
# Write a function that takes a list s and returns a new list that keeps only the even-indexed elements of s and multiplies them by their corresponding index.
def even_weighted(s):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    return [s[x] * x for x in range(len(s)) if x % 2 == 0]

# Q5: Max Product
# Write a function that takes in a list and returns the maximum product that can be formed using nonconsecutive elements of the list. The input list will contain only numbers greater than or equal to 1.
def max_product(s):
    """Return the maximum product that can be formed using
    non-consecutive elements of s.
    >>> max_product([10,3,1,9,2]) # 10 * 9
    90
    >>> max_product([5,10,5,10,5]) # 5 * 5 * 5
    125
    >>> max_product([])
    1
    """
    # empty list case
    if not s:
        return 1
    # one number list case
    elif len(s) == 1:
        return s[0]
    # Choose the max path
    else:
        # Take: choose the current element and skip the next one
        take = s[0] * max_product(s[2:])
        # Skip: skip the current element and choose the take the next one or keep skip the next one
        skip = max_product(s[1:])
        return max(take, skip)