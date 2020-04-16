import pytest

from car_fueling import compute_min_refills


@pytest.mark.parametrize('distance, tank, stops, expected',
                         [(950, 400, [200, 375, 550, 750], 2),
                          (10, 3, [1, 2, 4, 9], -1)])
def test_compute_min_refills(distance, tank, stops, expected):
    assert compute_min_refills(distance, tank, stops) == expected
