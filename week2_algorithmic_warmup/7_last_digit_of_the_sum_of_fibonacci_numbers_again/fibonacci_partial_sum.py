# Uses python3
import sys


def fibonacci_partial_sum_naive(from_: int, to: int) -> int:
    sum_ = 0

    current = 0
    next_ = 1

    for i in range(to + 1):
        if i >= from_:
            sum_ += current

        current, next_ = next_, current + next_

    return sum_ % 10


def fibonacci_partial_sum(from_: int, to: int) -> int:
    from_ = from_ % 60
    to = to % 60
    if to < from_:
        to += 60

    return fibonacci_partial_sum_naive(from_, to)


if __name__ == '__main__':
    input = sys.stdin.read()
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum(from_, to))
