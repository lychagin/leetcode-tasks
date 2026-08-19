"""
Link: https://leetcode.com/problems/rotate-image/description/?envType=problem-list-v2&envId=matrix

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
DO NOT allocate another 2D matrix and do the rotation.

Example 1:
----------
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:
----------
Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000
"""
class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #self.print_matrix(matrix)
        # Делаем подход: Транспонирование матрицы + переворот строки
        msize = len(matrix)
        # сначала делаем транспонирование
        for i in range(msize):
            for j in range(msize):
                if j > i:
                    matrix[j][i], matrix[i][j] = (matrix[i][j], matrix[j][i])
            # Тут же после обработки строки можем ее сразу же развернуть
        #print(f"AFTER: matrix:")        
        #self.print_matrix(matrix)
        for i in range(msize):
            left = 0
            right = msize - 1
            while left < right:
                matrix[i][left], matrix[i][right] = (matrix[i][right], matrix[i][left])
                left += 1
                right -= 1
        #print(f"FINAL: matrix:")        
        #self.print_matrix(matrix)

    def print_matrix(self, mat: list[list[int]]) -> None:
        for i in range(len(mat)):
            print(f"{mat[i]}")

sol = Solution()

print("TEST 1")
matrix = [[1,2,3],[4,5,6],[7,8,9]]
expected = [[7,4,1],[8,5,2],[9,6,3]]
sol.rotate(matrix)
assert matrix == expected

print("TEST 2")
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
expected = [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
sol.rotate(matrix)
assert matrix == expected