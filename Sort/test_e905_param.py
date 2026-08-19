import pytest
from Sort.e905_Sort_Array_By_Parity import Solution

@pytest.fixture
def sol_inst():
    return Solution()

@pytest.mark.parametrize(
    "nums, result",
    [
        ([3,1,2,4], [2,4,3,1]),
        ([0], [0])
    ]
)
def test_sort(sol_inst, nums, result):
    assert sol_inst.sortArrayByParity(nums) == result