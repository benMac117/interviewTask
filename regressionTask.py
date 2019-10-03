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
features = np.loadtxt(dataFilepath, delimiter=',', skiprows=1)
targets = features[:,-1]
features = features[:,:-1]

# Take a random 10% of the dataset for testing
numSamples = len(targets)
testingIndices = np.random.choice(range(numSamples), int(numSamples/10), replace=False)
trainingIndices = np.setdiff1d(range(numSamples), testingIndices)

trainingFeatues = features[trainingIndices]
trainingTargets = targets[trainingIndices]
testingFeatures = features[testingIndices]
testingTargets = targets[testingIndices]

regr = LinearRegressor()
regr.fit(trainingFeatues, trainingTargets)

predictions = regr.predict(testingFeatures)

# stretch to implement cross-validation