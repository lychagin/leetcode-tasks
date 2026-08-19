"""
Given a sorted array of distinct integers and a target value, 
return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.

Example 1:
----------
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
---------
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
----------
Input: nums = [1,3,5,6], target = 7
Output: 4

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104
"""
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        idx = -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            idx = left + ((right - left) // 2)
            val = nums[idx]
            if val > target:
                right = idx - 1
            elif val < target:
                left = idx + 1
            elif val == target:
                return idx

        return left

sol = Solution()

# print("TEST 1")
# nums = [1,3,5,6]
# target = 5
# exp = 2
# assert sol.searchInsert(nums, target) == exp

# print("TEST 2")
# nums = [1,3,5,6]
# target = 2
# exp = 1
# assert sol.searchInsert(nums, target) == exp

# print("TEST 3")
# nums = [1,3,5,6]
# target = 7
# exp = 4
# assert sol.searchInsert(nums, target) == exp

print("TEST 4")
nums = [1,3,5,6]
target = 0
exp = 0
assert sol.searchInsert(nums, target) == exp