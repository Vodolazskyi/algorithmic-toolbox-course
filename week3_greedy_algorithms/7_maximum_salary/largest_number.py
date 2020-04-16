# Uses python3
import copy
import sys
from typing import List


def is_greater_or_equal(digit: int, max_digit: int) -> bool:
    return int(str(digit)+str(max_digit)) >= int(str(max_digit)+str(digit))


def largest_number(a: List[int]) -> int:
    # write your code here
    res = []
    numbers = copy.deepcopy(a)
    while numbers:
        max_digit = 0
        for digit in numbers:
            if is_greater_or_equal(digit, max_digit):
                max_digit = digit
        res.append(max_digit)
        numbers.remove(max_digit)
    return int(''.join([str(x) for x in res]))


if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
