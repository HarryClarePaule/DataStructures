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
    
    # def reverse(self, string):
    #     letters = []
    #     for letter in string:
    #         letters.append(letter)
    #     letters.reverse()
    #     reverse_word = " ".join(letters)
    #     self.push(reverse_word)



def reverse_word(string):
    stack = Stack()

    for letter in string:
        stack.push(letter)

    rword = ''
    while stack.size() != 0: 
       rword += stack.pop()

    return(rword)


print(reverse_word('Hello Harry'))