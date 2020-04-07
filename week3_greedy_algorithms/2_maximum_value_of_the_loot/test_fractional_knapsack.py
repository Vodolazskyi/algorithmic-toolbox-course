import pytest

from fractional_knapsack import get_optimal_value


@pytest.mark.parametrize('capacity, weights, values, expected',
                         [(50, [20, 50, 30], [60, 100, 120], 180.0),
                          (10, [30], [500], 166.6667)])
def test_get_optimal_value(capacity, weights, values, expected):
    assert get_optimal_value(capacity, weights, values) == expected
