""" 
    Given an integer x, return true if x is a palindrome, and false otherwise.

    Example 1:

    Input: x = 121
    Output: true
    Explanation: 121 reads as 121 from left to right and from right to left.
    
    Example 2:

    Input: x = -121
    Output: false
    Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
    
    Example 3:

    Input: x = 10
    Output: false
    Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

    Constraints:

    -231 <= x <= 231 - 1
 
    Follow up: Could you solve it without converting the integer to a string?
    
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
      
# The purpose of using templete is that we both need to operate with x and at the end we need to compare a given integer(x) with the inverse number.

        if x < 0:
            return False
        
        template = x                              #First loop, template=121
        reverse = 0                               #First loop, reverse=0
        while x > 0:                                                         #Second loop, x=12            Third loop, x=1
            digit = (x % 10)                      #First loop, digit=1        Second loop, digit=2         Third loop, digit=1
            reverse = (reverse * 10) + digit      #First loop, reverse=1      Second loop, reverse=12      Third loop, reverse=121
            x = x // 10                           #First loop, x=12           Second loop, x=1             Third loop, x=0
            
        if (template == reverse):                 
            return True
        else:
            return False
