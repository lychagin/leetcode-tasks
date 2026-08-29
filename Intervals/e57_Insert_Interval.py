"""
Name: 57. Insert Interval
Ref: https://leetcode.com/problems/insert-interval/description/

You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval 
and intervals is sorted in ascending order by starti. 
You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
Two intervals are considered overlapping if they share at least one point.

Insert newInterval into intervals such that intervals is still sorted in ascending order 
by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.

 

Example 1:
----------
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
----------
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
 

Constraints:
------------
0 <= intervals.length <= 10^4
intervals[i].length == 2
0 <= starti <= endi <= 10^5
intervals is sorted by starti in ascending order.
newInterval.length == 2
0 <= start <= end <= 10^5
"""
import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s | %(message)s")
logger = logging.getLogger(__name__)

class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        if not intervals:
            return []

        first_range = []
        last_range = []

        # Переменные для сборки одного общего среднего интервала
        new_start = newInterval[0]
        new_end = newInterval[1]

        for item in intervals:
            if item[1] < new_start:
                # Полностью слева от нового
                first_range.append(item)
            elif item[0] > new_end:
                last_range.append(item)
            else:
                # Есть пересечение — расширяем границы нового интервала
                new_start = min(new_start, item[0])
                new_end = max(new_end, item[1])
        
        return first_range + [[new_start, new_end]] + last_range

sol = Solution()
intervals = [[1,3],[6,9]]
newInterval = [2,5]
result1 = [[1,5],[6,9]]
res = sol.insert(intervals, newInterval)
print(f"result: {res}")
        