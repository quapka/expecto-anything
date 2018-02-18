#!/usr/bin/python3
import numpy as np
from collections import Counter, defaultdict

"""
In the video Make better software (https://youtu.be/qXZ75Ds5vOs?t=27m13s)
Joel Spolsky gives this exercise:

Given a function rand5, that generates numbers 0-4 (where each outcome is
equally likely) implement a function rand7, that generates numbers 0-6,
where each outcome is equally likely (that is 1/7).
"""


def rand5():
    return np.random.randint(0, 5)

def rand7():
    bits = []
    while len(bits) < 3:
        r = rand5()
        if r == 0:
            bits.append('0')
        if r == 1:
            bits.append('1')

    num = int(''.join([b for b in bits]), 2)

    if num == 7:
        num = rand7()
    return num

if __name__ == '__main__':
    n_samples = 100000
    rands = [rand7() for x in range(n_samples)]
    counter = Counter(rands)
    probs = dict()
    for num, counts in counter.items():
        probs[num] = counts / n_samples

    for x in range(7):
        print(x, counter[x], probs[x])
