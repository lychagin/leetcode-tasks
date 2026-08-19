"""
Given an array of integers nums, calculate the pivot index of this array.
The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.
If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.
Return the leftmost pivot index. If no such index exists, return -1.


Example 1:
----------
Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11

Example 2:
----------
Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.

Example 3:
----------
Input: nums = [2,1,-1]
Output: 0
Explanation:
The pivot index is 0.
Left sum = 0 (no elements to the left of index 0)
Right sum = nums[1] + nums[2] = 1 + -1 = 0
 

Constraints:

1 <= nums.length <= 104
-1000 <= nums[i] <= 1000
"""
class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        nsize = len(nums)
        target = [0] * (nsize + 1)
        for i in range(nsize):
            target[i+1] = target[i] + nums[i]
        total_sum = target[nsize]
        for j in range(nsize):
            left_sum = target[j] # Сумма элементов слева от j (indices 0..j-1)
            right_sum = total_sum - left_sum - nums[j]  # Всё остальное без текущего элемента
            if left_sum == right_sum:
                return j
        return -1

sol = Solution()

print("TEST 1")
nums = [1,7,3,6,5,6]
assert sol.pivotIndex(nums) == 3

print("TEST 2")
nums = [1,2,3]
assert sol.pivotIndex(nums) == -1

print("TEST 3")
nums = [2,1,-1]
assert sol.pivotIndex(nums) == 0