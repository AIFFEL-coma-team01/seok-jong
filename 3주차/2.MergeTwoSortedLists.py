# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        
        l1_p=l1
        l2_p=l2
        
        if l1.val>l2.val:
            head  = l2
        else:
            head=l1
        
        
        
        while l1_p is not None or l2_p is not None:
            if l1_p.val<=l2_p.val:
                
                tmp=l1_p
                l1_p=l1_p.next
                tmp.next=l2_p
                
            else:
                tmp=l2_p
                l2_p=l2_p.next
                tmp.next=l1_p
            
        return head