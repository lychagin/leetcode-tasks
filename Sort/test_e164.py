import pytest
from Sort.e164_Maximum_Gap import Solution

@pytest.fixture
def sol_inst():
    return Solution()

@pytest.mark.parametrize(
    "nums, res",
    [
        ([3,6,9,1], 3),
        ([10], 0)
    ]
)
def test_sort(sol_inst, nums, res):
    assert sol_inst.maximumGap(nums) == res