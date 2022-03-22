import functools
import numpy as np

class Perceptron(object): 
    # use self in class
    def __init__(self, input_num, activator):
        """
        initialize the number of input and activator
        """
        self.activator = activator
        """
        initialize the weight and bias to 0
        """
        self.weights = [0.0 for _ in range(input_num)]
        self.bias = 0.0
    
    def __str__(self):
        return 'weights\t:%s\nbias\t:%f\n' % (self.weights, self.bias)
    
    def predict(self, input_vec):
        """
        input the vectors and get the calculation result of the proceptron
        """
        #input vectors are like[x1,x2,x3...]
        #weights are like[w1,w2,w3...]
        #zip input and weights together we get [(x1,w1),(x2,w2),(x3,w3)...]
        #x1*w1,x2*w2,x3*w3 
        return self.activator(sum(x*w for x,w in zip(input_vec, self.weights)) + self.bias)

    def train(self, input_vecs, labels, iteration:int, rate):
        """
        train data is input vectors and labels, and iteration times and learning rate
        """
        for i in range(iteration):
            self._one_iteration(input_vecs, labels, rate)

    def _one_iteration(self, input_vecs, labels, rate):
        """
        this is one iteration of all iterations
        """
        samples = zip(input_vecs, labels)
        for (input_vec, label) in samples:
            output = self.predict(input_vec)
        #in every iteration it updates the weights
            self._update_weights(input_vec, output, label, rate)

    def _update_weights(self,input_vec, output, label, rate):
        delta = label - output
        self.bias += rate*delta
        #The list container can be used as an array but stores pointers to objects
        #so we need to use np.array to transfer it into a real array
        self.weights += rate*delta*np.array(input_vec)        

# test on and function    
def acti_func(x):
    return 1 if x > 0 else 0

def get_training_dataset():
    input_vecs = [[1,1],[0,0],[1,0],[0,1]]
    labels = [1,0,0,0]
    return input_vecs, labels

def train_and_perceptron():
    """initialize the perceptron, and is 2-dimension"""
    # instantiate an object of a class
    p = Perceptron(2, acti_func)
    # get_training_dataset function has the input_vecs and labels as the return value
    input_vecs, labels = get_training_dataset()
    p.train(input_vecs, labels, 100, 0.1)
    #return the trained perceptron
    return p

if __name__ == '__main__':
    # get a trained and_perceptron, train_and_perceptron
    # function returns p, give this return value to new perceptron
    and_perceptron = train_and_perceptron()
    print(and_perceptron)
    print(and_perceptron.predict([1,1]))
    print(and_perceptron.predict([1,0]))
    print(and_perceptron.predict([0,0]))
    print(and_perceptron.predict([0,0]))






