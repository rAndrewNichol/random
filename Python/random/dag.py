class node:
	def __init__(self, label = None, connections = []):
		self.label = label
		
	def addOut(self):
		pass
	def addIn(self):
		pass 
class graph:
	def __init__(self, map):
		pass		


class dag:
	def __init__(self,map):
	# map is of form {1:[(2,10),(3,7)],2:[(3,4)]...},
	# ie {node:[(to_node,arcweight),...],2:[...]...}
		self.graph = graph(map)
		
