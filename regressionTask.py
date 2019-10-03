from __future__ import division
import numpy as np
from LinearRegressor import LinearRegressor

# Load the features and targets from the .csv
dataFilepath = '/home/ben/Data/morsum/avocadoCleaned.csv'
features = np.loadtxt(dataFilepath, delimiter=',', skiprows=1)
targets = features[:,-1]
features = features[:,:-1]

# Take a random 10% of the dataset for testing
# In a real setting I would apply cross-validation instead
numSamples = len(targets)
testingIndices = np.random.choice(range(numSamples), int(numSamples/10), replace=False)
trainingIndices = np.setdiff1d(range(numSamples), testingIndices)

trainingFeatues = features[trainingIndices]
trainingTargets = targets[trainingIndices]
testingFeatures = features[testingIndices]
testingTargets = targets[testingIndices]

# Create and train the regression model with the training data
# I chose these hyperparameters after a little manual experimentation plotting the training loss
regr = LinearRegressor(lRate=0.05, epochCap=20000, loggingGap=500)
trainingLosses = regr.fit(trainingFeatues, trainingTargets)

for lossEntry in trainingLosses:
    print(lossEntry)

predictions = regr.predict(testingFeatures)
output = vstack(testingTargets, predictions)
np.savetxt('/home/ben/Data/morsum/', output, delimiter=',')