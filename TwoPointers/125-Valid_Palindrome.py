class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_clean = "".join(symb for symb in s if symb.isalnum()).lower()
        r_clean = s_clean[::-1]

        return s_clean == r_clean

s = "A man, a plan, a canal: Panama"
s2 = " "
sol = Solution()
print(f"Result: {sol.isPalindrome(s2)}")