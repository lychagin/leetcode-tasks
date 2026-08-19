import pytest
from BinarySearch.e34_Find_First_and_Last_Position_of_Element_in_Sorted_Array import Solution

@pytest.fixture
def sol_inst():
    return Solution()

@pytest.mark.parametrize(
    "nums, target, res",
    [
        ([5,7,7,8,8,10], 8, [3,4]),
        ([5,7,7,8,8,10], 6, [-1,-1]),
        ([], 0, [-1,-1])
    ]
)
def test_tange(sol_inst, nums, target, res):
    assert sol_inst.searchRange(nums, target) == res