#!/bin/python3
'''

It's really easy to have off-by-1 errors in these problems.
Pay very close attention to your list indexes and your < vs <= operators.
'''


def find_smallest_positive(xs):
    '''
    Assume that xs is a list of numbers sorted from LOWEST to HIGHEST.
    Find the index of the smallest positive number.
    If no such index exists, return `None`.
    This is essentially the binary search algorithm from class,
    but you're always searching for 0.

    APPLICATION:
    This is a classic question for technical interviews.

    >>> find_smallest_positive([-3, -2, -1, 0, 1, 2, 3])
    4
    >>> find_smallest_positive([1, 2, 3])
    0
    >>> find_smallest_positive([-3, -2, -1]) is None
    True
    '''
    if len(xs) == 0:
        return None
    if len(xs) == 1 and xs[0] <= 0:
        return None
    if xs[-1] <= 0:
        return None
    if xs[0] > 0:
        print(xs.index(xs[0]))
        print(xs)
        return 0
    mid = len(xs) // 2
    if xs[mid] > 0 and xs[mid - 1] <= 0:
        print(mid)
        return mid
    if xs[mid] > 0:
        print(xs)
        return find_smallest_positive(xs[:mid])
    if xs[mid] < 0:
        print(xs)
        return find_smallest_positive(xs[mid:]) + len(xs[:mid])
    if xs[mid] == 0:
        print(xs.index(0) + 1)
        return xs.index(0) + 1


def count_repeats1(xs, x):
    if len(xs) == 0:
        return 0
    if xs[0] <= x:
        return 0
    if xs[-1] > x:
        return 0
    mid = len(xs) // 2
    if xs[mid] == x and xs[mid - 1] != x:
        return mid
    if xs[mid] == x and xs[mid - 1] == x:
        return count_repeats1(xs[:mid], x)
    if xs[mid] > x:
        return count_repeats1(xs[mid:], x) + len(xs[:mid])
    if xs[mid] < x:
        return count_repeats1(xs[:mid], x)


def count_repeats2(xs, x):
    if len(xs) == 0:
        return 0
    if xs[-1] == x:
        return len(xs)
    if xs[-1] > x:
        return 0
    mid = len(xs) // 2
    if xs[mid] < x and xs[mid - 1] >= x:
        return mid
    if xs[mid] >= x:
        return count_repeats2(xs[mid:], x) + len(xs[:mid])
    if xs[mid] < x:
        return count_repeats2(xs[:mid], x)


def count_repeats(xs, x):
    '''
    Assume that xs is a list of numbers sorted from HIGHEST to LOWEST,
    and that x is a number.
    Calculate the number of times that x occurs in xs.

    Use the following three step procedure:
        1) use binary search to find the lowest index with a value >= x
        2) use binary search to find the lowest index with a value < x
        3) return the difference between step 1 and 2
    I highly recommend creating stand-alone functions for steps 1 and 2,
    and write your own doctests for these functions.
    Then, once you're sure these functions work independently,
    completing step 3 will be easy.

    APPLICATION:
    This is a classic question for technical interviews.

    >>> count_repeats([5, 4, 3, 3, 3, 3, 3, 3, 3, 2, 1], 3)
    7
    >>> count_repeats([3, 2, 1], 4)
    0
    '''
    return count_repeats2(xs, x) - count_repeats1(xs, x)


def argmin(f, lo, hi, epsilon=1e-3):
    '''
    The basic algorithm is:
        1) The base case is when hi-lo < epsilon
        2) For each recursive call:
            a) select two points m1 and m2 that are between lo and hi
            b) one of the 4 points (lo,m1,m2,hi) must be the smallest;
    APPLICATION:

    See the pytests for correct examples.

    >>> argmin(lambda x: (x-5)**2, -20, 20)
    5.000040370009773
    >>> argmin(lambda x: (x-5)**2, -20, 0)
    -0.00016935087808430278
    '''
    if hi - lo < epsilon:
        return (lo + hi) / 2
    m1 = lo + (hi - lo) / 3
    m2 = hi - (hi - lo) / 3
    if f(m1) < f(m2):
        return argmin(f, lo, m2, epsilon)
    else:
        return argmin(f, m1, hi, epsilon)

################################################################
# the functions below are extra credit
################################################################


def find_boundaries(f):
    '''
    Returns a tuple (lo,hi).
    This function is useful for initializing argmin.

    HINT:
    Begin with initial values lo=-1, hi=1.
    Let mid = (lo+hi)/2
    if f(lo) > f(mid):
        recurse with lo*=2
    elif f(hi) < f(mid):
        recurse with hi*=2
    else:
        you're done; return lo,hi
    '''


def argmin_simple(f, epsilon=1e-3):
    '''
    you do not need to specify lo and hi.

    NOTE:
    There is nothing to implement for this function.
    If you implement the find_boundaries function correctly,
    then this function will work correctly too.
    '''
