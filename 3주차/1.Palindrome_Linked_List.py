# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(self, head: ListNode) -> bool:
        q=[]
        node=head
        while node is not None:
            q.append(node.val)
            node=next
        start=0
        end=len(q)-1
        for i in range(len(q)//2):
            if q[start]!=q[end]:
                return False
            else:
                start+=1
                end-=1
                continue
        return True

