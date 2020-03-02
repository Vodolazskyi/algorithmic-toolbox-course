import pytest

from fibonacci_last_digit import get_fibonacci_last_digit


@pytest.mark.parametrize("n, expected",
                         [(3, 2),
                          (331, 9),
                          (327305, 5)])
def test_get_fibonacci_last_digit(n, expected):
    assert get_fibonacci_last_digit(n) == expected
