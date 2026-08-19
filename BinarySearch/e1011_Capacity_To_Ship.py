"""
Task: 1011. Capacity To Ship Packages Within D Days
Ref: https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/

A conveyor belt has packages that must be shipped from one port to another within days days.
The 1st package on the conveyor belt has a weight of 'weights[i]'. 
Each day, we load the ship with packages on the conveyor belt (in the order given by weights). 
We may not load more weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within 'days' days.

Example 1:
---------
Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
Output: 15
Explanation: A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
1st day: 1, 2, 3, 4, 5
2nd day: 6, 7
3rd day: 8
4th day: 9
5th day: 10

Note that the cargo must be shipped in the order given, so using a ship of capacity 14 
and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.

Example 2:
----------
Input: weights = [3,2,2,4,1,4], days = 3
Output: 6
Explanation: A ship capacity of 6 is the minimum to ship all the packages in 3 days like this:
1st day: 3, 2
2nd day: 2, 4
3rd day: 1, 4

Example 3:
----------
Input: weights = [1,2,3,1,1], days = 4
Output: 3
Explanation:
1st day: 1
2nd day: 2
3rd day: 3
4th day: 1, 1
 

Constraints:
------------
1 <= days <= weights.length <= 5 * 10^4
1 <= weights[i] <= 500
"""
import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        # weights = [1,2,3,4,5,6,7,8,9,10], days = 5, output = 15
        # (1 + 2 + 3 + ...) <= 15
        min_capacity = max_capacity = 0
        max_capacity = 0
        for i in weights:
            min_capacity = max(min_capacity, i)
            max_capacity += i

        # left = 10, right = 55
        # [10, 11, 12, ... 52, 53, 54, 55]
        left, right = min_capacity, max_capacity
        while left <= right:
            # mid = 22
            mid = left + ((right - left) // 2)
            intermediate_sum = 0
            turns = 1
            for i in weights:
                intermediate_sum += i
                if intermediate_sum > mid:
                    intermediate_sum = i
                    turns += 1

            if turns > days:
                left = mid + 1
            else:
                right = mid - 1

        #logger.info(f"left: {left}")
        return left

# sol = Solution()
# sol.shipWithinDays([1,2,3,4,5,6,7,8,9,10], 5)