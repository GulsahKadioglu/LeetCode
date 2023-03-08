""" 

    Given a sorted array of distinct integers and a target value, return the index if the target is found.
    If not, return the index where it would be if it were inserted in order.

    You must write an algorithm with O(log n) runtime complexity.

    Example 1:

    Input: nums = [1,3,5,6], target = 5
    Output: 2
    
    Example 2:

    Input: nums = [1,3,5,6], target = 2
    Output: 1
    
    Example 3:

    Input: nums = [1,3,5,6], target = 7
    Output: 4
 
    Constraints:

    1 <= nums.length <= 10^4
    -10^4 <= nums[i] <= 10^4
    
    nums contains distinct values sorted in ascending order.
    -10^4 <= target <= 10^4
    
"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
    
# Firstly we can define the right(r) and left(l) index of the array
# Secondly if we know the integer in the middle(m) of the array, we can compare this with target
# If the integer is smaller/bigger than the target, we can limit the integers of the array with new r and l integers
      
      left = 0
         right = len(nums) - 1
         while left <= right:
               middle = left +(right-left) // 2
               if nums[middle] > target:
                  right = middle - 1
               elif num[middle] < target:
                  left = middle + 1
               else:
               return middle
         return -1
