"""
Given an integer array nums, return the maximum difference between two successive elements in its sorted form. If the array contains less than two elements, return 0.
You must write an algorithm that runs in linear time and uses linear extra space.

Example 1:
----------
Input: nums = [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either (3,6) or (6,9) has the maximum difference 3.

Example 2:
----------
Input: nums = [10]
Output: 0
Explanation: The array contains less than 2 elements, therefore return 0.
 

Constraints:
------------
1 <= nums.length <= 105
0 <= nums[i] <= 109
"""
import logging
import time

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s | %(message)s", force=True)
logger = logging.getLogger(__name__)

class Solution:
    def maximumGap(self, nums: list[int]) -> int:
        if len(nums) < 2:
            return 0

        max_num = max(nums)
        # Запускаем поразрядную сортировку в цикле
        # exp последовательно принимает значения: 1, 10, 100, 1000...
        exp = 1
        while max_num // exp > 0:
            # На каждом шаге перезаписываем nums результатом сортировки текущего разряда
            nums = self.sort_radix(nums, exp)
            exp *= 10

        # find max difference between adjacent nums
        idx = 0
        end = len(nums)
        max_diff = 0

        while idx < end:
            if idx + 1 < end:
                curr_diff = nums[idx + 1] - nums[idx]
                if curr_diff > max_diff:
                    max_diff = curr_diff
            idx += 1

        return max_diff

    def sort_radix(self, nums: list[int], exp: int) -> list[int]:
        count = [0] * 10
        output = [0] * len(nums)

        # 1. Считаем, сколько каких цифр у нас есть (как у вас, но без append)
        for i in nums:
            last_digit = (i // exp) % 10 # Получаем цифру нужного разряда
            count[last_digit] += 1
        # 2. Магия: превращаем количество в индексы.
        # Каждая ячейка будет хранить КРАЙНЮЮ ПРАВУЮ позицию для этой цифры в будущем массиве.
        for i in range(1, 10):
            count[i] += count[i - 1]
        # 3. Раскладываем числа в правильном порядке в плоский массив output
        # Идем с конца исходного массива nums (это важно для стабильности!)
        for i in range(len(nums) - 1, -1, -1):
            digit = (nums[i] // exp) % 10
            # Находим позицию, куда должно встать число, и уменьшаем счетчик
            position = count[digit] - 1
            output[position] = nums[i]
            count[digit] -= 1

        return output

sol = Solution()
sol.maximumGap([3,6,9,1])
sol.maximumGap([10])
        