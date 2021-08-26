#!/home/mark/penvs/generic/bin/python

import functools

# =============================================================================
# def memoize(f):
#     memo = {}
#     def helper(x):
#         if x not in memo:            
#             memo[x] = f(x)
#         return memo[x]
#     return helper
# =============================================================================

def fib_helper(n, memo):    
    q = 0
    if memo[n] >- 0:
        return memo[n]
    if n == 0 or n == 1:
        q = n
    else:
        if n not in memo:
            q = fib_helper(n-1, memo) + fib_helper(n-2, memo)
    memo[n] = q
    return q

def fib(n):
    memo = [-1]*(n + 1)
    return fib_helper(n, memo)


@functools.lru_cache()
def fib_lru_cache(n):
    if n < 2:
        return n
    else:
        return fib_lru_cache(n - 2) + fib_lru_cache(n - 1)


def fastFib(n, memo = {}):
    """Assumes n is an int >= 0, memo used only by recursive calls
       Returns Fibonacci of n"""
    if n == 0 or n == 1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result = fastFib(n-1, memo) + fastFib(n-2, memo)
        memo[n] = result
        return result

for i in range(121):
    print('fib(' + str(i) + ') =', fastFib(i))


