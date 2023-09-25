class queue:
    def __init__(self):
        self.x=[]
    def empty(self):
        return len(self.x)==0
    def enqueue(self,y):
        self.x.insert(0,y)
    def dequeue(self):
        if not self.empty():
            return self.x.pop()
        else:
            return "Queue empty"
    def size(self):
        return len(self.x)
    
queue = queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)

print("Queue: ", queue.x)

dequeue = queue.dequeue()
print("dequeued item :", dequeue)
print("Queue after dequeue: ", queue.x)

print("size: ", queue.size())