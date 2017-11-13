from random import random

def split_data(data, split_prob):
	results = [], []
	for row in data:
		# this guy is fuckin brilliant
		results[0 if random() < split_prob else 1].append(row)
	return results


