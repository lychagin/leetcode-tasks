"""
347. Top K Frequent Elements
Ref: https://leetcode.com/problems/top-k-frequent-elements/description/?envType=problem-list-v2&envId=sorting

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.


Example 1:
----------
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
----------
Input: nums = [1], k = 1
Output: [1]

Example 3:
----------
Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2
Output: [1,2]


Constraints:
------------
1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4

k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 
Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""
import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s | %(message)s", force=True)
logger = logging.getLogger(__name__)

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # вначале подсчитываем частоты чисел
        freqDict: dict = {}
        for i in nums:
            freqDict[i] = freqDict.get(i, 0) + 1
        #logger.debug(f"freqDict: {freqDict}")

        # раскладываем частоты по "карманам"
        buckets = [[] for _ in range(len(nums) + 1)]
        #logger.debug(f"buckets (brfore): {buckets}")
        for key, val in freqDict.items():
            #logger.debug(f"key: {key}, val: {val}")
            buckets[val].append(key)
        
        #logger.debug(f"buckets (after): {buckets}")

        result = []
        buckLen = len(buckets)
        # собираем k наиболее часто встречающихся числе
        for i in range(buckLen - 1, -1, -1):
            for j in buckets[i]:
                result.append(j)
                if len(result) == k:
                    #logger.debug(f"result: {result}")
                    return result
      
        return result

sol = Solution()
#sol.topKFrequent([1,1,1,2,2,3], 2)
sol.topKFrequent([1,2,1,2,1,2,3,1,3,2], 2)