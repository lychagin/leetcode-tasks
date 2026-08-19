"""
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

- If the group's length is 1, append the character to s.
- Otherwise, append the character followed by the group's length.

The compressed string s should not be returned separately, but instead, be stored in the input character array chars. 
Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.

Note: The characters in the array beyond the returned length do not matter and should be ignored.

 

Example 1:
----------
Input: chars = ["a","a","b","b","c","c","c"]
Output: 6
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
After modifying the input array in-place, the first 6 characters of chars should be ["a","2","b","2","c","3"].

Example 2:
----------
Input: chars = ["a"]
Output: 1
Explanation: The only group is "a", which remains uncompressed since it is a single character.
After modifying the input array in-place, the first character of chars should be ["a"].

Example 3:
----------
Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: 4
Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".
After modifying the input array in-place, the first 4 characters of chars should be ["a","b","1","2"].
 

Constraints:

1 <= chars.length <= 2000
chars[i] is a lowercase English letter, uppercase English letter, digit, or symbol.
"""
class Solution:
    def compress(self, chars: list[str]) -> int:
        write_pos = 0
        group_count = 0
        symb_in_group = 1
        count = len (chars)
        #print(f"initial: {chars}; count={count}")
        print("-----------")
        for i in range(count):
            #print(f"char[{i}] = '{chars[i]}'")
            symb_current = chars[i]
            if i != count - 1:
                symb_next = chars[i+1]
                # chars = ["a","a","b","b","c","c","c"]
                if symb_current == symb_next:
                    symb_in_group += 1
                    continue
            group_count += 1
            chars[write_pos] = symb_current
            write_pos += 1
            if symb_in_group > 1:
                chr = list(str(symb_in_group))
                for j in range(len(chr)):
                    chars[write_pos] = chr[j]
                    write_pos += 1
            symb_in_group = 1
        print(f"chars: {chars}")

        return write_pos

sol = Solution()

chars = ["a","a","b","b","c","c","c"]
print(f"BEFORE: {chars}")
result = sol.compress(chars)
print(f"result={result}")
print(f"AFTER: {chars}")

chars = ["a"]
result = sol.compress(chars)
print(f"result={result}")