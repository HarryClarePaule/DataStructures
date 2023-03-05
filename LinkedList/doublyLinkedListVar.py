class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1

    def insert(self, data, index):
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")
        new_node = Node(data)
        if index == 0:
            if self.head is None:
                self.head = new_node
                self.tail = new_node
            else:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
        elif index == self.size:
            self.append(data)
        else:
            current = self.head
            for i in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next.prev = new_node
            current.next = new_node
            new_node.prev = current
        self.size += 1

    def remove(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        if index == 0:
            if self.size == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
        elif index == self.size - 1:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            current = self.head
            for i in range(index - 1):
                current = current.next
            current.next = current.next.next
            current.next.prev = current
        self.size -= 1

    def remove_value(self, value):
        current = self.head
        index = 0
        while current is not None:
            if current.data == value:
                self.remove(index)
                return
            current = current.next
            index += 1

    def extend(self, iterable):
        for item in iterable:
            self.append(item)

    def print_forward(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

    def print_backward(self):
        current = self.tail
        while current is not None:
            print(current.data)
            current = current.prev

    def __len__(self):
        return self.size

if __name__ == '__main__':
    list = ["banana","mango","grapes","orange"]
    dll = DoublyLinkedList()
    dll.extend(list)
    dll.append("harry")
    dll.print_forward()
    dll.print_backward()