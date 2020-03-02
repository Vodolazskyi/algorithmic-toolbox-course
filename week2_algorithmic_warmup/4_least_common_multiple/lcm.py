# Uses python3
import sys


def lcm_naive(a: int, b: int) -> int:
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a * b


def gcd(a: int, b: int) -> int:
    if min(a, b) == 0:
        return max(a, b)
    if a < b:
        return gcd(a, b % a)
    else:
        return gcd(b, a % b)


def lcm(a: int, b: int) -> int:
    return int(a * b / gcd(a, b))


if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))
