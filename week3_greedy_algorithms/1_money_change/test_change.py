import pytest

from change import get_change


@pytest.mark.parametrize('m, expected',
                         [(2, 2),
                          (28, 6),
                          (121, 13)])
def test_get_change(m, expected):
    assert get_change(m) == expected
