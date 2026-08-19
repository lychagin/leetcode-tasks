"""
Ref: 191. Number of 1 Bits: https://leetcode.com/problems/number-of-1-bits/description/?envType=problem-list-v2&envId=bit-manipulation

Given a positive integer n, write a function that returns 
the number of set bits in its binary representation (also known as the Hamming weight).

 

Example 1:
----------
Input: n = 11
Output: 3
Explanation:
    The input binary string 1011 has a total of three set bits.

Example 2:
----------
Input: n = 128
Output: 1
Explanation:
    The input binary string 10000000 has a total of one set bit.

Example 3:
----------
Input: n = 2147483645
Output: 30
Explanation:
    The input binary string 1111111111111111111111111111101 has a total of thirty set bits.

Constraints:
    1 <= n <= 231 - 1
 
Follow up: If this function is called many times, how would you optimize it?
"""
import time

class Solution:
    def hammingWeight_str(self, n: int) -> int:
        return bin(n & 0xFFFFFFFF).count('1')
    
    def hammingWeight_bit(self, n: int) -> int:
        count = 0
        x = n & 0xFFFFFFFF
        while x:
            x &= x - 1
            count += 1
        return count

    def hammingWeight_bit_count(self, n: int) -> int:
        return (n & 0xFFFFFFFF).bit_count()

sol = Solution()

start = time.perf_counter()
for _ in range(1_000_000):
    sol.hammingWeight_str(2147483645)
str_end = time.perf_counter() - start
print(f"Str: {str_end:.4f} sec")

start = time.perf_counter()
for _ in range(1_000_000):
    sol.hammingWeight_bit(2147483645)
bit_end = time.perf_counter() - start
print(f"Bit: {bit_end:.4f} sec")

start = time.perf_counter()
for _ in range(1_000_000):
    sol.hammingWeight_bit_count(2147483645)
bit_end = time.perf_counter() - start
print(f"Bit count: {bit_end:.4f} sec")


# print("TEST 1")
# assert sol.hammingWeight(11) == 3

# print("TEST 2")
# assert sol.hammingWeight(128) == 1

# print("TEST 3")
# assert sol.hammingWeight(2147483645) == 30
