"""
Given a square matrix mat, return the sum of the matrix diagonals.
Only include the sum of all the elements on the primary diagonal and 
all the elements on the secondary diagonal that are not part of the primary diagonal.

 

Example 1:
----------

Input: mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]
Output: 25
Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
Notice that element mat[1][1] = 5 is counted only once.

Example 2:
----------
Input: mat = [[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]
Output: 8

Example 3:
----------
Input: mat = [[5]]
Output: 5
 

Constraints:

n == mat.length == mat[i].length
1 <= n <= 100
1 <= mat[i][j] <= 100
"""
from math import exp


class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        msize = len(mat)
        main_sum = 0
        secondary_sum = 0
        for i in range(msize):
            #print(f"i: {i}; mat[i]={mat[i]}")
            main_sum += mat[i][i]
            secondary_sum += mat[i][msize - 1 - i]
        #print(f"main_sum: {main_sum}")
        #print(f"secondary_sum: {secondary_sum}")
        if (msize % 2 == 0):
            center_value = 0
        else:
            center_mat = msize // 2
            center_value = mat[center_mat][center_mat]
        #print(f"center val: {center_value}")
        result = main_sum + secondary_sum - center_value
        #print(f"result: {result}")

        return result


sol = Solution()

mat = [[1,2,3],
       [4,5,6],
       [7,8,9]]
expected = 25
result = sol.diagonalSum(mat)
assert result == expected

mat = [[1,1,1,1],
       [1,1,1,1],
       [1,1,1,1],
       [1,1,1,1]]
expected = 8
result = sol.diagonalSum(mat)
assert result == expected