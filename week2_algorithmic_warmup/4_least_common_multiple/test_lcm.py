import pytest

from lcm import lcm


@pytest.mark.parametrize('a, b, expected',
                         [(6, 8, 24),
                          (761457, 614573, 467970912861)])
def test_lcm(a, b, expected):
    assert lcm(a, b) == expected
