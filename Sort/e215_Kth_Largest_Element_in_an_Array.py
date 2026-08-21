"""
215. Kth Largest Element in an Array
Ref: https://leetcode.com/problems/kth-largest-element-in-an-array/description/

Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
Can you solve it without sorting?

Example 1:
----------
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
----------
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
 

Constraints:
------------
1 <= k <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
"""
import logging
import random
import time

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s | %(message)s")
logger = logging.getLogger(__name__)

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        logger.debug(f"nums: {nums}, k: {k}")
        # Целевой индекс в отсортированном по возрастанию массиве
        target = len(nums) - k

        def quick_select(left: int, right: int) -> int:
            # Базовый случай: если в подмассиве один элемент, это наш ответ
            if left == right:
                return nums[left]

            # Схема Хоара возвращает индекс границы, а не точную позицию пивота
            # partition вызывается ТОЛЬКО для массивов длиной >= 2
            pivot_idx = self.partition(nums, left, right)

            # Шаг 2: Сравниваем с целевым индексом
            if target <= pivot_idx:
                return quick_select(left, pivot_idx) # Ищем в левой группе [left...j]
            else:
                return quick_select(pivot_idx + 1, right)  # Ищем в правой группе [j+1...right]

        return quick_select(0, len(nums) - 1)

    def partition(self, nums: list[int], left: int, right: int) -> int:
        # Случайный выбор опорного элемента
        pivot_idx = random.randint(left, right)
        pivot = nums[pivot_idx]
        
        # Встречные указатели выходят за границы на 1 шаг для корректного цикла do-while
        i = left - 1
        j = right + 1
        
        while True:
            # Двигаем левый указатель, пока элементы меньше pivot
            i += 1
            while nums[i] < pivot:
                i += 1
                
            # Двигаем правый указатель, пока элементы больше pivot
            j -= 1
            while nums[j] > pivot:
                j -= 1
                
            # Если указатели встретились или пересеклись
            if i >= j:
                return j
                
            # Меняем элементы местами, если они стоят не в своих половинах
            nums[i], nums[j] = nums[j], nums[i]        


"""
    Фунция partition написанная по схеме Ломуто
    Решение не прошло на leetcode из-за Time Limit Exceeded
    Нужно использовать схему разделения Хоара

    def partition(self, nums: list[int], left: int, right: int) -> int:
        pivot_idx = random.randint(left, right)
        pivot = nums[pivot_idx]

        nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
        # Сдвигаем все элементы, которые меньше pivot, налево
        store_idx = left
        for i in range(left, right):
            if nums[i] < pivot:
                nums[i], nums[store_idx] = nums[store_idx], nums[i]
                store_idx += 1
                
        # Возвращаем pivot на его законное место
        nums[store_idx], nums[right] = nums[right], nums[store_idx]
        return store_idx
"""

start = time.perf_counter()
sol = Solution()
res = sol.findKthLargest([3,2,1,5,6,4], 2)
end = time.perf_counter() - start
logger.info(f"res: {res}")
logger.info(f"Duration: {end:.4f}")

