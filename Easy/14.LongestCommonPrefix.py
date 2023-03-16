"""
    Write a function to find the longest common prefix string amongst an array of strings.

    If there is no common prefix, return an empty string "".

    Example 1:

    Input: strs = ["flower","flow","flight"]
    Output: "fl"
    
    Example 2:

    Input: strs = ["dog","racecar","car"]
    Output: ""
    Explanation: There is no common prefix among the input strings.
 
    Constraints:

    1 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] consists of only lowercase English letters.7
    
"""
class Solution:                                               # It creates a class named "Solution". This class will contain our solution.
    def longestCommonPrefix(self, strs: List[str]) -> str:    # This class contain a function named "longestCommonPrefix".
 
# The "self" parameter is used to indicate that this function is a method.
# The function takes a "strs" parameter of type "List[str]" and returns a "str" value.

        result=""  # An empty string named "result". This string will hold the result of finding the longest common prefix.
       
# Loops a variable named "i" for the length of the string "strs[0]".        
        
        for i in range(len(strs[0])):                  # This will be used to check each character individually to find the longest common prefix.
            for s in strs:                             # It creates a loop for each string in the list named "strs".
                if i==len(s) or s[i]!==strs[0][i]:     # Returns the string "result" if the variable "i" is equal to the length of the string "s" or
                    return result                      # the character "s[i]" is not equal to the character "strs[0][i]", that is, if the longest common
                result=result+strs[0][i]               # prefix is not found. Otherwise, the character "strs[0][i]"(at index i of the first string in the list "strs")
        return result                                  # is add to the "result" string.
    
    # This returns the result string, which is the longest common prefix among the strings in the list strs.
