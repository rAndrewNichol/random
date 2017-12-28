#uniform cost graph
from queue import queue as q
from stack import stack
from collections import defaultdict

class node:
    def __init__(self, outs = set()):
        self.outs = set(outs)
    def add_edge(self, out):
        self.outs.add(out)
        
class graph:
    def __init__(self, data = [[0]]):
        # matrix will be symmetric if graph is non-directed
        # matrix must be square
        self.data = data
        self.graph = self.build()
    def __str__(self):
        s = ""
        for key,value in self.graph.items():
            s += "{}: {}\n".format(key, value.outs)
        return s
    def build(self):
        graph = defaultdict(node) 
        size = len(self.data)
        if size == len(self.data[0]):
            # this is for graphs instantiated using a cost matrix
            for i in range(size):
                graph[i] = node([j for j in range(size) if self.data[i][j]])
            self.min, self.max = 0, i
        else:
            # this is for graphs instantiated using a list of edges (tuples)
            for edge in self.data:
                graph[edge[0]].add_edge(edge[1]) 
                # to accomodate nondirectional edges
                # graph[edge[1]].add_edge(edge[0])
            self.min, self.max = min(graph.keys()), max(graph.keys())
        return graph
    def find_shortest(self, f = 0, t = 0, method = 'bf'):
        if not t:
            t = self.max
        if not f:
            f = self.min
        print ("min:{},max:{}".format(self.min,self.max))
        start, goal = self.graph[f], self.graph[t]
        if method not in ['bf','df','a*','dijkstra']:
            raise Exception('invalid method for find_shortest()') 
        if method == 'bf':
            pred = {}
            explored, queue = set(), q([self.graph[f]])
            while queue:
                current = queue.dequeue()
                explored.add(current)
                for out in [self.graph[each] for each in current.outs if self.graph[each] not in explored]:
                    if out == goal:
                        back = current
                        path = [out,current]
                        while back != start:
                            back = pred[back]
                            path.append(back)
                        get_labels = {value:str(key) for key, value in self.graph.items()}
                        return "->".join(reversed([get_labels[each] for each in path]))
                    pred[out] = current
                    queue.enqueue(out)
                
g = graph([[0,1,1,0,0],[1,0,0,0,1],[1,0,0,1,0],[0,0,1,0,1],[0,1,0,1,0]])
gg = graph([(0,1),(0,2),(2,3),(3,4),(1,4)])
ggg = graph([('A','B'),('A','C'),('C','D'),('D','E'),('B','E')])
print(gg)
print(g)
print (g.find_shortest(0,4,'bf'))
print (gg.find_shortest(0,4,'bf'))
print (ggg.find_shortest('A','E','bf'))
print (g.find_shortest())
print (gg.find_shortest())
print (ggg.find_shortest())
