"""
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

 

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
"""

## Variant 1:
class Solution1:
    @staticmethod
    def reverseString(s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

print("Variant 1:")
str = ["h","e","l","l","o"]
solution = Solution1.reverseString(str)
print(f"Returned value (must be None): {solution}")
print(f"Reversed string: {str}")

## Variant 2:
class Solution2:
    @staticmethod
    def reverseString(s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        for i in range(n // 2):
            j = n - i - 1
            s[i], s[j] = s[j], s[i]

print("Variant 2:")
str = ["h","e","l","l","o"]
solution = Solution2.reverseString(str)
print(f"Returned value (must be None): {solution}")
print(f"Reversed string: {str}")

## Variant 3:
class Solution:
    def reverseString(self, s: list[str]) -> None:
        def helper(left: int, right: int) -> None:
            if left >= right:
                return
            s[left], s[right] = s[right], s[left]
            helper(left + 1, right - 1)

        helper(0, len(s) - 1)

print("Variant 3:")
str = ["h","e","l","l","o"]
solution = Solution()
print(f"Returned value (must be None): {solution.reverseString(str)}")
print(f"Reversed string: {str}")