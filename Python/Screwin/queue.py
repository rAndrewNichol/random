class Queue():
    def __init__(self):
        self.newest = None
        self.oldest = None
    def is_empty(self):
        return True if not self.oldest else False
    def enqueue(self, value):
        if self.is_empty():
            self.newest = Node(value, self.newest, None)
            self.oldest = self.newest
        else:
            new = Node(value, self.newest, None)
            self.newest.behind = new
            self.newest = new
        return
    def dequeue(self):
        if not self.is_empty():
            tmp = self.oldest
            if not self.oldest.behind:
                self.newest = None
            self.oldest = self.oldest.behind
            return tmp
        return None
    def __str__(self):
        full = ''
        next_ = self.newest
        while next_:
            full += ", " + str(next_.value) 
            next_ = next_.ahead
        return full
            

class Node():
    def __init__(self, value, ahead = None, behind = None):
        self.value = value
        self.ahead = ahead
        self.behind = behind
    def __str__(self):
        return str(self.value)

q = Queue()
q.enqueue(5)
q.enqueue(12)
print(q)
d = q.dequeue()
print(d)
d = q.dequeue()
print(d)
q.dequeue()
q.enqueue(1)
q.enqueue(21)
q.enqueue(182)
print(q)
