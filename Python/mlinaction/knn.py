from numpy import *
import operator
import matplotlib.pyplot as plt
import matplotlib
file = 'test_data.txt'

def load_data(filename):
	rows, labels, testrows, testlabels = [], [], [], []
	with open(filename, 'r') as infile:
		source = array([line.split() for line in infile.read().splitlines()])
	data  = source[:,:-1].astype(float)
	labels  = source[:,-1]
	length = len(labels)
	# to standardize data....
	mins = data.min(0)
	maxs = data.max(0)
	ranges = maxs - mins
	normed = (data - tile(mins, (length,1))) /  ranges
	# for line in data[:int(.9*length)]:
	# 	rows.append([float(num) for num in line.split()[:3]])
	# 	labels.append(line.split()[-1])
	# for line in data[int(.9*length):]:
	# 	testrows.append([float(num) for num in line.split()[:3]])
	# 	testlabels.append(line.split()[-1])

	# return ((array(rows), labels), (array(testrows), testlabels))
	return ((normed[:int(length*.9),:], labels[:length*.9]), (normed[int(length*.9):,:], labels[int(length*.9):]))

def classify(data, input, k):
	labels = data[1]
	data = data[0]
	size = len(data)
	# Alt methods
	# size2 = data.shape[0]
	# print("Size : %d, size2: %d" % (size,size2))
	# print("Size: {:d}, size2: {:d}".format(size,size2))
	distances = []
	pt_ct = 0
	for point in data:
		sum = 0
		for dim in range(len(input)):
			sum += (input[dim] - point[dim])**2
		distances.append((sum ** .5, labels[pt_ct])), 
		pt_ct += 1 
	nearest = sorted(distances, key = lambda x:x[0])[:k]
	lab_cts = {}
	for each in nearest:
		if each[1] in lab_cts:
			lab_cts[each[1]] += 1
		else:
			lab_cts[each[1]] = 1
	return max(lab_cts.items(), key = lambda x: x[1])[0]

def classify_np(data, input, k):
	# much more efficient
	labels = data[1]
	data = data[0]
	size = data.shape[0]
	#difference matrix
	diffMat = tile(input, (size,1)) - data
	nearest = sorted(enumerate([row for row in (diffMat ** 2).sum(axis = 1)]), key = lambda x:x[1])[:k]
	lab_cts = {}
	for each in nearest:
		label = labels[each[0]]
		if label in lab_cts:
			lab_cts[label] += 1
		else:
			lab_cts[label] = 1
	return max(lab_cts.items(), key = lambda x: x[1])[0]

def visualize(data):
	#matplotlibstuff....
	fig = plt.figure()
	ax = fig.add_subplot(111)
	ax.scatter(data[:,1], data[:,2])
	plt.show()

def __main__():
	data, holdout = load_data(file)
	holdoutArray = holdout[0]
	holdoutLabels = holdout[1]
	# visualize(data[0])
	correct = 0
	for i in xrange(len(holdoutLabels)):
		pred = str(classify_np(data, holdoutArray[i], 10))
		if pred == str(holdoutLabels[i]):
			correct += 1
	print "Error Rate: " + str(1 - float(correct)/len(holdoutLabels))

		
	# classify(data, holdoutArray[i], 10)

__main__()
