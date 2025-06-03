HW_SOURCE_FILE = __file__

"""Q1: Neighbor Digits
Implement the function neighbor_digits. neighbor_digits takes in a positive integer num and an optional argument prev_digit. 
neighbor_digits outputs the number of digits in num that have the same digit to its right or left."""
def neighbor_digits(num, prev_digit=-1, count=0):
    """
    Returns the number of digits in num that have the same digit to its right
    or left.
    >>> neighbor_digits(111)
    3
    >>> neighbor_digits(123)
    0
    >>> neighbor_digits(112)
    2
    >>> neighbor_digits(1122)
    4
    """
    "*** YOUR CODE HERE ***"
    last_digit = num % 10
    second_last_digit = (num // 10) % 10
    # Base Case
    if num < 10:
        if last_digit == prev_digit:
            count += 1
        return count
    # Recursive Case
    else:
        if prev_digit == last_digit or last_digit == second_last_digit:
            count += 1
            prev_digit = last_digit
        num = (num - last_digit) // 10
        return neighbor_digits(num, prev_digit, count)
        
    

        
    

"""Q2: Has Subsequence
Implement the function has_subseq, which takes in a number n and a "sequence" of digits seq. 
The function returns whether n contains seq as a subsequence, which does not have to be consecutive.
For example, 141 contains the sequence 11 because the first digit of the sequence, 1, is the first digit of 141, and the next digit of the sequence, 1, is found later in 141."""
def has_subseq(n, seq):
    """
    Complete has_subseq, a function which takes in a number n and a "sequence"
    of digits seq and returns whether n contains seq as a subsequence, which
    does not have to be consecutive.

    >>> has_subseq(123, 12)
    True
    >>> has_subseq(141, 11)
    True
    >>> has_subseq(144, 12)
    False
    >>> has_subseq(144, 1441)
    False
    >>> has_subseq(1343412, 134)
    True
    """
    "*** YOUR CODE HERE ***"
    # Impossible subseq
    if seq > n:
        return False
    
    last_digit_n = n % 10
    last_digit_seq = seq % 10
    
    if seq == 0:
        return True
    if n == 0:
        return False
    if seq > 0 and n > 0:
        if last_digit_n == last_digit_seq:
            n, seq = n // 10, seq // 10
        else:
            n = n // 10
    return has_subseq(n, seq)
        


def num_eights(pos, count=0):
    """Returns the number of times 8 appears as a digit of pos.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr'])
    True
    """
    "*** YOUR CODE HERE ***"
    if pos == 0:
        return count
    if pos > 0:
        if pos % 10 == 8:
            return num_eights(pos // 10, count + 1)
        else:
            return num_eights(pos // 10, count)
# 1 test cases passed! No cases failed.   




def pingpong(n, count=1, dir=1, total_count=1):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(8)
    8
    >>> pingpong(10)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    -2
    >>> pingpong(30)
    -2
    >>> pingpong(68)
    0
    >>> pingpong(69)
    -1
    >>> pingpong(80)
    0
    >>> pingpong(81)
    1
    >>> pingpong(82)
    0
    >>> pingpong(100)
    -6
    >>> from construct_check import check
    >>> # ban assignment statements
    >>> check(HW_SOURCE_FILE, 'pingpong',
    ...       ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr'])
    True
    """
    "*** YOUR CODE HERE ***"
    def direction(x):
        return x * -1
    
    def any_eight(x):
        return '8' in str(x)

    if n == total_count:
        return count
    if n > total_count:
        if any_eight(total_count) or total_count % 8 == 0:
            return pingpong(n, count + direction(dir), direction(dir), total_count + 1)
        else:
            return pingpong(n, count + dir, dir, total_count + 1)
#     1 test cases passed! No cases failed.




    



def get_larger_coin(coin):
    """Returns the next larger coin in order.
    >>> get_larger_coin(1)
    5
    >>> get_larger_coin(5)
    10
    >>> get_larger_coin(10)
    25
    >>> get_larger_coin(2) # Other values return None
    """
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25


def get_smaller_coin(coin):
    """Returns the next smaller coin in order.
    >>> get_smaller_coin(25)
    10
    >>> get_smaller_coin(10)
    5
    >>> get_smaller_coin(5)
    1
    >>> get_smaller_coin(2) # Other values return None
    """
    if coin == 25:
        return 10
    elif coin == 10:
        return 5
    elif coin == 5:
        return 1


def count_coins(change, coin=25):
    """Return the number of ways to make change using coins of value of 1, 5, 10, 25.
    >>> count_coins(15)
    6
    >>> count_coins(10)
    4
    >>> count_coins(20)
    9
    >>> count_coins(100) # How many ways to make change for a dollar?
    242
    >>> count_coins(200)
    1463
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_coins', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    if change == 0:
        return 1
    elif change < 0:
        return 0
    elif coin == None:
        return 0
    else:
        return count_coins(change - coin, coin) + count_coins(change, get_smaller_coin(coin))
#    1 test cases passed! No cases failed.


"""
>>> def count_partitions(n, m):
     计算使用最大数 m 的整数分割 n 的方式的数量
     if n == 0:
         return 1
     elif n < 0:
         return 0
     elif m == 0:
         return 0
     else:
         return count_partitions(n-m, m) + count_partitions(n, m-1)

>>> count_partitions(6, 4)
9
>>> count_partitions(5, 5)
7
>>> count_partitions(10, 10)
42
>>> count_partitions(15, 15)
176
>>> count_partitions(20, 20)
627
"""