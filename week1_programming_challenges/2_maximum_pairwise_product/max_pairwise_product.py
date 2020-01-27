# python3
from typing import List


def max_pairwise_product(numbers: List[int]) -> int:
    sorted_numbers = sorted(numbers)
    return sorted_numbers[-1] * sorted_numbers[-2]


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
