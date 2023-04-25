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
        
# Instances of the 'ListNode' class represent the nodes of a linked list. The '__init__()' method of the class is used to create these instances.
# This method defines the 'val' property of the node and the 'next' property that points to the next node.
        
# Dummy Head Node: One of the problems in dealing with pointer(variables that hold the memory address of another variable)# For a linked list, we use a head record to keep the location of the head and sometimes a tail record to keep that of the tail, 
# based ordered lists is writing code to take care of special cases. If we want to insert a node in an ordered linked list,
# we must take care of the 'special case'* of inserting this node in the beginning of the list. 
# *If a node is inserted into the beginning of the list, the pointer indicating the beginning of the list, head,  must be changed.
# ıf we want to delete a particular node, we must again also write code to handle the special case of deleting the first node in the list.
# For a linked list, we use a head record to keep the location of the head and sometimes a tail record to keep that of the tail, 
# but we usually don't use other records to keep location information of other nodes in the linked list since we can find them in the previous node.

        head = ListNode()
        tail = head
        
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
                tail = tail.next
                
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
            
        return head.next
     
