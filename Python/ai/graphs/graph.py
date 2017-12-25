#uniform cost graph
from queue import queue as q
from stack import stack
from collections import defaultdict

class node:
    def __init__(self, outs = set(), ins = set()):
        self.outs = set(outs)
        self.ins = set(ins) 

class graph:
    def __init__(self, matrix = [[0]]):
        # matrix will be symmetric if graph is non-directed
        # matrix must be square
        self.matrix = matrix
        self.graph = self.build()
    def __str__(self):
        s = ""
        for key,value in self.graph.items():
            s += "{}: {}\n".format(key, value.outs)
        return s
    def build(self):
        graph = defaultdict(node) 
        size = len(self.matrix)
        for i in range(size):
            graph[i] = node([j for j in range(size) if self.matrix[i][j]])
        self.max = i
        return graph
    def find_shortest(self, f = 0, t = 0, method = 'bf'):
        if not t:
            t = self.max
        if method not in ['bf','df','a*']:
            raise Exception('invalid method for find_shortest()')
        if method == 'bf':
            explored, queue = set(), q([f])
            return queue 


g = graph([[0,1,0,1],[1,0,1,0],[0,1,0,1],[1,0,1,0]])
print(g)
print (g.find_shortest(0,3,'bf'))
