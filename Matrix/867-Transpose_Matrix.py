"""
Given a 2D integer array matrix, return the transpose of matrix.
The transpose of a matrix is the matrix flipped over its main diagonal, 
switching the matrix's row and column indices.

Example 1:
----------
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]

Example 2:
----------
Input: matrix = [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 1000
1 <= m * n <= 105
-109 <= matrix[i][j] <= 109
"""
from zipfile import MAX_EXTRACT_VERSION


class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        row_count = len(matrix)
        col_count = len(matrix[0])
        result = []
        for i in range(col_count):
            result.append([0]*row_count)
        for i in range(len(matrix)):
            col_count = len(matrix[i])
            #result.append([0]*col_count)
            #print(f"i={i}; result: {result}; len(matrix[{i}])={len(matrix[i])}")
            for j in range(len(matrix[i])):
                #print(f"i={i}; j={j} [{matrix[j][i]}] |", end=" ")
                result[j][i] = matrix[i][j]
            #print()
        #print(f"IN : {matrix}")
        #print(f"OUT: {result}")
        return result

sol = Solution()

matrix = [[1,2,3],[4,5,6],[7,8,9]]
expected =  [[1,4,7],[2,5,8],[3,6,9]]
result = sol.transpose(matrix)
assert len(result) == len(expected)
for i in range(len(expected)):
    assert expected[i] == result[i]

matrix = [[1,2,3],[4,5,6]]
expected =  [[1,4],[2,5],[3,6]]
result = sol.transpose(matrix)
assert len(result) == len(expected)
for i in range(len(expected)):
    assert expected[i] == result[i]    