import pytest
from Sort.e347_Top_K_Frequent_Elements_Block_Sort import Solution

@pytest.fixture
def sol_inst():
    return Solution()

@pytest.mark.parametrize(
    "nums, k, res",
    [
        ([1,1,1,2,2,3], 2, [1,2]),
        ([1], 1, [1]),
        ([1,2,1,2,1,2,3,1,3,2], 2, [1,2])
    ]
)
def test_sort(sol_inst: Solution, nums, k, res):
    assert sol_inst.topKFrequent(nums, k) == res