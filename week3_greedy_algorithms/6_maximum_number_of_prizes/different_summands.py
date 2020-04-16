# Uses python3
import sys
from typing import List


def optimal_summands(n: int) -> List[int]:
    summands: List[int] = []
    # write your code here
    rest = n
    for i in range(1, n+1):
        if i <= rest:
            summands.append(i)
            rest -= i
        else:
            summands[-1] += rest
            break
    return summands


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
