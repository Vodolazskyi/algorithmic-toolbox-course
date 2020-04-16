# Uses python3
import sys
from collections import namedtuple
from operator import attrgetter
from typing import List


Segment = namedtuple('Segment', 'start end')


def optimal_points(segments: List[Segment]) -> List:
    points = []
    # write your code here
    for s in sorted(segments, key=attrgetter('end')):
        if not points:
            points.append(s.end)
        else:
            if s.end < points[-1] or s.start > points[-1]:
                points.append(s.end)
    return points


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2],
                                                           data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
