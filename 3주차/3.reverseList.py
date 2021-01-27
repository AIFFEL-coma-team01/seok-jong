# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        tmp=head
        pre=None
        
        while tmp is not None:
            next_p=tmp.next
            tmp.next=pre
            
            pre=tmp
            tmp=next_p
        return pre
            