"""
https://leetcode.com/problems/range-sum-query-2d-immutable/description/

Given a 2D matrix matrix, handle multiple queries of the following type:

Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
Implement the NumMatrix class:

NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
You must design an algorithm where sumRegion works on O(1) time complexity.

 

Example 1:
+---+---+---+---+---+
| 3 | 0 | 1 | 4 | 2 |
+---+===+===+---+---+
| 5 ‖ 6 | 3 ‖ 2 | 1 |  <-- Зелёная [G]: (6,3,2,0)
+---+---#===+===+===+  <-- Синяя   [B]: (3,2,1,0,1,5)
| 1 ‖ 2 # 0 | 1 ‖ 5 |  <-- Красная [R]: (2,0,1,1,0,1,0,3,0)
+---+===#===+===+---+
| 4 ‖ 1 | 0 | 1 ‖ 7 |
+---+---+---+---+---+
| 1 ‖ 0 | 3 | 0 ‖ 5 |
+---+===+===+===+---+

Input
["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
[[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
Output
[null, 8, 11, 12]

Explanation
NumMatrix numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
numMatrix.sumRegion(2, 1, 4, 3); // return 8 (i.e sum of the red rectangle)
numMatrix.sumRegion(1, 1, 2, 2); // return 11 (i.e sum of the green rectangle)
numMatrix.sumRegion(1, 2, 2, 4); // return 12 (i.e sum of the blue rectangle)
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
-104 <= matrix[i][j] <= 104
0 <= row1 <= row2 < m
0 <= col1 <= col2 < n
At most 104 calls will be made to sumRegion.
"""
class NumMatrix:

    """
    Пример расчета начальной матрицы префиксной суммы.
    mat =  [ [1, 2, 3],
             [4, 5, 6],
             [7, 8, 9] ]
     
    perf = [ [1,   3,  6],
             [5,  12, 21],
             [12, 27, 45]]

    1. Первая строчка - считаем как обычно - нарастающим итогом.
        perf[0][0] = 1
        perf[0][1] = 1 + 2 = 3
        perf[0][2] = 3 + 3 = 6

    2. Крайний левый столбец новой строки: берем значение сверху - берем значение сверху (префиксной матрицы) + текущее значение изначальной матрицы
       perf[1][0] = 1 + 4 = 5

    3. Все оставшиеся столбцы считаем по формуле:
        - ячейка слева + ячейка сверку - ячейка по диагонали + ячейка исходной матрицы
       perf[1][1] = perf[1][0] + perf[0][1] - perf[0][0] + mat[1][1] = 5 + 3 - 1 + 5 = 12

       Общая формула: perf[i][j] = perf[i][j-1] + perf[i-1][j] - perf[i-1][j-1] + mat[i][j]


    """
    def __init__(self, matrix: list[list[int]]):
        self.int_mat = matrix
        row_size = len(self.int_mat)
        col_size = len(self.int_mat[0])
        self.perf = [[0] * col_size for _ in range(row_size)]
        for i in range(row_size):
            for j in range(col_size):
                up_cell = 0 if i == 0 else self.perf[i-1][j]
                left_cell = 0 if j == 0 else self.perf[i][j-1]
                if i == 0:
                    diag_cell = 0
                else:
                    diag_cell = 0 if j == 0 else self.perf[i-1][j-1]

                self.perf[i][j] = up_cell + left_cell - diag_cell + self.int_mat[i][j]
        printMatrix(self.perf)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        """
            Формула расчет суммы подматрицы:
            - Берем значение из перфиксной подматрицы - правый нижний угол
              current_cell = perf[row2][col2]
            - Дальше смотрим на верхний левый угол подматрицы 
            - up_cell = верхняя ячейка над правым углом
                up_cell = perf[row1 - 1][col2]
            - left_cell = левая ячейка на левым углом
                left_cell = perf[row2][col-1]
            - diag_cell = значение по диагонали влево вверх на левым верхним углом подматрицы
            sum = perf[row2][col2] - perf[row1-1][col2] - perf[row2][col1-1] + perf[row1-1][col1-1]
        """
        up = self.perf[row1 - 1][col2] if row1 > 0 else 0
        left = self.perf[row2][col1 - 1] if col1 > 0 else 0
        diag = self.perf[row1 - 1][col1 - 1] if row1 > 0 and col1 > 0 else 0
        return self.perf[row2][col2] - up - left + diag
        
def printMatrix(matrix: list[list[int]], matrixName: str = ""):
    print(f"-------{matrixName}--------")
    for i in range(len(matrix)):
        print(f"{matrix[i]}")
    print("---------------")

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# matrix = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
# #printMatrix(matrix, "Initial matrix")
# obj = NumMatrix(matrix)
# assert obj.sumRegion(2, 1, 4, 3) == 8
# assert obj.sumRegion(1, 1, 2, 2) == 11
# assert obj.sumRegion(1, 2, 2, 4) == 12

matrix2 = [[-1]]
printMatrix(matrix2, "Initial matrix")
obj2 = NumMatrix(matrix2)
result = obj2.sumRegion(0, 0, 0, 0)
print(f"result: {result}")
assert result == -1