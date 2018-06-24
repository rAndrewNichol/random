import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

mnist = input_data.read_data_sets("/tmp/data/",one_hot=True)

'''
input > weights > hidden l 1 (activation functions) > 
weights > hidden l 2 (act function) > weights > output layer

compare output to indended output with cost function (cross entropy etc)
optimization function to minimize cost (gradient descent etc)

backpropogation (algorithm goes backward through the process and
manipulates weights)

1 feed forward + backprop cycle = 1 epoch
'''

n_nodes_hl1, n_nodes_hl2, n_nodes_hl3 = 500, 500, 500

n_classes = 10
batch_size = 100
n_layers = 3

# height x width
x = tf.placeholder('float', [None, 784]) # input data (flattened)
y = tf.placeholder('float')

def neural_network_model(data):
	# (input_data * weights) + bias
	hidden_layer_1 = {'weights' : tf.Variable(tf.random_normal([784, n_nodes_hl1])), 
									'biases' : tf.Variable(tf.random_normal([n_nodes_hl1]))}

	hidden_layer_2 = {'weights' : tf.Variable(tf.random_normal([n_nodes_hl1, n_nodes_hl2])), 
									'biases' : tf.Variable(tf.random_normal([n_nodes_hl2]))}

	hidden_layer_3 = {'weights' : tf.Variable(tf.random_normal([n_nodes_hl2, n_nodes_hl3])), 
									'biases' : tf.Variable(tf.random_normal([n_nodes_hl3]))}

	output_layer = {'weights' : tf.Variable(tf.random_normal([n_nodes_hl3, n_classes])), 
									'biases' : tf.Variable(tf.random_normal([n_classes]))}

	l1 = tf.add(tf.matmul(data, hidden_layer_1['weights']), hidden_layer_1['biases'])
	l1 = tf.nn.relu(l1)

	l2 = tf.add(tf.matmul(l1, hidden_layer_2['weights']), hidden_layer_2['biases'])
	l2 = tf.nn.relu(l2)

	l3 = tf.add(tf.matmul(l2, hidden_layer_3['weights']), hidden_layer_3['biases'])
	l3 = tf.nn.relu(l3)

	output = tf.add(tf.matmul(l3, output_layer['weights']), output_layer['biases'])

	return output

def train_neuraL_network(x):
	prediction = neural_network_model(x)
	cost = tf.reduce_mean( tf.nn.softmax_cross_entropy_with_logits_v2(logits=prediction, labels=y) )
	# 											learning_rate default = 0.001
	optimizer = tf.train.AdamOptimizer().minimize(cost)
	# cycles of feed forward + back propogation
	n_epochs = 10

	with tf.Session() as sess:
		sess.run(tf.global_variables_initializer())
		for epoch in range(n_epochs):
			epoch_loss = 0
			for _ in range(int(mnist.train.num_examples/batch_size)):
				epoch_x, epoch_y = mnist.train.next_batch(batch_size)
				_, c = sess.run([optimizer,cost], feed_dict={x: epoch_x, y: epoch_y})
				epoch_loss += c
			print("Epoch {} completed out of {}. Loss : {}\n".format(epoch,n_epochs, epoch_loss))

		correct = tf.equal(tf.argmax(prediction,1), tf.argmax(y,1))

		accuracy = tf.reduce_mean(tf.cast(correct,'float'))
		print('Accuracy: {}'.format(accuracy.eval({x:mnist.test.images,y:mnist.test.labels})))

train_neuraL_network(x)
