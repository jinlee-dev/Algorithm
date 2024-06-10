import sys

class Node:
    def __init__(self, value):
        self.next = None
        self.value = value

class Queue:
    def __init__(self):
        self.front = None
        self.back = None
        self.count = 0

    def Push(self, node):
        if self.count == 0:
            self.front = node
        else:
            self.back.next = node
        node.next = None
        self.back = node
        self.count = self.count + 1


    def Pop(self):
        if self.count >= 1:
            popNode = self.front
            self.front = popNode.next
            self.count = self.count - 1
            return popNode
        else:
            return Node(-1)
    
    def Size(self):
        return self.count
    
    def Front(self):
        if self.Size() > 0:
            return self.front
        return Node(-1)
    
    def Back(self):
        if self.Size() > 0:
            return self.back
        return Node(-1)
    
count = int(sys.stdin.readline())
input = []
for i in range(count):
    s = str(sys.stdin.readline())
    s = s.replace('\n', '')
    input.append(s)

q = Queue()

for i in input:
    split = i.split()
    if len(split) == 1:
        console = str(split[0])
        val = 0
        if console == 'pop':
            val = q.Pop().value
        elif console == 'size':
            val = q.Size()
        elif console == 'empty':
            val = int(q.Size() == 0)
        elif console == 'front':
            val = q.Front().value
        elif console == 'back':
            val = q.Back().value
        print(val)
    elif len(split) == 2:
        val = int(split[1])
        q.Push(Node(val))

