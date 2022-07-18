def multiply(m, n):
    """
    >>> multiply(5, 3)
    15
    """
    if n == 1:
        return m
    return m + multiply(m, n - 1)


def is_prime(n):
    """
    >>> is_prime(7)
    True
    >>> is_prime(10)
    False
    >>> is_prime(1)
    False
    """
    def prime_helper(cur):
        if cur == 1:
            return True
        elif (cur == 0) or (n % cur == 0):
            return False
        else:
            return prime_helper(cur - 1)
    return prime_helper(n - 1)


def count_stair_ways(n):
    if n == 0:
        return 1
    if n < 0:
        return 0
    return count_stair_ways(n - 1) + count_stair_ways(n - 2)

def count_k(n, k):
    """
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # Only one step at a time
    1
    """
    if n == 0:
        return 1
    if n < 0:
        return 0
    res = 0
    for i in range(1, k + 1):
        res += count_k(n - i, k)
    return res


def even_weighted(s):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    return [s[_] * _ for _ in range(0, len(s), 2)]


def max_product(s):
    """Return the maximum product that can be formed using non-consecutive
    elements of s.
    >>> max_product([10,3,1,9,2]) # 10 * 9
    90
    >>> max_product([5,10,5,10,5]) # 5 * 5 * 5
    125
    >>> max_product([])
    1
    """
    def max_product_helper(cur):
        if cur == []:
            return 1
        return max(cur[0] * max_product_helper(cur[2:]), max_product_helper(cur[1:]))
    return max_product_helper(s)


def check_hole_number(n):
    """
    >>> check_hole_number(123)
    False
    >>> check_hole_number(3241968)
    True
    >>> check_hole_number(3245968)
    False
    """
    if n // 10 == 0:
        return True
    return ((n % 10) > (n // 10 % 10)) and ((n // 100 % 10) > (n // 10 % 10)) and check_hole_number(n // 100)


def check_mountain_number(n):
    """
    >>> check_mountain_number(103)
    False
    >>> check_mountain_number(153)
    True
    >>> check_mountain_number(123456)
    True
    >>> check_mountain_number(2345986)
    True
    """
    def helper(cur, peak=False):
        if cur // 100 == 0:
            return True
        # check the peak point
        if ((cur // 100 % 10) < (cur // 10 % 10)) and ((cur // 10 % 10) > (cur % 10)) and not peak:
            return helper(cur // 10, peak=True)
        # check monotonic and check the next part
        return ((cur // 10 % 10) - (cur % 10)) * ((cur // 100 % 10) - (cur // 10 % 10)) > 0 and helper(cur // 10, peak)
    return helper(n)