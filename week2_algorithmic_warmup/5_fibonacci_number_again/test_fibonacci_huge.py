import pytest

from fibonacci_huge import get_fibonacci_huge


@pytest.mark.parametrize('n, m, expected',
                         [(239, 1000, 161),
                          (2816213588, 239, 151)])
def test_get_fibonacci_huge(n, m, expected):
    assert get_fibonacci_huge(n, m) == expected
