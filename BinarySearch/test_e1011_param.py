import pytest
from BinarySearch.e1011_Capacity_To_Ship import Solution

@pytest.fixture
def sol_inst():
    return Solution()

@pytest.mark.parametrize(
    "weights, days, expected",
    [
        ([1,2,3,4,5,6,7,8,9,10], 5, 15),
        ([3,2,2,4,1,4], 3, 6),
        ([1,2,3,1,1], 4, 3)
    ]
)
def test_capacity(sol_inst, weights, days, expected):
    assert sol_inst.shipWithinDays(weights, days) == expected