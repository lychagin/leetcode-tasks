"""
451. Sort Characters By Frequency
Ref: https://leetcode.com/problems/sort-characters-by-frequency/description/?envType=problem-list-v2&envId=sorting

Given a string s, sort it in decreasing order based on the frequency of the characters. 
The frequency of a character is the number of times it appears in the string.
Return the sorted string. If there are multiple answers, return any of them.

Example 1:
==========
Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

Example 2:
==========
Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
Note that "cacaca" is incorrect, as the same characters must be together.

Example 3:
==========
Input: s = "Aabb"
Output: "bbAa"
Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
 

Constraints:

1 <= s.length <= 5 * 10^5
s consists of uppercase and lowercase English letters and digits.
"""
import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s | %(message)s", force=True)
logger = logging.getLogger(__name__)

class Solution:
    def frequencySort(self, s: str) -> str:
        result = self.TimSort(s)
        #result = self.BucketSort(s)
        return result

    def BucketSort(self, s: str) -> str:
        count_dict = {}
        for ch in s:
            count_dict[ch] = count_dict.get(ch, 0) + 1
        buckets = [[] for _ in range(len(s) + 1)]
        #logger.debug(f"buckets: {buckets}")

        for ch, freq in count_dict.items():
            buckets[freq].append(ch)
        #logger.debug(f"buckets: {buckets}")

        result_list = []
        for i in range(len(buckets) - 1, -1, -1):
            for ch in buckets[i]:
                result_list.append(ch * i)
        return ''.join(result_list)

    def TimSort(self, s:str) -> str:
        # Реализуем сортировку по алгоритиу TimSort
        count_dict = {}
        for ch in s:
            count_dict[ch] = count_dict.get(ch, 0) + 1
        #logger.debug(f"count_dict: {count_dict}")

        unique_chars = sorted(count_dict.keys(), key=lambda ch: count_dict[ch], reverse=True)
        return ''.join(ch * count_dict[ch] for ch in unique_chars)


sol = Solution()
res = sol.frequencySort("tree")
logger.debug(f"Final string: {res}")