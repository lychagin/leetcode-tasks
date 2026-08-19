"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

Example 1:
-----------
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
-----------
Input: nums = [0]
Output: [0]
 

Constraints:
1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1

Follow up: Could you minimize the total number of operations done?
"""
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Мое решение
        nums_size = len(nums)
        pos = 0
        for i in range(nums_size):
            if nums[i] != 0:
                nums[pos] = nums[i]
                pos += 1

        for i in range (pos, nums_size):
            nums[i] = 0
    # Каноническое решение
    def moveZeroes_orig(self, nums: list[int]) -> None:
        snowball = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                snowball += 1
            elif snowball > 0:
                nums[i], nums[i - snowball] = nums[i - snowball], nums[i]
        

sol = Solution()

print("TEST 1")
print("------")
nums = [0,1,0,3,12]
expected = [1,3,12,0,0]
print(f"nums BEFORE: {nums}; expected: {expected}")
sol.moveZeroes(nums)
print(f"nums AFTER: {nums}")
for i in range(len(expected)):
    assert nums[i] == expected[i]

print("TEST 2")
print("------")
nums = [0]
expected = [0]
print(f"nums BEFORE: {nums}; expected: {expected}")
sol.moveZeroes(nums)
print(f"nums AFTER: {nums}")
for i in range(len(expected)):
    assert nums[i] == expected[i]
