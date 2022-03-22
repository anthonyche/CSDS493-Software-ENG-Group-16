from Perceptron import Perceptron

#Activate_function
Act_func = lambda x: x

#Class inheritance
class LinearUnit(Perceptron):
    def __init__(self, input_num):
        #input_num is the number of feature
        Perceptron.__init__(self, input_num, Act_func)
    
def get_training_dataset():
    input_vecs = [[5],[3],[8],[1.4],[10.1],[13.8]] # working years
    labels = [5500, 2300, 7600, 1800, 11400, 20000 ]
    return input_vecs, labels

def train_linear_unit():
    # instantiate an object lu of a class LinearUnit
    lu = LinearUnit(1)
    input_vecs, labels = get_training_dataset()
    #train func is inherited from class Perceptron
    lu.train(input_vecs, labels, 10, 0.001)
    return lu

if __name__ == '__main__':
    linear_unit = train_linear_unit() # linear_unit is the return value lu
    # and lu is the object of the class LinearUnit
    print(linear_unit)
    print('Work 3.4 years, monthly salary = %.2f'% linear_unit.predict([3.4]))
    print('Work 18 years, monthly salary = %.2f'% linear_unit.predict([18]))
    print('Work 1.5 years, monthly salary = %.2f'% linear_unit.predict([1.5]))
    print('Work 6.8 years, monthly salary = %.2f'% linear_unit.predict([6.8]))



    




