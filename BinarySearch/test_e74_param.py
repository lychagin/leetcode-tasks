import pytest
from BinarySearch.e74_Search_a_2D_Matrix import Solution

@pytest.fixture
def sol_inst():
    return Solution()

@pytest.mark.parametrize(
    "matrix, target, result",
    [
        ([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3, True),
        ([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13, False)
    ]
)
def test_find_target(sol_inst, matrix, target, result):
    assert sol_inst.searchMatrix(matrix, target) == result
