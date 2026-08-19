"""
Ref: https://leetcode.com/problems/valid-perfect-square/
Name: 367. Valid Perfect Square

Given a positive integer num, return true if num is a perfect square or false otherwise.
A perfect square is an integer that is the square of an integer. 
In other words, it is the product of some integer with itself.

You must not use any built-in library function, such as sqrt.

Example 1:
----------
Input: num = 16
Output: true
Explanation: We return true because 4 * 4 = 16 and 4 is an integer.

Example 2:
----------
Input: num = 14
Output: false
Explanation: We return false because 3.742 * 3.742 = 14 and 3.742 is not an integer.

Constraints:

1 <= num <= 231 - 1
"""
import logging

#logging.basicConfig(level=logging.DEBUG, format="%(levelname)s | %(message)s")
logging.basicConfig(level=logging.DEBUG, format="%(levelname)s [%(filename)s] | %(message)s")
logger = logging.getLogger("T1")

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # x = 16, return True
        result = False
        left, right = 0, num
        while left <= right:
            mid = left + ((right - left) // 2)
            probe = mid * mid
            #logger.debug(f"num: {num}; left: {left}, right: {right}, mid: {mid}, probe: {probe}")
            if probe == num:
                return True
            elif probe < num:
                left = mid + 1
            elif probe > num:
                right = mid - 1
        return result

sol = Solution()
