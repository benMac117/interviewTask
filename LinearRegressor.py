import numpy as np

class LinearRegressor:
    def __init__(self, lRate=0.1, epochCap=100):
        self.lRate = lRate
        self.epochCap = epochCap

    def predict(self, X):
        #throw error if weights don't exist yet
        return np.dot(X, self.weights) # take the dot product of input with weights

    def cost(self, yPred, yTrue):
        return np.mean(abs(yTrue - yPred))

    def calculate_gradients(self, X, yPred, y):
        # same as linear regression, coursera
        return np.dot(X.T, (yPred - y)) / len(X)

    def apply_gradients(self, gradients):
        self.weights -= self.lRate * gradients 


    def fit(self, X, y):
        self.weights = np.zeros(X.shape[1])

        for epochCount in range(self.epochCap):
            yPred = self.predict(X)

            gradients = self.calculate_gradient(self.weights)
            self.apply_gradients(gradients, self.weights)