# Uses python3
import sys


def fibonacci_partial_sum_naive(from_: int, to: int) -> int:
    sum_ = 0

    current = 0
    next_   = 1

    for i in range(to + 1):
        if i >= from_:
            sum_ += current

        current, next_ = next_, current + next_

    return sum_ % 10


if __name__ == '__main__':
    input = sys.stdin.read()
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_naive(from_, to))
