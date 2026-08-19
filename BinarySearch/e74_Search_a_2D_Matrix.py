"""
You are given an 'm x n' integer matrix 'matrix' with the following two properties:
 - Each row is sorted in non-decreasing order.
 - The first integer of each row is greater than the last integer of the previous row.
Given an integer 'target', return 'true' if 'target' is in 'matrix' or 'false' otherwise.

You must write a solution in O(log(m * n)) time complexity.

Example 1:
+----+----+----+----+
|  1 |  3 |  5 |  7 |
+----+----+----+----+
| 10 | 11 | 16 | 20 |
+----+----+----+----+
| 23 | 30 | 34 | 60 |
+----+----+----+----+

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
+----+----+----+----+
|  1 |  3 |  5 |  7 |
+----+----+----+----+
| 10 | 11 | 16 | 20 |
+----+----+----+----+
| 23 | 30 | 34 | 60 |
+----+----+----+----+

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-10^4 <= matrix[i][j], target <= 10^4
"""
import logging
import time

logging.basicConfig(level=logging.INFO, format="%(levelname)s | %(message)s", force=True)
logger = logging.getLogger(__name__)

class Solution:
    # Каноническое решение
    def searchMatrixCanon(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        m, n = len(matrix), len(matrix[0])
        left, right = 0, (m * n) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            # Магия превращения одномерного индекса в координаты матрицы:
            """
                        Столбец 0    Столбец 1    Столбец 2    Столбец 3
            Строка 0:      [0]          [1]          [2]          [3]
            Строка 1:      [4]          [5]          [6]          [7]
            Строка 2:      [8]          [9]         [10]         [11]

            1. Номер строки (row = mid // n): 6 // 4 = 1

            Целочисленное деление показывает, сколько полных строк мы уже «перешагнули». 
            В число 6 помещается ровно одна полная строка из 4 элементов

            2. Номер столбца (col = mid % n): 6 % 4 = 2

            Остаток от деления показывает, на сколько элементов мы продвинулись в текущей строке после последней «границы»

            Универсальное правило:
              mid // n — отвечает на вопрос: «В какую по счету строку мы попали?»
              mid % n — отвечает на вопрос: «На каком шаге внутри этой строки мы остановились?»
            """

            row = mid // n  # Номер строки — сколько полных строк поместилось в mid
            col = mid % n   # Номер столбца — остаток от деления
            
            val = matrix[row][col]
            
            if val == target:
                return True
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return False
    # моё решение
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        def findRow(target: int) -> int:
            left, right = 0, len(matrix) - 1
            colMax = len(matrix[0]) - 1
            while left <= right:
                mid = left + ((right - left) // 2)
                firstCol = matrix[mid][0]
                lastCol = matrix[mid][colMax]
                if firstCol <= target and lastCol >= target:
                    return mid
                elif firstCol > target:
                    right = mid - 1
                elif lastCol < target:
                    left = mid + 1
            return -1

        def findCol(row: int, target: int) -> bool:
            left, right = 0, len(matrix[0]) - 1
            while left <= right:
                mid = left + ((right - left) // 2)
                val = matrix[row][mid]
                if val == target: 
                    return True
                elif val < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return False

        targetRow = findRow(target)
        if targetRow == -1: return False
        
        return findCol(targetRow, target)

sol = Solution()
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
start = time.perf_counter()
result = sol.searchMatrix(matrix, target)
print(f"result: {result}")
end = time.perf_counter() - start
print(f"Total time: {end:.4f} sec")