digits = [1,2,3,4,5,6,7,8,9]
import numpy as np

class solver:
	def __init__(self,digits,goal):
		self.digits = [str(d) for d in digits]
		self.goal = str(goal)
	def solve(self):
		return check(goal,'0')
	def check(self,wanted_digit='0',remainder='0'):
		if str(sum([int(d[-1]) for d in self.digits]))[-1]==wanted_digit:
		#continue
			print "YES"		
		else:
			print "NO"		

attempt = solver(digits,100)	
attempt.check()	
