# Import the necessary library
import numpy as np


# Build the Perceptron Model
class Perceptron:

    def __init__(self, num_inputs, learning_rate=0.01):
        # Initialize the weight and learning rate
        self.weights = np.random.rand(num_inputs + 1) #tezine za treniranje modela; np.random.rand(num_inputs + 1) - vraca r random broja
        print(self.weights)
        self.learning_rate = learning_rate
        print(self.learning_rate)

    # Define the first linear layer
    def linear(self, inputs):
        Z = inputs @ self.weights[1:].T + self.weights[0] # @ -> mnozi matrice!; .T znaci transponovano (preabcuje iz brste u kolonu); 
        # self.weights[0] -> izolovanje W(0)
        # print(inputs, self.weights[1:], self.weights[0])
        return Z

    # Define the Heaviside Step function.
    def Heaviside_step_fn(self, z):
        if z >= 0:
            return 1
        else:
            return 0

    # Define the Prediction
    def predict(self, inputs):
        Z = self.linear(inputs) #input su x1 i x2
        try:
            pred = []
            for z in Z:
                pred.append(self.Heaviside_step_fn(z)) #razvrstava pred listu u kojoj su 0 i 1
        except:
            return self.Heaviside_step_fn(Z)
        return pred

    # Define the Loss function
    def loss(self, prediction, target):
        loss = (prediction - target) #racuna koliko smo pogrijesili
        return loss

    # Define training
    def train(self, inputs, target):
        prediction = self.predict(inputs)
        error = self.loss(prediction, target)
        self.weights[1:] += self.learning_rate * error * inputs # pinje ili spusta koeficijente u zavisnosti kolika je greska
        self.weights[0] += self.learning_rate * error

    # Fit the model
    def fit(self, X, y, num_epochs):
        for epoch in range(num_epochs): #epocha su prolazni ciklusi za korekciju
            for inputs, target in zip(X, y): #inputs (0,0), (0,1), (1,0), (1,1), targets 0 0 0 1, zip od toga pravi jednu listu
                self.train(inputs, target) #za jednu epohu