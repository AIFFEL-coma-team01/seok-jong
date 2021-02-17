class ListNode:
        def __init__(self, val=None, right=None,left=None):
            self.val = val
            self.right = right
            self.left = left


class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self._max=k
        self.leng=0

        self.head=ListNode(None)
        self.tail=self.head
        self.head.left=self.head
        self.head.right=self.head

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.leng==self._max:
            return False
        if self.leng==0:
            self.head.val=value
            self.leng+=1
            return True
        else:
            tmp=ListNode(value,self.head,self.tail)
            self.head.left=tmp
            self.tail.right=tmp
            self.head=tmp
            self.leng+=1
            return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.leng==self._max:
            return False
        if self.leng==0:
            self.head.val=value
            self.leng+=1
            return True
        else:
            tmp=ListNode(value,self.head,self.tail)
            self.head.left=tmp
            self.tail.right=tmp
            self.tail=tmp
            self.leng+=1
            return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.leng==0:
            return False

        self.head=self.head.right
        self.head.left=self.tail
        self.tail.right=self.head
        self.leng-=1
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.leng==0:
            return False

        self.tail=self.tail.left
        self.tail.right=self.head
        self.head.left=self.tail
        self.leng-=1
        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.leng==0:
            return -1
        return self.head.val

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.leng==0:
            return -1
        return self.tail.val

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        if self.leng==0:
            return True
        else:
            return False


    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        if self.leng==self._max:
            return True
        else:
            return False

  

# Your MyCircularDeque object will be instantiated and called as such:
obj = MyCircularDeque(4)
param_1 = obj.insertFront(9)
param_4 = obj.deleteLast()
param_6 = obj.getRear()
param_6 = obj.getRear()



param_5 = obj.getFront()
param_2 = obj.insertLast(3)
param_5 = obj.getFront()
param_1 = obj.insertFront(9)
param_6 = obj.getRear()
param_5 = obj.getFront()
param_5 = obj.getFront()
param_4 = obj.deleteLast()
param_6 = obj.getRear()

param_3 = obj.deleteFront()
param_4 = obj.deleteLast()
param_5 = obj.getFront()
param_6 = obj.getRear()
param_7 = obj.isEmpty()
param_8 = obj.isFull()