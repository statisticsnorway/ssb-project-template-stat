#!/usr/bin/python3
from typing import Iterable


def fizz(x: int) -> str:
    if x % 3 == 0:
        return "fizz"
    return ""


def buzz(x: int) -> str:
    if x % 5 == 0:
        return "buzz"
    return ""


def fizzbuzz(x: Iterable[int]) -> list[str]:
    result = []
    for y in x:
        r = ""
        r = fizz(y) + buzz(y)
        if not r:
            r = str(y)
        result.append(r)
    return result
