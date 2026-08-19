import pytest
from Sort.e75_Sort_Colors import Solution

@pytest.fixture
def sol_inst():
    return Solution()

@pytest.mark.parametrize(
    "nums, res",
    [
        ([2,0,2,1,1,0], [0,0,1,1,2,2]),
        ([2,0,1], [0,1,2])
    ]
)
def test_colors(sol_inst, nums, res):
    assert sol_inst.sortColors(nums) == res