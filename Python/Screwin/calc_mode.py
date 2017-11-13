class Stats:
	def __init__(self, nums = []):
		self.nums = nums
	def mode(self):
		try:
			num_counts = {}
			for num in self.nums:
				if num not in num_counts:
					num_counts[num] = 1
				else:
					num_counts[num] += 1
			max_value = 0
			for item in num_counts.items():
				if item[1] > max_value: max_value = item[1]

			return [item[0] for item in num_counts.items() if item[1] == max_value]
		except ValueError:
			print("No values in collection")


new = Stats([1,2,3,4,4,5,2,7,5])
print(new.mode())