import pytest

from fibonacci_partial_sum import fibonacci_partial_sum


@pytest.mark.parametrize('from_, to, expected',
                         [(3, 7, 1),
                          (10, 10, 5),
                          (10, 200, 2)])
def test_fibonacci_partial_sum(from_, to, expected):
    assert fibonacci_partial_sum(from_, to) == expected
