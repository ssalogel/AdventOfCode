from typing import Optional
from math import sqrt, floor
from itertools import chain, cycle, accumulate


def bitwise_not(operand: int, mask: Optional[int] = None) -> int:
    if mask:
        return ~operand & mask
    return ~operand


def bitwise_or(a: int, b: int, mask: Optional[int] = None) -> int:
    if mask:
        return (a | b) & mask
    return a | b


def bitwise_and(a: int, b: int, mask: Optional[int] = None) -> int:
    if mask:
        return (a & b) & mask
    return a & b


def bitwise_lshift(a: int, magnitude: int, mask: Optional[int] = None):
    if mask:
        return (a << magnitude) & mask
    return a << magnitude


def bitwise_rshift(a: int, magnitude: int, mask: Optional[int] = None):
    if mask:
        return (a >> magnitude) & mask
    return a >> magnitude


def divisors(n: int) -> list[int]:
    divisors = set()
    for i in range(1, floor(sqrt(n))+1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n//i)
    return sorted(divisors)


def magic_divisors(n: int) -> list[int]:
    """https://rosettacode.org/wiki/Factors_of_an_integer#Python"""
    def prime_powers(n):
        # c goes through 2, 3, 5, then the infinite (6n+1, 6n+5) series
        for c in accumulate(chain([2, 1, 2], cycle([2, 4]))):
            if c * c > n:
                break
            if n % c:
                continue
            d, p = (), c
            while not n % c:
                n, p, d = n // c, p * c, d + (p,)  # type: ignore
            yield (d)
        if n > 1:
            yield ((n,))

    r = [1]
    for e in prime_powers(n):
        r += [a * b for a in r for b in e]
    return r
