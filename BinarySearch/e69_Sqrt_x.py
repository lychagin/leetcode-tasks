"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. 
The returned integer should be non-negative as well.
You must not use any built-in exponent function or operator.
For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 
Example 1:
----------
Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.

Example 2:
----------
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., 
and since we round it down to the nearest integer, 2 is returned.
 
Constraints:

0 <= x <= 2^31 - 1
"""
import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s | %(message)s")
logger = logging.getLogger(__name__)

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0: return 0
        left, right = 1, x

        while left <= right:
            mid = left + ((right - left) // 2)
            probe = mid * mid

            if probe == x:
                return mid
            elif probe < x:
                left = mid + 1
            else:
                right = mid - 1

        logger.info(f"right: {right}")
        return right

sol = Solution()

print("TEST 1")
assert sol.mySqrt(4) == 2

print("TEST 2")
assert sol.mySqrt(8) == 2