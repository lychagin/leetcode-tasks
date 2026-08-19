"""
Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving 
the order of characters. No two characters may map to the same character, but a character may map to itself.

Example 1:
----------
Input: s = "egg", t = "add"

Output: true

Explanation:

The strings s and t can be made identical by:

Mapping 'e' to 'a'.
Mapping 'g' to 'd'.

Example 2:
----------
Input: s = "f11", t = "b23"

Output: false

Explanation:

The strings s and t can not be made identical as '1' needs to be mapped to both '2' and '3'.

Example 3:
----------
Input: s = "paper", t = "title"

Output: true

Constraints:

1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.
"""
from unittest import result

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        result = True
        transcode = {}
        transcode_contra = {}
        # s = "f11"
        # t = "b23"
        for first, second in zip(s, t):
            # второе назначение одного символа. Было - a-> x, сейчас a -> y. Сразу неправильно
            if first in transcode and transcode[first] != second:
                return False
            else:
                transcode[first] = second

            if second in transcode_contra and transcode_contra[second] != first:
                return False
            else:
                transcode_contra[second] = first

        return result

sol = Solution()

print("TEST 1")
s = "egg"
t = "add"
expected = True
result = sol.isIsomorphic(s, t)
assert result == expected

print("TEST 2")
s = "f11"
t = "b23"
expected = False
result = sol.isIsomorphic(s, t)
assert result == expected

print("TEST 3")
s = "paper"
t = "title"
expected = True
result = sol.isIsomorphic(s, t)
assert result == expected