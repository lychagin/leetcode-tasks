"""
Given two version strings, version1 and version2, compare them. 
A version string consists of revisions separated by dots '.'. 
The value of the revision is its integer conversion ignoring leading zeros.

To compare version strings, compare their revision values in left-to-right order. 
If one of the version strings has fewer revisions, treat the missing revision values as 0.

Return the following:

If version1 < version2, return -1.
If version1 > version2, return 1.
Otherwise, return 0.
 

Example 1:
----------
Input: version1 = "1.2", version2 = "1.10"

Output: -1

Explanation:

version1's second revision is "2" and version2's second revision is "10": 2 < 10, so version1 < version2.

Example 2:
----------
Input: version1 = "1.01", version2 = "1.001"

Output: 0

Explanation:

Ignoring leading zeroes, both "01" and "001" represent the same integer "1".

Example 3:
----------
Input: version1 = "1.0", version2 = "1.0.0.0"

Output: 0

Explanation:

version1 has less revisions, which means every missing revision are treated as "0".

 

Constraints:

1 <= version1.length, version2.length <= 500
version1 and version2 only contain digits and '.'.
version1 and version2 are valid version numbers.
All the given revisions in version1 and version2 can be stored in a 32-bit integer.
"""
class Solution:
    # мое решение
    def compareVersion(self, version1: str, version2: str) -> int:
        str_ver1 = version1.split('.')
        str_ver2 = version2.split('.')
        ver1_len = len(str_ver1)
        ver2_len = len(str_ver2)
        #ver_leader = []
        max_num = 0
        if ver1_len > ver2_len:
            max_num = ver1_len
            ver_leader = str_ver1
            ver_follower = str_ver2
            leader_type = "v1"
        else:
            max_num = ver2_len
            ver_leader = str_ver2
            ver_follower = str_ver1
            leader_type = "v2"

        for i in range(max_num):
            ver1 = int(ver_leader[i])
            if i >= len(ver_follower):
                ver2 = 0
            else:
                ver2 = int(ver_follower[i])
                
            if ver1 == ver2:
                pass
            elif ver1 > ver2:
                if leader_type == "v1":
                    return 1
                else:
                    return -1
            elif ver1 < ver2:
                if leader_type == "v1":
                    return -1
                else:
                    return 1

        return 0
    # Каноническое решение
    def compareVersion_orig(self, version1: str, version2: str) -> int:
        v1 = list(map(int, version1.split('.')))
        v2 = list(map(int, version2.split('.')))
        
        for a, b in zip(v1, v2):
            if a < b:
                return -1
            if a > b:
                return 1
        
        # Обработка разницы в длине — недостающие ревизии считаются как 0
        for num in v1[len(v2):]:
            if num:
                return 1
        for num in v2[len(v1):]:
            if num:
                return -1
        
        return 0
    # Каноническое оптимальное решение
    def compareVersion_orig_best(self, version1: str, version2: str) -> int:
        for a, b in zip_longest(
            map(int, version1.split('.')),
            map(int, version2.split('.')),
            fillvalue=0
        ):
            if a < b:
                return -1
            if a > b:
                return 1
        return 0

sol = Solution()

version1 = "7.5.2.4"
version2 = "7.5.3"
result = sol.compareVersion(version1, version2)
print(f"result: {result}")
assert result == -1

# version1 = "1.2"
# version2 = "1.10"
# result = sol.compareVersion(version1, version2)
# print(f"result: {result}")
# assert result == -1