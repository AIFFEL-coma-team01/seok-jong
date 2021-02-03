'''
LeetCode 622

Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.

Implementation the MyCircularQueue class:

MyCircularQueue(k) Initializes the object with the size of the queue to be k.
int Front() Gets the front item from the queue. If the queue is empty, return -1.
int Rear() Gets the last item from the queue. If the queue is empty, return -1.
boolean enQueue(int value) Inserts an element into the circular queue. Return true if the operation is successful.
boolean deQueue() Deletes an element from the circular queue. Return true if the operation is successful.
boolean isEmpty() Checks whether the circular queue is empty or not.
boolean isFull() Checks whether the circular queue is full or not.
'''




class MyCircularQueue:

    def __init__(self, k: int):
        self.cir_que = [None for i in range(k)]
        self.front=0
        self.rear=0
        self.max_=k-1

    def enQueue(self, value: int) -> bool:
        if self.isFull() ==True:
            return False
        if self.isEmpty()==True:
            self.cir_que[self.front]=value
            return True
        if self.rear==self.max_:
            self.rear=0
        else:
            self.rear+=1
        self.cir_que[self.rear]=value
        return True


    def deQueue(self) -> bool:
        if self.isEmpty() ==True:
            return False
        self.cir_que[self.front]=None
        if self.isEmpty()==True:
            return True
        if self.front==self.max_:
            self.front=0
        else:
            self.front+=1
        return True

    def Front(self) -> int:
        if self.isEmpty()!=True:
            return self.cir_que[self.front]
        else:
            return -1

    def Rear(self) -> int:
        if self.isEmpty()!=True:
            return self.cir_que[self.rear]
        else:
            return -1
        
    def isEmpty(self) -> bool:
        if self.front==self.rear:
            if self.cir_que[self.front]==None:
                return True
        return False


    def isFull(self) -> bool:
        if self.rear==self.max_:
            if self.front==0:
                return True 
            return False
        if self.rear+1==self.front:
            return True
        else:
            return False


# Your MyCircularQueue object will be instantiated and called as such:
'''
obj = MyCircularQueue(6)
print(obj.enQueue(6))
print(obj.Rear())
print(obj.Rear())
print(obj.deQueue())
print(obj.enQueue(5))
print(obj.Rear())
print(obj.deQueue())
print(obj.front())
print(obj.deQueue())
print(obj.deQueue())
print(obj.deQueue())
'''


'''
Runtime: 96 ms, faster than 9.76% of Python3 online submissions for Design Circular Queue.
Memory Usage: 15 MB, less than 9.17% of Python3 online submissions for Design Circular Queue.

'''



  
class MyCircularQueue:

    def __init__(self, k: int):
        self.q=[None]*k
        self.maxlen=k
        self.p1=0
        self.p2=0

    def enQueue(self, value: int) -> bool:
        if self.q[self.p2] is None: #꽉 차있는지 검사
            self.q[self.p2]=value
            self.p2=(self.p2+1)%self.maxlen #p2 한칸 전진 %연산 이용하여 끝 포인트일 경우 0으로 이동 
            return True
        else:
            return False # data를 넣고 p2를 이동시키므로 list에 공간이 없으면 False 반환 

    def deQueue(self) -> bool:
        if self.q[self.p1] is None: #비어있으면 False반환
            return False
        else:
            self.q[self.p1]=None 
            self.p1=(self.p1+1)%self.maxlen # p1 한칸 전진 

        return True


    def Front(self) -> int:
        return -1 if self.q[self.p1] is None else self.q[self.p1] 

    def Rear(self) -> int:
        return -1 if self.q[self.p2-1] is None else self.q[self.p2-1] #p2가 0일 경우에도 -1이 되므로 끝 data를 반환 
        
    def isEmpty(self) -> bool:
        return self.p1 == self.p2 and self.q[self.p1] is None


    def isFull(self) -> bool:
        return self.p1 == self.p2 and self.q[self.p1] is not None


'''
Runtime: 64 ms, faster than 90.14% of Python3 online submissions for Design Circular Queue.
Memory Usage: 15 MB, less than 29.43% of Python3 online submissions for Design Circular Queue.

'''