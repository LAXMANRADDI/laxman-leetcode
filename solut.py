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

