"""
    You are given the heads of two sorted linked lists list1 and list2.

    Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

    Return the head of the merged linked list.
    
    Example 1:
    
    Input: list1 = [1,2,4], list2 = [1,3,4]
    Output: [1,1,2,3,4,4]
    
    Example 2:

    Input: list1 = [], list2 = []
    Output: []
    
    Example 3:

    Input: list1 = [], list2 = [0]
    Output: [0]

    Constraints:

    The number of nodes in both lists is in the range [0, 50].
    -100 <= Node.val <= 100
    Both list1 and list2 are sorted in non-decreasing order.
    
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
# Dummy Head Node: One of the problems in dealing with pointer(variables that hold the memory address of another variable)
# based ordered lists is writing code to take care of special cases. If we want to insert a node in an ordered linked list,
# we must take care of the 'special case'* of inserting this node in the beginning of the list. 
# *If a node is inserted into the beginning of the list, the pointer indicating the beginning of the list, head,  must be changed.
# ıf we want to delete a particular node, we must again also write code to handle the special case of deleting the first node in the list.

        dummy = ListNode()
        head = dummy
        
        
