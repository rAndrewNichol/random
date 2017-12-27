class stack:
    def __init__(self, stack=[]):
        self.stack = stack
    def push(self,value):
        self.stack.append(value)
    def pop(self):
        return self.stack.pop(len(self.stack)-1)
    def __str__(self):
        return "stack({})".format(self.stack)
    def __bool__(self):
        return self.stack != []

#s = stack()
#s.push(0)
#s.push(1)
#print ("popping {} from stack".format(s.pop()))
#print (s)
