# Uses python3
import sys
from typing import List


def get_optimal_value(capacity: int,
                      weights: List[int],
                      values: List[int]) -> float:
    value = 0.
    # write your code here
    values_per_weight = []
    for v, w in zip(values, weights):
        values_per_weight.append((v / w, w))

    for v, w in sorted(values_per_weight, reverse=True):
        if capacity == 0:
            break
        if w <= capacity:
            value += v * w
            capacity -= w
        else:
            value += v * capacity
            capacity = 0

    return round(value, 4)


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
