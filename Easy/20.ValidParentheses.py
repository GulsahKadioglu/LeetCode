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
     
# We will check if a given string is a valid parenthesis string.
# O(n) because we're only having to go through every input character once.
     
    stack = []
    d = { ")" : "(", "]" : "[" , "}" : "{" }
    
    for c in s:                                 # The loop to assign each character of array named s in turn to 'c'.
        if c in d:                              # Checks if the 'c' is in the 'd' dictionary. If not, it will skip processing and continue processing other characters.
           if stack and stack[-1] == d[c]:      # Checks whether the last element of the 'stack' list corresponds to the opening parenthesis in the 'd' dictionary.
              stack.pop()                       # If so, it removes the last element from the list with the pop() method.
           else:                                # Otherwise, it returns False.
              return False
           else:
               stack.append(c)                  # If the 'c' is not in the 'd' dictionary, it adds it to the 'stack' list.
     return True if not stack else False
