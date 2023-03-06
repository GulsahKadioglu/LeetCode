"""
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    You can return the answer in any order.

    Example 1:

    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
    
    Example 2:

    Input: nums = [3,2,4], target = 6
    Output: [1,2]
    
    Example 3:

    Input: nums = [3,3], target = 6
    Output: [0,1]
 
    Constraints:

    2 <= nums.length <= 104
    -109 <= nums[i] <= 109
    -109 <= target <= 109
    Only one valid answer exists.

    Follow-up: Can you come up with an algorithm that is less than O(n^2) time complexity?
    
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    
# Big-O notation describes the limiting behavior of a function when the argument tends towards a particular value or infinity.
# It is used to classify algorithms by how their runtime or space requirements grow as the input size (n) grows.
# There is a quadratic( O(n^2) ) time complexity when it has to perform a linear time operation for each value in the input data.

# We want to find two values whose sum is the target number in the given array and return their indexs.

# Hashmap is a type of data structure that maps keys to value pairs.
# It stores key-value pairs, and the key is created using a hash function (a function that calculates an index value holding items to search, add, remove, etc.). 
# This makes accessing data easy and fast.

# We can loop through the array once and every iteration.
# Through this loop we're going to add something to the hash map.
# Thus, as we iterate through the array for every number we look at,
# what we're actually going to store is the number we need to add to that number to reach the target.
# This will be the key we add to the map.

# The dict function creates a dictionary. It is used to store data values in key:value pairs. It is a collection which is unordered, changeable and indexed.
# The range function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.

        map = dict()

        for i in range(len(nums)):
            number = nums[i]
            remaining = target - nums[i]
            
            if number in map:
               return [map[number], i]
            else:
               map[remaining] = i
