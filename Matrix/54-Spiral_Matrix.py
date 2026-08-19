"""
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
----------
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
----------
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""
from doctest import master


class Solution:
    def print_matrix(self, matrix: list[list[int]]) -> None:
        num_rows = len(matrix)
        for i in range(num_rows):
            print(f"{matrix[i]}]")

    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        msize = len(matrix)
        nsize = len(matrix[0])
        result = []

        """
        i=0, j=0(1), 1(2), 2(3)
        i=0+1(6), 2(9), j=0
        i=msize, i=0+1(8), 7 

        """
        top = 0
        bottom = msize 
        left = 0
        right = nsize
        stop = False

        #print(f"Initial matrix:")
        self.print_matrix(matrix)
        # спираль - 4 шага:
        # - слева направо
        # - сверху вниз
        # - справа налево
        # - снизу вверх
        while not stop:
            # Вправо
            i = left
            while i < right:
                result.append(matrix[top][i])
                i +=1
            top += 1
            # Вниз
            i = top
            while i < bottom:
                result.append(matrix[i][right-1])
                i +=1
            right -= 1
            # Проверка после "вниз"
            if top >= bottom:
                stop = True
                break
            # Влево
            i = right - 1
            while i >= left:
                result.append(matrix[bottom-1][i])
                i -= 1
            bottom -= 1
            # Проверка после "влево"
            if left >= right:
                stop = True
                break
            # Вверх
            i = bottom - 1
            while i >= top:
                result.append(matrix[i][left])
                i -=1
            left += 1
            # Проверка после "вверх"
            if left >= right or top >= bottom:
                stop = True

        #print(f"result: {result}")           
            
        return result

sol = Solution()

print(f"TEST 1")
matrix = [[1,2,3],[4,5,6],[7,8,9]]
expected = [1,2,3,6,9,8,7,4,5]
result = sol.spiralOrder(matrix)
assert result == expected

print(f"TEST 2")
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
expected = [1,2,3,4,8,12,11,10,9,5,6,7]
result = sol.spiralOrder(matrix)
assert result == expected

print(f"TEST 3")
matrix = [[2,5,8],[4,0,-1]]
expected = [2,5,8,-1,0,4]
result = sol.spiralOrder(matrix)
# wrong output/result = [2,5,8,-1,0,4,0]
assert result == expected