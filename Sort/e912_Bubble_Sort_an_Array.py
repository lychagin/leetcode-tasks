"""
912. Sort an Array
Ref: https://leetcode.com/problems/sort-an-array/description/

Given an array of integers nums, sort the array in ascending order and return it.
You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

Example 1:
----------
Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).

Example 2:
----------
Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
Explanation: Note that the values of nums are not necessarily unique.
 

Constraints:

1 <= nums.length <= 5 * 10^4
-5 * 10^4 <= nums[i] <= 5 * 10^4
"""
import time
import random
import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s | %(message)s")
logger = logging.getLogger(__name__)

class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        #result = bubble_sort(nums)
        #result = heap_sort(nums)
        #print(f"result: {result}")
        self.quick_sort(nums, 0, len(nums) - 1)
        logger.info(f"nums: {nums}")
        return nums

    def quick_sort(self, nums: list[int], low: int, high: int):
        # Базовый случай: если в подмассиве 0 или 1 элемент, сортировать нечего
        if low >= high:
            return
        
        # 1. Выбираем pivot (лучше брать случайный индекс между low и high!)
        pivot = nums[random.randint(low, high)]
        left = low
        right = high

        # 2. Цикл разделения (Partition) прямо здесь
        while left < right:
            # Двигаем левый указатель, пока элемент меньше pivot
            while nums[left] < pivot:
                left += 1
            
            # Двигаем правый указатель, пока элемент больше pivot
            while nums[right] > pivot:
                right -= 1 

            # Если указатели не пересеклись, меняем элементы местами
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        # 3. Рекурсивные вызовы для двух получившихся частей
        self.quick_sort(nums, low, right) # Сортируем левую часть
        self.quick_sort(nums, left, high) # Сортируем правую часть

def bubble_sort(nums: list[int]):
    n = len(nums)
    for i in range(n - 1):
        swapped = False
        # Последние i элементов уже на своих местах
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
        if not swapped:
            break
    return nums

def heap_sort(nums: list[int]):
    n = len(nums)

    # Вспомогательная функция просеивания вниз (БЕЗ РЕКУРСИИ)
    def sift_down_cycle(i, size, arr):
        """
        Просеивание вниз (sift-down) для max-heap в итеративном виде.
    
        Параметры:
            i      — индекс узла, с которого начинаем просеивание
            size   — текущий размер кучи (не весь массив, а активная часть)
            arr    — сам массив, в котором поддерживаем свойство кучи
    
        Работает «на месте»: меняет элементы в arr.
        """
        while i * 2 + 1 < size:
            left = 2 * i + 1
            right = 2* i + 2

            j = left
            # Выбираем большего ребёнка для max-heap
            if right < size and arr[right] > arr[left]:
                j = right
            
            # Если родитель уже больше или равен ребёнку — останавливаемся
            if arr[i] >= arr[j]:
                break

            arr[i], arr[j] = arr[j], arr[i]
            i = j

    # Вспомогательная функция просеивания вниз (РЕКУРСИВНАЯ)
    def sift_down_rec(i, size):
        largest = i
        left = i * 2 + 1
        right = i * 2 + 2

        if left < size and nums[left] > nums[largest]:
            largest = left
        if right < size and nums[right] > nums[largest]:
            largest = right

        if largest != i:
            nums[i], nums[largest] = nums[largest], nums[i]
            sift_down_rec(largest, size)

    # 1. Построить max-heap
    for i in range(n // 2 - 1, -1, -1):
        #sift_down_rec(i, n)
        sift_down_cycle(i, n, nums)

    # 2. Извлекать максимум и восстанавливать кучу
    for end in range(n - 1, 0, -1):
        nums[0], nums[end] = nums[end], nums[0]
        #sift_down_rec(0, end)
        sift_down_cycle(0, end, nums)

    return nums

sol = Solution()
start = time.perf_counter()
sol.sortArray([5,2,3,1])
end = time.perf_counter() - start
print(f"Run sort: {end:.4f}")