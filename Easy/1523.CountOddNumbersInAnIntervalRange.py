"""
    Given two non-negative integers low and high. Return the count of odd 
    numbers between low and high (inclusive).
    
    Example:
    Input: low = 3, high = 7
    Output: 3
    Explanation: The odd numbers between 3 and 7 are [3,5,7].
    
    Constraints:
        - 0 <= low <= high <= 10^9
"""
class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        if high%2==0 and low%2==0:
          return (high-low)/2
        else:
            return (high-low)/2+1
