import pytest
from BinarySearch.e367_vps import Solution

@pytest.fixture
def sol_instance():
    return Solution()

@pytest.mark.parametrize(
    "num, res",
    [
        (16, True),
        (14, False)
    ]
)
def test_square(sol_instance, num, res):
    assert sol_instance.isPerfectSquare(num) == res