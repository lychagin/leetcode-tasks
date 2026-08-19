"""
75. Sort Colors
Ref: https://leetcode.com/problems/sort-colors/description/?envType=problem-list-v2&envId=sorting

Given an array nums with n objects colored red, white, or blue, 
sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.

Example 1:
----------
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:
----------
Input: nums = [2,0,1]
Output: [0,1,2]
 
Constraints:
------------
n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.
 

Follow up: Could you come up with a one-pass algorithm using only constant extra space?
"""
class Solution:
    def sortColors(self, nums: list[int]) -> None:
        if not nums:
            return nums

        # 1. Находим минимальное и максимальное значение в массиве
        min_val: int = min(nums)
        max_val: int = max(nums)

        # Разница между макс и мин определяет размер массива счетчиков
        range_of_elements = max_val - min_val + 1
        count_arr = [0] * range_of_elements

        # 2. Подсчитываем количество каждого элемента
        # Используем (num - min_val), чтобы сдвинуть отрицательные числа в диапазон от 0
        for num in nums:
            count_arr[num - min_val] += 1

        # 3. Перезаписываем исходный массив nums на основе подсчитанных данных
        idx = 0
        for i in range(range_of_elements):
            while count_arr[i] > 0:
                nums[idx] = i + min_val # Возвращаем исходное число (добавляем мин. значение)
                idx += 1
                count_arr[i] -= 1
        return nums

sol = Solution()
nums = [2,0,2,1,1,0]
sol.sortColors(nums)            
print(f"nums: {nums}")