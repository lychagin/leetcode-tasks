import pytest
from BinarySearch.e162_Find_Peak_Element import Solution

@pytest.fixture
def sol_inst():
    return Solution()

@pytest.mark.parametrize(
    "nums, result",
    [
        ([1,2,3,1], 2),
        ([1,2,1,3,5,6,4], 5)
    ]
)
def test_peak(sol_inst, nums, result):
    assert sol_inst.findPeakElement(nums) == result