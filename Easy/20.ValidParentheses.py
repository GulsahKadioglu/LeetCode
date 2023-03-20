""""
     Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

     An input string is valid if:
     Open brackets must be closed by the same type of brackets.
     Open brackets must be closed in the correct order.
     Every close bracket has a corresponding open bracket of the same type.

     Example 1:

     Input: s = "()"
     Output: true
     
     Example 2:

     Input: s = "()[]{}"
     Output: true
     
     Example 3:

     Input: s = "(]"
     Output: false
 
     Constraints:

     1 <= s.length <= 104
     s consists of parentheses only '()[]{}'.
     
"""
class Solution:
    def isValid(self, s: str) -> bool:
     
# O(n) because we're only having to go through every input character once.
     
    stack = []
    p = { ")" : "(", "]" : "[" , "}" : "{" }
    
    for c in s:
        if c in p:
           if stack and stack[-1] == p[c]:
              stack.pop()
           else:
              return False
           else:
               stack.append(c)
     return True if not stack else False
