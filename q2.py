class Stack:
    def __init__(self):
        self.x =[]
    def empty(self):
        return len(self.x)==0
    def push(self,y):
        self.x.append(y)
    def pop(self):
        if not self.empty():
            return self.x.pop()
        else:
            return "Empty stack. Cannot pop"
stack=Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print("Stack:", stack.x)
pop = stack.pop()
print("popped: ", pop)
print("After pop: ", stack.x)