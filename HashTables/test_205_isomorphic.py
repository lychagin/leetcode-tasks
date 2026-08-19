import pytest
import importlib.util
import sys

spec = importlib.util.spec_from_file_location("_205_Isomorphic_Strings", "HashTables/205-Isomorphic_Strings.py")
module = importlib.util.module_from_spec(spec)
sys.modules["_205_Isomorphic_Strings"] = module
spec.loader.exec_module(module)
Solution = module.Solution


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize("s,t,expected", [
    # Basic examples from problem statement
    ("egg", "add", True),
    ("f11", "b23", False),
    ("paper", "title", True),

    # Single character cases
    ("a", "a", True),          # map to self
    ("a", "b", True),          # map to different single char

    # Edge cases for bidirectional mapping
    ("ab", "aa", False),       # b->a, a->a - violation
    ("foo", "bar", False),     # o->a and o->r - violation
])
def test_is_isomorphic(solution, s, t, expected):
    assert solution.isIsomorphic(s, t) == expected