import pytest

from gcd import gcd


@pytest.mark.parametrize("a, b, expected",
                         [(18, 35, 1),
                          (28851538, 1183019, 17657)])
def test_gcd(a, b, expected):
    assert gcd(a, b) == expected
