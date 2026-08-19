"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
Example 2:

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
 

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.
"""
from asyncio import FastChildWatcher
from unittest import result


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        row_num = len(board)
        col_num = len(board)
        transp_board = [[0]*row_num for _ in range(col_num)]
        s3_boxes = {i : [] for i in range(row_num)}
        print(f"s3_boxes: {s3_boxes}")
        print(f"transp_board: {transp_board}")
        for i in range(row_num):
            if self.is_not_unique(board[i], f"Row {i} invalid"): return False

            for j in range(col_num):
                value = board[i][j]
                transp_board[j][i] = value
                i_index = i // 3
                j_index = j // 3
                index = i_index * 3 + j_index
                s3_boxes[index].append(value)

        print(f"S3 boxes length: {len(s3_boxes)}")
        for idx in range(len(s3_boxes)):
            print(f"S3 box [{idx}]: {s3_boxes[idx]}")
            if self.is_not_unique(s3_boxes[idx], f"S3 box {idx} is invalid"):
                return False
        for i in range(col_num):
            if self.is_not_unique(transp_board[i], f"Column {i} invalid"):
                return False

        return True
    
    def is_not_unique(self, input_str: str, err_msg: str) -> bool:
        result = False
        clean_line = "".join(filter(str.isdigit, input_str))
        orig_count = len(clean_line)
        unique_count = len(set(clean_line))
        if orig_count != unique_count:
            result = True
            print(err_msg)
        return result

sol = Solution()

#print("Test 1\n")
board = [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
expected = True
assert sol.isValidSudoku(board) == expected

#print("Test 2\n")
board = [["8","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
expected = False
assert sol.isValidSudoku(board) == expected