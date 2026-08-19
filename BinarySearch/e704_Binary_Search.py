"""
Given an array of integers nums which is sorted in ascending order, 
and an integer target, write a function to search target in nums. 
If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
----------
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
----------
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
 

Constraints:

1 <= nums.length <= 104
-104 < nums[i], target < 104
All the integers in nums are unique.
nums is sorted in ascending order.
"""
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        targetIndex = -1
        left = 0
        right = len(nums) - 1
        idx = 0
        while left <= right:
            idx = left + ((right - left) // 2)
            probeNum = nums[idx]
            # left = 0, right = 5, mid = 2, probeNum = 3
            if probeNum > target:
                # надо искать левее
                right = idx - 1
            elif probeNum < target:
                # ищем правее
                left = idx + 1
            elif probeNum == target:
                targetIndex = idx
                break;
            else:
                left += 1
                right -= 1
        return targetIndex

sol = Solution()

print(f"TEST 1")
nums = [-1,0,3,5,9,12]
target = 9
pos = 4
assert sol.search(nums, target) == pos

print(f"TEST 2")
nums = [-1,0,3,5,9,12]
target = 2
pos = -1
assert sol.search(nums, target) == pos

print(f"TEST 3")
nums = [5]
target = 5
pos = 0
assert sol.search(nums, target) == pos