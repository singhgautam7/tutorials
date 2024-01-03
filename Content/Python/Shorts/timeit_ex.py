"""
A program to compare the time between appending
100 million items in a list and a list comprehension
"""

import timeit

def for_loop_append():
    res = []
    for i in range(100_000_000):
        res.append(i)
    return res

def list_comprehension():
    res = [i for i in range(100_000_000)]
    return res

if __name__ == '__main__':
    time1 = timeit.timeit(for_loop_append, number=1)
    time2 = timeit.timeit(list_comprehension, number=1)

    # Two things to note here
    # 1. Write the func name without parenthesis '()'
    # 2. The parameter 'number' states how many times
    #    you want to run the function to check.
    #    For ex - if the value of the param is 10,
    #    then it will return the avg time of running
    #    the function 10 times.

    print(f"For loop - {time1:.2f}s")
    print(f"List compr. - {time2:.2f}s")
