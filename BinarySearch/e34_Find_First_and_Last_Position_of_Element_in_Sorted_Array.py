"""
34. Find First and Last Position of Element in Sorted Array
Ref: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/

Given an array of integers nums sorted in non-decreasing order, 
find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example 1:
----------
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
----------
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
----------
Input: nums = [], target = 0
Output: [-1,-1]

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
"""
import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s | %(message)s", force=True)
logger = logging.getLogger(__name__)
#logger.propagate = False

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        if not nums:
            return [-1, -1]
        
        logger.info(f"nums: {nums}, target: {target}")

        def findFirst(x):
            left , right = 0, len(nums) - 1
            first_idx = -1
            # Используем <= т.к. если в массиве один элемент, то < не сработает и пропустим проверку
            while left <= right:
                mid = left + ((right - left) // 2)
                if nums[mid] >= x:
                    if nums[mid] == x:
                        first_idx = mid
                    right = mid - 1
                else:
                    left = mid + 1
            return first_idx if x == target else left

        start = findFirst(target)
        if start == -1:
            return [-1,-1]
        
        end = findFirst(target + 1) - 1

        return [start, end]