import pytest
from BinarySearch.e33_Search_in_Rotated_Sorted_Array import Solution

@pytest.fixture
def sol_inst():
    return Solution()

@pytest.mark.parametrize(
    "nums, target, result",
    [
        ([4,5,6,7,0,1,2], 0, 4),
        ([4,5,6,7,0,1,2], 3, -1),
        ([1], 0, -1)
    ]
)
def test_sort(sol_inst, nums, target, result):
    assert sol_inst.search(nums, target) == result