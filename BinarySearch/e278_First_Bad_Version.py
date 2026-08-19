"""
You are a product manager and currently leading a team to develop a new product. 
Unfortunately, the latest version of your product fails the quality check. 
Since each version is developed based on the previous version, 
all the versions after a bad version are also bad.
Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, 
which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. 
Implement a function to find the first bad version. 
You should minimize the number of calls to the API.

Example 1:
----------
Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.

Example 2:
----------
Input: n = 1, bad = 1
Output: 1

Constraints:

1 <= bad <= n <= 231 - 1
"""
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s | %(message)s")
logger = logging.getLogger(__name__)

class Stubber:
    def __init__(self, vals: list[bool]):
        self.vals = vals

    def isBadVersion(self, idx: int) -> bool:
        return self.vals[idx]

class Solution:
    def __init__(self, st: Stubber):
        self.st = st

    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        while left < right:
            idx = left + ((right - left) // 2) 
            # idx = 2, val = false. ищем дальше. true правее
            ok = self.st.isBadVersion(idx)
            logger.info(f"n={n}, left={left}; right={right}; idx={idx}; ok={ok}")
            if not ok:
                left = idx + 1
            else:
                # value = true. уже сбойная версия. нужно найти левее - есть ли еще одна?
                right = idx

        logger.info(f"FINAL: n={n}, left={left}; right={right}; idx={idx}; ")
            
        return left


st = Stubber([False, False, False, False, True, True])
sol = Solution(st)

print("TEST 1")
sol.firstBadVersion(5)
assert sol.firstBadVersion(5) == 4

print("TEST 2")
assert sol.firstBadVersion(1) == 1

print("TEST 3")
assert sol.firstBadVersion(2) == 2