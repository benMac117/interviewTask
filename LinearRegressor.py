import numpy as np

class LinearRegressor:
    def __init__(self, lRate=0.1, epochCap=100):
        self.lRate = lRate # Learning rate for the model
        self.epochCap = epochCap # How may training iterations the model should take

    def cost(self, predictions, targets):
        """Calculate the current cost/loss for the model"""
        return np.mean(abs(targets - predictions))

    def calculate_gradients(self, samples, predictions, targets):
        """Calculate the gradients for optimising the model parameters"""
        return np.dot(samples.T, (predictions - targets)) / len(targets)

    # This return value is purely to make testing more clean, happy to discuss whether it is correct
    # Same with using weights rather than just self.weights -= ...
    def apply_gradients(self, weights, lRate, gradients):
        """Modify the model to minimise cost"""
        self.weights = weights - lRate * gradients
        return self.weights

    # I'm including the weights as a nullable parameter rather than using self.weights to make testing easier
    # This doesn't feel like the best solution
    def predict(self, samples, weights=None):
        """Make a prediction for a given input"""
        if weights is None:
            weights = self.weights
        return np.dot(weights, samples.T) # take the dot product of input with weights

    def fit(self, samples, targets):
        """Apply gradient decent to train a model given training data"""
        self.weights = np.ones(samples.shape[1])

        for epochCount in range(self.epochCap):
            predictions = self.predict(samples, self.weights)

            if not epochCount % 1: # print the loss every 50 epochs
                loss = self.cost(predictions, targets)
                print('Epochs: {}, loss: {}, weights: {}'.format(epochCount, loss, self.weights[:3]))

            gradients = self.calculate_gradients(samples, predictions, targets)
            self.apply_gradients(self.weights, self.lRate, gradients)

    
