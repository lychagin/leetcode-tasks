"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
----------
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
----------
Input: s = "rat", t = "car"
Output: false

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""
from collections import Counter

class Solution:
    def checkDict(self, s: dict, l: str):
        if l in s:
            s[l] = s.get(l) + 1
        else:
            s[l] = 1

    def isAnagram(self, s: str, t: str) -> bool:
        s_len = len(s)
        t_len = len(t)
        if (s_len != t_len): return False

        sc_count = Counter()
        tc_count = Counter()
        #s_dict = dict()
        #t_dict = dict()
        for i in range(len(s)):
            s_letter = s[i]
            t_letter = t[i]
            sc_count[s_letter] += 1
            tc_count[t_letter] += 1
            #self.checkDict(s_dict, s_letter)
            #self.checkDict(t_dict, t_letter)

        #if s_dict == t_dict:
        if sc_count == tc_count:
            result = True
        else:
            result = False
        return result

sol = Solution()

print("TEST 1")
s = "anagram"
t = "nagaram"
result = sol.isAnagram(s, t)
assert result == True

print("TEST 2")
s = "rat"
t = "car"
result = sol.isAnagram(s, t)
assert result == False