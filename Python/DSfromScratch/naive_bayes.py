import re, os, random
from math import log, exp
from tools import split_data
# from collections import defaultdict

def tokenize(message):
	message = message.lower() # convert to lowercase
	all_words = set(re.findall("[a-z0-9'-]+", message)) # sets capture unique elements
	return all_words

def count_words(training_set):
	''' training_set consists of a list of (message, is_spam) pairs '''
	counts = {}
	# counts = defaultdict(lambda: [0,0])
	for message, is_spam in training_set:
		for word in tokenize(message):
			if word not in counts: counts[word] = [0,0]
			counts[word][0 if is_spam else 1] += 1
	return counts

def probabilities(count_dict, total_spams, total_non_spams, k = .5):
	# triplets of (word, prob word|spam, prob word|non_spam)
	triplets = [(w, (spam + k) / (total_spams + 2 * k), (non_spam + k) / (total_non_spams + 2 * k)) 
	for w, (spam, non_spam) in count_dict.items()]
	return triplets

# Note: p(x) * p(y) * p(z) = exp( ln(p(x)) + ln(p(y)) + ln(p(z)) )
# Which greatly reduces the risk of underflow to 0 during calculation!

def calc_prob_is_spam_given_data(word_probs, message):
	message_in_words = tokenize(message)
	log_prob_spam = log_prob_non_spam = 0.0
	for word, prob_if_spam, prob_if_non_spam in word_probs:
		if word in message_in_words:
			log_prob_spam += log(prob_if_spam)
			log_prob_non_spam += log(prob_if_non_spam)
		else:
			log_prob_spam += log(1 - prob_if_spam)
			log_prob_non_spam += log(1 - prob_if_non_spam)
	prob_words_if_spam = exp(log_prob_spam)
	prob_words_if_non_spam =  exp(log_prob_non_spam)
	return prob_words_if_spam / (prob_words_if_spam + prob_words_if_non_spam)

class NaiveBayes:

	def __init__(self, k = .5):
		self.k = k

	def train(self, training_set):
		num_spams = len([is_spam for message, is_spam in training_set if is_spam])
		num_non_spams = len(training_set) - num_spams
		word_counts = count_words(training_set)
		self.word_probs = probabilities(word_counts, num_spams, num_non_spams, self.k)

	def classify(self, message):
		return calc_prob_is_spam_given_data(self.word_probs, message)


def __main__():
	start_path = 'C:/Users/Andrew/Documents/Coding/PythonFiles/DSfromScratch'
	os.chdir(start_path)

	data = []
	relevant_files = [file for file in os.listdir() if 'ham' in file or 'spam' in file]
	for file_name in relevant_files: 
		os.chdir(start_path + '/' + file_name)
		
		for each_file in os.listdir():
			is_spam = 1 if 'spam' in file_name else 0
			
			with open(each_file, 'r', encoding = 'ISO-8859-1') as file:
				for line in file:
					if line.startswith('Subject: '):
						subject = re.sub('^Subject: ', '', line).strip()
						data.append((subject, is_spam))

	random.seed(0)
	train_data, test_data = split_data(data, .75)

	classifier = NaiveBayes()
	classifier.train(train_data)

	#results:

	classified = [(subject, is_spam, classifier.classify(subject))
					for subject, is_spam in test_data]
	
	for each in classified: print(each)

	# analytics:
	amount_tested = len(test_data)
	counts = [(is_spam, prob_of_spam > .5) for _, is_spam, prob_of_spam in classified]
	print()
	print( 'Correct: ', len( [x for x,y in counts if x == y]) )
	print( 'Total: ', amount_tested)

	total_spams = len([is_spam for _, is_spam in test_data if is_spam])
	total_non_spams = amount_tested - total_spams

	num_pos = len([prediction for _,prediction in counts if prediction == 1])
	num_neg = len([prediction for _,prediction in counts if prediction==0])

	false_pos = len([is_spam for is_spam,prediction in counts if is_spam == 0 and prediction == 1])
	false_neg = len([is_spam for is_spam, prediction in counts if is_spam == 1 and prediction == 0])
	print('False Positives: ', false_pos)
	print('False Negatives: ', false_neg)

	# num_pos - false_pos = correctly classified positives
	# Precision is the fraction of relevant instances among the retrieved instances
	# ie number true out of number predicted to be true
	print('Precision = ', (num_pos - false_pos) / num_pos )

	# Recall is the fraction of relevant instances that have been retrieved over total relevant instances
	# ie number true out of all actually true
	print('Recall = ', (num_pos - false_pos) / total_spams)



__main__()


