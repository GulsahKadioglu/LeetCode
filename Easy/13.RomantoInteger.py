"""
    Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

    Symbol       Value
    I             1
    V             5
    X             10
    L             50
    C             100
    D             500
    M             1000
    
    For example, 2 is written as II in Roman numeral, just two ones added together.
    12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

    Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII.
    Instead, the number four is written as IV. Because the one is before the five we subtract it making four.
    The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9. 
    X can be placed before L (50) and C (100) to make 40 and 90. 
    C can be placed before D (500) and M (1000) to make 400 and 900.
    
    Given a roman numeral, convert it to an integer.

    Example 1:

    Input: s = "III"
    Output: 3
    Explanation: III = 3.
    
    Example 2:

    Input: s = "LVIII"
    Output: 58
    Explanation: L = 50, V= 5, III = 3.
    
    Example 3:

    Input: s = "MCMXCIV"
    Output: 1994
    Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

    Constraints:

    1 <= s.length <= 15
    s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
    It is guaranteed that s is a valid roman numeral in the range [1, 3999].
    
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        
# The corresponding Roman numeral letter is defined in a dictionary.
        
        r= {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
# A variable named 'result' is defined for the function to run.

        result = 0
       
# The loop runs for each character.
# If a character has a value less than the character after it,
# that character's value is subtracted; otherwise, its value is appended.
# As a result, the variable result will contain the decimal value of the Roman numeral equivalent in the string when the loop is complete.
# i+1 for the last character of s cannot be checked because it exceeds the index range of s,
# so r[s[i]] for the last character is added directly to the result.

        for i in range (len(s)):
            if i + 1 < len(s) and r[s[i]] < r[s[i + 1]]:
                result = result - r[s[i]]
            else:
                result = result + r[s[i]]
        return result
