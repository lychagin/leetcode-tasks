"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 
12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. 
However, the numeral for four is not IIII. Instead, the number four is written as IV. 
Because the one is before the five we subtract it making four. 
The same principle applies to the number nine, which is written as IX. 
There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.


Example 1:
----------
Input: s = "III"
Output: 3
Explanation: III = 3.

Example 2:
-----------
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 3:
----------
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

Constraints:

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].
"""
from operator import ne
from unittest import result


class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict_double = {
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
        }
        roman_dict_ones = {
            "I":  1,
            "V":  5,
            "X":  10,
            "L":  50,
            "C":  100,
            "D":  500,
            "M":  1000
        }
        sum = 0
        s_len = len(s)
        i = 0
        while i < s_len:
            one = s[i]
            if i < s_len - 1:
                next = s[i+1]
                #print(f"one: {one}; next: {next}")
                possible_double = one + next
            else:
                possible_double = one
            if possible_double in roman_dict_double:
                val = roman_dict_double.get(possible_double)
                sum += val
                i += 2
            else:
                val = roman_dict_ones.get(one)
                sum += val
                i += 1

        #print(f"sum: {sum}")
        return sum

sol = Solution()

print("TEST 1")
s = "III"
exp = 3
result = sol.romanToInt(s)
assert result == exp

print("TEST 2")
s = "LVIII"
exp = 58
result = sol.romanToInt(s)
assert result == exp

print("TEST 3")
s = "MCMXCIV"
exp = 1994
result = sol.romanToInt(s)
assert result == exp