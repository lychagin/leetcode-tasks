"""
2418. Sort the People
Ref: https://leetcode.com/problems/sort-the-people/description/

You are given an array of strings names, and an array heights that consists of distinct positive integers. Both arrays are of length n.
For each index i, names[i] and heights[i] denote the name and height of the ith person.
Return names sorted in descending order by the people's heights.

Example 1:
----------
Input: names = ["Mary","John","Emma"], heights = [180,165,170]
Output: ["Mary","Emma","John"]
Explanation: Mary is the tallest, followed by Emma and John.

Example 2:
----------
Input: names = ["Alice","Bob","Bob"], heights = [155,185,150]
Output: ["Bob","Alice","Bob"]
Explanation: The first Bob is the tallest, followed by Alice and the second Bob.

Constraints:

n == names.length == heights.length
1 <= n <= 103
1 <= names[i].length <= 20
1 <= heights[i] <= 105

names[i] consists of lower and upper case English letters.
All the values of heights are distinct.
"""
import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s | %(message)s", force=True)
logger = logging.getLogger(__name__)

class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        #return self.myFirstSolution(names, heights)
        return self.selectionSort(names, heights)

    def myFirstSolution(self, names: list[str], heights: list[int]) -> list[str]:
        peoples = list(zip(names, heights))
        peoples.sort(key=lambda item: item[1], reverse=True)
        #return list(map(lambda x: x[0], peoples))
        return [item[0] for item in peoples]

    def selectionSort(self, names: list[str], heights: list[int]) -> list[str]:
        n = len(heights)
        names, heights = list(names), list(heights)
        for i in range(n - 1):
            max_idx = i                          # ищем максимум в неотсортированной части
            for j in range(i + 1, n):
                if heights[j] > heights[max_idx]:
                    max_idx = j
            if max_idx != i:                     # ставим его в начало этой части
                heights[i], heights[max_idx] = heights[max_idx], heights[i]
                names[i], names[max_idx] = names[max_idx], names[i]
        return names

names = ["Mary","John","Emma"]
heights = [180,165,170]
sol = Solution()
res = sol.sortPeople(names, heights)
logger.debug(f"res = {res}")
        