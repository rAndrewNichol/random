class queue():
    def __init__(self, q = []):
        self.q = q
    def dequeue(self):
        return self.q.pop(0) 
    def enqueue(self,value):
        self.q.append(value) 
    def __str__(self):
        return "queue({})".format(self.q)
    def __bool__(self):
        return self.q != []

#q = queue()
#q.enqueue(0)
#q.enqueue(1)
#print ("dequeuing {} from queue".format(q.dequeue()))
#print (q)
