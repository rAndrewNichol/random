class Time:
	
	def __init__(self, hours = 0, minutes = 0, seconds = 0):
		self.hours, self.minutes, self.seconds = hours, minutes, seconds
	
	def printTime(self):
		#print("{:s}:{:s}:{:s}".format(self.hours.zfill(2), self.minutes.zfill(2), self.seconds.zfill(2)))
		print("%s:%s:%s" % (str(self.hours).zfill(2), str(self.minutes).zfill(2), str(self.seconds).zfill(2)))

	#apparently can also do this wacky-ass shit:
	def printTime2(time):
		print("%s:%s:%s" % (str(time.hours).zfill(2), str(time.minutes).zfill(2), str(time.seconds).zfill(2)))

	def after(self, compare):
		if self.hours > compare.hours:
			return True
		elif self.hours == compare.hours:
			if self.minutes > compare.minutes:
				return True
			elif self.minutes == compare.minutes:
				#ideally would have equivalency here, but cannot express that in boolean function
				if self.seconds >= compare.seconds:
					return True
		return False

	# can do without nests using == as the last-resort condition:
	'''def after(self, compare):
		if self.hours > compare.hours: return True
		elif self.hours < compare.hours: return False

		if self.minutes > compare.minutes: return True
		elif self.minutes < compare.minutes: return False
	
		if self.seconds >= compare.seconds:
			return True
		return False
	'''	
	def addTime(self, other_time):
		sum = Time(self.hours + other_time.hours, 
			self.minutes + other_time.minutes, 
			self.seconds + other_time.seconds) 
		if sum.minutes >= 60:
			sum.minutes -= 60
			sum.hours += 1
		if sum.seconds >= 60:
			sum.seconds -= 60
			sum.minutes += 1
		return sum

	# increment our time by some 'seconds'
	def increment(self, seconds):
		self.seconds += seconds
		while self.seconds >= 60:
			self.seconds -= 60
			self.minutes += 1
		while self.minutes >= 60:
			self.minutes -= 60
			self.hours += 1
    

# now some alternative stuff:
def convertToSeconds(t): 
	minutes = t.hours * 60 + t.minutes 
	seconds = minutes * 60 + t.seconds 
	return seconds 

def makeTime(seconds): 
	time = Time() 
	time.hours = seconds // 3600 
	time.minutes = (seconds%3600) // 60 
	time.seconds = seconds%60 
	return time 	

def addTime2(t1, t2): 
  	seconds = convertToSeconds(t1) + convertToSeconds(t2) 
  	return makeTime(seconds) 



noon = Time(12, 0, 45)
noon.printTime()

five_thirty = Time(5, 30, 27)
five_thirty.printTime()

print("after") if five_thirty.after(noon) else print ("before")
print("after") if noon.after(five_thirty) else print ("before")
print("after") if five_thirty.after(five_thirty) else print ("before")

five_thirty.addTime(noon).printTime()

five_thirty.increment(100)
five_thirty.printTime()

five_thirty.printTime2()

default = Time()
default.printTime()

