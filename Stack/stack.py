# ----------------------------------------------------------------
# Example of a stack implented using a list, not recommended since python stores list as dynamic array therefore O(n)

s = []
s.append('harry')
s.append('rebecca')
s.append('pinot')
s.append('phil')

print(s[-1])

print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())

# ----------------------------------------------------------------
# Example of stack using deque
from collections import deque

class Stack():
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return self.container[-1]
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)
    
dstack = Stack()

print(dstack.is_empty())

dstack.push(5)
dstack.push(10)

print(dstack.is_empty())

print(dstack.container)
print(dstack.pop())
print(f'Size is {dstack.size}')
print(dstack.peek())
dstack.is_empty()
print(f'Size is {dstack.size}')


