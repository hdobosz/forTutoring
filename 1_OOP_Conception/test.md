'''
Node 1       Node 2       Node 3       Node 4
+-------+    +-------+    +-------+    +-------+
| Data 1|    | Data 2|    | Data 3|    | Data 4|
| Next--+--->| Next--+--->| Next--+--->| Next--+--->
+-------+    +-------+    +-------+    +-------+
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

