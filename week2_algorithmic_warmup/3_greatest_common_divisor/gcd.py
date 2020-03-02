# Uses python3
import sys


def gcd_naive(a: int, b: int) -> int:
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd


def gcd(a: int, b: int) -> int:
    if min(a, b) == 0:
        return max(a, b)
    if a < b:
        return gcd(a, b % a)
    else:
        return gcd(b, a % b)


if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd(a, b))
