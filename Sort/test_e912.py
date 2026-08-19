import pytest
from Sort.e912_Bubble_Sort_an_Array import Solution

@pytest.fixture
def sol_inst():
    return Solution()

@pytest.mark.parametrize(
    "nums, result",
    [
        ([5,2,3,1], [1,2,3,5]),
        ([5,1,1,2,0,0], [0,0,1,1,2,5])
    ]
)
def test_bubble_sort(sol_inst, nums, result):
    assert sol_inst.sortArray(nums) == result