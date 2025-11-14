1] roman to intger conversion :


Approach
*]Create a dictionary of Roman numeral values.
*]Loop through the string.
*]If the current symbol is less than the next symbol, subtract it.
*]Otherwise, add it.
*] works because Roman subtractive combinations follow patterns (like IV, IX, XL, XC, CM)


class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        for i in range(len(s)):
            # If next value is larger, subtract current value
            if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
                total -= roman[s[i]]
            else:
                total += roman[s[i]]
        
        return total
input :   s = "MCMXCIV"

output :  1994


2] Given an array of strings, find the longest common prefix among all strings. If there is no common prefix, return "". 
 *]]Approach (Horizontal Scanning — Fast & Simple)
Assume the first string is the prefix.
Compare it with each next string.
Shrink the prefix until it matches the start of each string.
Return the final prefix.


class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        prefix = strs[0]  # assume prefix is whole first string
        
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]  # shrink prefix
                if not prefix:
                    return ""
        
        return prefix
input :: ["flower","flow","flight"]
output :: "fl"


3]] valid paranthesis::
Push opening brackets to a stack .
When a closing bracket appears, check if it matches the top of the stack.

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}
        
        for char in s:
            if char in pairs:
                if not stack or stack[-1] != pairs[char]:
                    return False
                stack.pop()  # match found, remove opening
            else:
                stack.append(char)  # opening bracket
        return len(stack) == 0

input :"()"
output : true
