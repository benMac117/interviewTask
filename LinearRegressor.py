import numpy as np

class LinearRegressor:
    def __init__(self, lRate=0.1, epochCap=100):
        self.lRate = lRate # Learning rate for the model
        self.epochCap = epochCap # How may training iterations the model should take

    # I'm including the weights as a parameter rather than using self.weights to make testing easier
    def predict(self, samples, weights):
        """Make a prediction for a given input"""
        return np.dot(X, samples) # take the dot product of input with weights

    def cost(self, predictions, targets):
        """Calculate the current cost/loss for the model"""
        return np.mean(abs(targets - predictions))

    def calculate_gradients(self, samples, predictions, targets):
        """Calculate the gradients for optimising the model parameters"""
        return np.dot(samples.T, (predictions - targets)) / len(targets)

    # This return value is purely to make testing more clean, happy to discuss whether it is correct
    # Same with using weights rather than just self.weights -= ...
    def apply_gradients(self, weights, lRate, gradients):
        self.weights = weights - lRate * gradients
        return self.weights 

    def fit(self, samples, targets):
        self.weights = np.zeros(samples.shape[1])

        for epochCount in range(self.epochCap):
            predictions = self.predict(samples)

            gradients = self.calculate_gradient(samples, predictions, targets)
            self.apply_gradients(self.weights, self.lRate, gradients)