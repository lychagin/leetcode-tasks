import pytest
from BitManipulation.e389_Find_the_Difference import Solution

@pytest.fixture
def solution_instance():
    return Solution()

@pytest.mark.parametrize(
    "s,t,expected",
    [
        ("abcd", "abcde", "e"),
        ("", "y", "y"),
        ("a", "aa", "a"),
        ("xyz", "zyxa", "a"),
    ],
)
def test_find_the_difference(solution_instance, s, t, expected):
    assert solution_instance.findTheDifference(s, t) == expected
