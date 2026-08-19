"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​. After removing duplicates, return the number of unique elements k.

The first k elements of nums should contain the unique numbers in sorted order. The remaining elements beyond index k - 1 can be ignored.

Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.

 

Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
 

Constraints:

1 <= nums.length <= 3 * 104
-100 <= nums[i] <= 100
nums is sorted in non-decreasing order.
"""
class Solution:
    # Мое решение
    def removeDuplicates(self, nums: list[int]) -> int:
        min_val = min(nums)
        max_val = max(nums)
        zeros_size = max_val - min_val + 1
        zeros = [0] * zeros_size
        for i in nums:
            idx = i - min_val
            zeros[idx] = 1
        sorted_array = []
        pos = 0
        for i in range(zeros_size):
            val = i + min_val
            sorted_array.extend([val] * zeros[i])
            if zeros[i] > 0:
                nums[pos] = val
                pos += 1
        return len(sorted_array)
    # Каноническое решение
    # [1,1,2]
    def removeDuplicates_orig(self, nums: list[int]) -> int:
        if len(nums) == 0: return 0
        k = 1
        for i in range(1, len(nums)):
            print(f"i={i}, nums[i]={nums[i]}; k={k}, nums[k-1]={nums[k-1]}")
            if nums[i] != nums[k-1]:
                nums[k] = nums[i]
                k += 1
        return k

# def count_sort(nums: list[int]) -> list[int]:
#     min_val = min(nums)
#     max_val = max(nums)
#     zeros_size = max_val - min_val + 1
#     zeros = [0] * zeros_size
#     for i in nums:
#         idx = i - min_val
#         zeros[idx] += 1
#     sorted_array = []
#     for i in range(zeros_size):
#         val = i + min_val
#         sorted_array.extend([val] * zeros[i])

#     return sorted_array

def count_sort_unique(nums: list[int]) -> list[int]:
    min_val = min(nums)
    max_val = max(nums)
    zeros_size = max_val - min_val + 1
    zeros = [0] * zeros_size
    for i in nums:
        idx = i - min_val
        zeros[idx] = 1
    sorted_array = []
    for i in range(zeros_size):
        val = i + min_val
        nums[i] = val
        #sorted_array.extend([val] * zeros[i])
    print(f"sorted_array: {sorted_array}")
    return sorted_array


# test_nums = [5, 2, -1, 5]
# count_sort_unique(test_nums)

sol = Solution()

nums = [1,1,2]
expectedNums = [1,2]
k = sol.removeDuplicates(nums)
assert k == len(expectedNums)
for i in range(k):
    assert nums[i] == expectedNums[i]

nums = [0,0,1,1,1,2,2,3,3,4]
expectedNums = [0,1,2,3,4]
k = sol.removeDuplicates_orig(nums)
assert k == len(expectedNums)
for i in range(k):
    assert nums[i] == expectedNums[i]

nums = [0,0,0,0,3]
expectedNums = [0,3]
k = sol.removeDuplicates(nums)
assert k == len(expectedNums)
for i in range(k):
    assert nums[i] == expectedNums[i]
