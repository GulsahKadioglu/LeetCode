"""
    You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check.
    
    Since each version is developed based on the previous version, all the versions after a bad version are also bad.
    
    Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.
    
    You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version.
    
    You should minimize the number of calls to the API.

    Example 1:

    Input: n = 5, bad = 4
    Output: 4
    Explanation:
    call isBadVersion(3) -> false
    call isBadVersion(5) -> true
    call isBadVersion(4) -> true
    Then 4 is the first bad version.
    
    Example 2:

    Input: n = 1, bad = 1
    Output: 1
 
    Constraints:
    1 <= bad <= n <= 231 - 1
   
"""

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
    
# We can use the binary search method(if we know the integer in the middle of the array we can compare this with isBadVersion(version))
# If the right and left integers are smaller/bigger than the isBadVersion(version), we can limit the integers of the array with new right(r) and left(l) integers

        l = 0
        r = n
        while l < r:
              m = l + (r-l) // 2
              if isBadVersion(m):
                 r = m
              else:
                 l = m + 1
        return l
