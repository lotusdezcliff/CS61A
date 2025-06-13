# Q1: Map, Filter, Reduce
def my_map(fn, seq):
    """Applies fn onto each element in seq and returns a list.
    >>> my_map(lambda x: x*x, [1, 2, 3])
    [1, 4, 9]
    """
    "*** YOUR CODE HERE ***"
    return [fn(x) for x in seq]

def my_filter(pred, seq):
    """Keeps elements in seq only if they satisfy pred.
    >>> my_filter(lambda x: x % 2 == 0, [1, 2, 3, 4])  # new list has only even-valued elements
    [2, 4]
    """
    "*** YOUR CODE HERE ***"
    return [x for x in seq if pred(x)]

def my_reduce(combiner, seq):
    """Combines elements in seq using combiner.
    seq will have at least one element.
    >>> my_reduce(lambda x, y: x + y, [1, 2, 3, 4])  # 1 + 2 + 3 + 4
    10
    >>> my_reduce(lambda x, y: x * y, [1, 2, 3, 4])  # 1 * 2 * 3 * 4
    24
    >>> my_reduce(lambda x, y: x * y, [4])
    4
    >>> my_reduce(lambda x, y: x + 2 * y, [1, 2, 3]) # (1 + 2 * 2) + 2 * 3
    11
    """
    "*** YOUR CODE HERE ***"
    if len(seq) == 1:
        return seq[0]
    else:
        while len(seq) >= 2:
            result = combiner(seq[0], seq[1])
            seq[0] = result
            seq.pop(1)
        return seq[0]

# Q2: WWPD: Mutability
# What would Python display? In addition to giving the output, draw the box and pointer diagrams for each list to the right.

# >>> s1 = [1, 2, 3]
# >>> s2 = s1
# >>> s1 is s2
# Output: True

# >>> s2.extend([5, 6])
# >>> s1[4]
# Output: 6

# >>> s1.append([-1, 0, 1])
# >>> s2[5]
# Output: [-1, 0, 1]

# >>> s3 = s2[:]
# >>> s3.insert(3, s2.pop(3))
# >>> len(s1)
# Output: 6

# >>> s1[4] is s3[6]
# Output: False

# >>> s3[s2[4][1]]
# Output: 1

# >>> s1[:3] is s2[:3]
# Output: False

# >>> s1[:3] == s2[:3]
# Output: True

# >>> s1[4].append(2)
# >>> s3[6][3]
# Output: Error