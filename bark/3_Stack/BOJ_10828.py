import sys

class Node:
    def __init__(self, v):
        self.next = None
        self.value = v

class Stack:
    def __init__(self):
        self.count = 0
        self.top = Node(-1)
    
    def Push(self, node):
        node.next = self.top
        self.top = node
        self.count = self.count + 1

    def Pop(self):
        if self.count >= 1:
            popNode = self.top
            self.top = popNode.next
            self.count = self.count - 1
            return popNode
        else:
            return self.top

    def Size(self):
        return self.count
    
    def Empty(self):
        return self.count == 0
    
    def Top(self):
        return self.top


count = int(sys.stdin.readline())
input = []
for i in range(count):
    s = str(sys.stdin.readline())
    s = s.replace('\n', '')
    input.append(s)

st = Stack()

for i in input:
    lstr = i.split()
    if len(lstr) == 1:
        v = -1
        func = lstr[0]
        if func == 'top':
            v = st.Top().value
        elif func == 'size':
            v = st.Size()
        elif func == 'empty':
            v = int(st.Empty())
        elif func == 'pop':
            v = st.Pop().value
        print(v)
    elif len(lstr) == 2:
        node = Node(int(lstr[1]))
        st.Push(node)