"""
Given an integer array nums sorted in non-decreasing order, 
return an array of the squares of each number sorted in non-decreasing order.

Example 1:
----------
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]

Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:
----------
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
 

Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?
"""

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        print(f"DEBUG: input nums: {nums}")
        nums_len = len(nums)
        result = [0] * nums_len
        start = 0
        pos = end = nums_len - 1
        while start <= end:
            left = nums[start] * nums[start]
            right = nums[end] * nums[end]
            if left > right:
                result[pos] = left
                start += 1
            else:
                result[pos] = right
                end -= 1
            print(f"DEBUG: i={pos}; result[{pos}]={result[pos]}")
            pos -= 1
        return result
"""    
    def sortedSquares2(self, nums: list[int]) -> list[int]:
        target = [x * x for x in nums]

        minv = min(target)
        maxv = max(target)
        zeros_size = maxv - minv + 1
        #print(f"zeros_size: {zeros_size}")
        zeros = [0] * zeros_size

        i = minv
        while i <= maxv:
            count_d = target.count(i)
            zeros[i - minv] = count_d
            #print(f"iter: {i}; count_d: {count_d}")
            i += 1
        
        #print(f"zeros: {zeros}")
        sorted_arr = []
        i = 0
        for val in range(zeros_size):
            value = val + minv
            sorted_arr.extend([value] * zeros[i])
            #print(f"DEBUG: Sorting [{i}]: sorted_arr: {sorted_arr}")
            i += 1

        return sorted_arr
"""

sol = Solution()

nums1 = [-4,-1,0,3,10]
result = sol.sortedSquares(nums1)        
print(f"result: {result}")

nums2 = [-7,-3,2,3,11]
result = sol.sortedSquares(nums2)        
print(f"result: {result}")
