import numpy as np

class LinearRegressor:
    def __init__(self, lRate=0.1, epochCap=100):
        self.lRate = lRate # Learning rate for the model
        self.epochCap = epochCap # How may training iterations the model should take

    # I'm including the weights as a parameter rather than using self.weights to make testing easier
    def predict(self, X, weights):
        """Make a prediction for a given input"""
        return np.dot(X, weights) # take the dot product of input with weights

    def cost(self, yPred, yTrue):
        """Calculate the current cost/loss for the model"""
        return np.mean(abs(yTrue - yPred))

    def calculate_gradients(self, X, yPred, y):
        """Calculate the gradients for optimising the model parameters"""
        return np.dot(X.T, (yPred - y)) / len(X)

    # This return value is purely to make testing more clean, happy to discuss whether it is correct
    # Same with using weights rather than just self.weights -= ...
    def apply_gradients(self, weights, lRate, gradients):
        self.weights = weights - lRate * gradients
        return self.weights 

    def fit(self, X, y):
        self.weights = np.zeros(X.shape[1])

        for epochCount in range(self.epochCap):
            yPred = self.predict(X)

            gradients = self.calculate_gradient(self.weights)
            self.apply_gradients(gradients, self.weights)