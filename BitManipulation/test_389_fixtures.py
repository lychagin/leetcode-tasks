import pytest
from BitManipulation.e389_Find_the_Difference import Solution

@pytest.fixture
def solution_instance():
    return Solution()

def test_find_the_difference_basic(solution_instance):
    s = "abcd"
    t = "abcde"
    assert solution_instance.findTheDifference(s, t) == "e"

def test_find_the_difference_empty_s(solution_instance):
    s = ""
    t = "y"
    assert solution_instance.findTheDifference(s, t) == "y"