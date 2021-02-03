'''
LeetCode 225

Implement a last in first out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal queue (push, top, pop, and empty).

Implement the MyStack class:

void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.
Notes:

You must use only standard operations of a queue, which means only push to back, peek/pop from front, size, and is empty operations are valid.
Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue), as long as you use only a queue's standard operations.


'''






import queue 
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.que=queue.Queue()
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.que.put(x)
        for _ in range(self.que.qsize()-1):
            self.que.put(self.que.get())

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.que.get()


    def top(self) -> int:
        """
        Get the top element.
        """
        tmp=self.que.get()
        self.que.put(tmp)
        for _ in range(self.que.qsize()-1):
            self.que.put(self.que.get())
        return tmp

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.que.empty()


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
obj.push(2)
print(obj.top())
print(obj.pop())
print(obj.top())
print(obj.empty())





'''
Runtime: 24 ms, faster than 94.85% of Python3 online submissions for Implement Stack using Queues.
Memory Usage: 14.5 MB, less than 13.49% of Python3 online submissions for Implement Stack using Queues.
'''