# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        tmp=head
        
        while tmp and tmp.next:
            tmp_val=tmp.val
            tmp.val=tmp.next.val
            tmp.next.val=tmp_val
            
            tmp=tmp.next.next
            
        return head
           