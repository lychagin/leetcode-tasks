from BitManipulation.e389_Find_the_Difference import Solution

def test_find_basic_diff_1():
    sol = Solution()
    print("TEST1")
    s = "abcd"
    t = "abcde"
    exp = "e"
    result = sol.findTheDifference(s, t)
    assert result == exp

def test_find_basic_diff_2():
    sol = Solution()
    print("TEST2")
    s = ""
    t = "y"
    exp = "y"
    result = sol.findTheDifference(s, t)
    assert result == exp

