from __future__ import division
import numpy as np

class LinearRegressor:
    def predict(self, X):
        #throw error if weights don't exist yet
        return np.dot(X, self.weights) # take the dot product of input with weights

    def cost(self, yPred, yTrue):
    	print(abs(yTrue - yPred).shape)
        return np.mean((1-yTrue) + yPred - yPred*2*(1-yTrue))

    def fit(self, X, y):
        self.weights = np.zeros(X.shape[1])

        for epochCount in range(self.epochCap):
            yPred = self.predict(X)

            gradients = self.calculate_gradient

dataFilepath = '/home/ben/Data/morsum/avocadoCleaned.csv'
data = np.loadtxt(dataFilepath, delimiter=',', skiprows=1)
targets = data[:,-1]
data = data[:,:-1]
print(targets.shape)
print(data.shape)
print(targets[0])
print(data[0])
