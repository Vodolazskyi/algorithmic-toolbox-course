# Uses python3
import sys


def get_change(m: int) -> int:
    # write your code here
    coins = [10, 5, 1]
    rest = m
    change = 0
    for coin in coins:
        if rest // coin == 0:
            next
        change += rest // coin
        rest = rest % coin
    return change


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
