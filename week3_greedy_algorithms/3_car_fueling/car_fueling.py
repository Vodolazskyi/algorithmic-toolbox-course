# python3
import sys
from typing import List


def compute_min_refills(distance: int, tank: int, stops: List[int]) -> int:
    # write your code here
    new_stops = [0] + stops + [distance]
    num_refills, current_refill = 0, 0,
    while current_refill <= len(stops):
        last_refill = current_refill
        while current_refill <= len(stops) and \
                new_stops[current_refill+1] - new_stops[last_refill] <= tank:
            current_refill += 1
        if current_refill == last_refill:
            return -1
        if current_refill <= len(stops):
            num_refills += 1
    return num_refills


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
