"""
    Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

    answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
    answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
    Note that the integers in the lists may be returned in any order.

    Example 1:

    Input: nums1 = [1,2,3], nums2 = [2,4,6]
    Output: [[1,3],[4,6]]
    Explanation:
    For nums1, nums1[1] = 2 is present at index 0 of nums2, whereas nums1[0] = 1 and nums1[2] = 3 are not present in nums2. Therefore, answer[0] = [1,3].
    For nums2, nums2[0] = 2 is present at index 1 of nums1, whereas nums2[1] = 4 and nums2[2] = 6 are not present in nums2. Therefore, answer[1] = [4,6].
    
    Example 2:

    Input: nums1 = [1,2,3,3], nums2 = [1,1,2,2]
    Output: [[3],[]]
    Explanation:
    For nums1, nums1[2] and nums1[3] are not present in nums2. Since nums1[2] == nums1[3], their value is only included once and answer[0] = [3].
    Every integer in nums2 is present in nums1. Therefore, answer[1] = [].
 

    Constraints:
  
    1 <= nums1.length, nums2.length <= 1000
    -1000 <= nums1[i], nums2[i] <= 1000
    
"""

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
# Big-O notation describes the limiting behavior of a function when the argument tends towards a particular value or infinity.
# It is used to classify algorithms by how their runtime or space requirements grow as the input size (n) grows.
# Big-O is a concept used to calculate how fast the algorithm works and to evaluate the efficiency of the algorithm.
# All of the operations in the problem have O(n) time complexity because each list element will be visited only once.

# Sets are collections of unique elements, meaning that they can't have duplicates. 
# This property makes sets useful in efficiently removing duplicate values from a list or tuple by converting them to a set and then back to a list or tuple. 

        num1, num2 = set(nums1), set(nums2)
        return [num1 - num2, num2 - num1]
    
