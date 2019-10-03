from __future__ import division
import numpy as np
from LinearRegressor import LinearRegressor

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

regr = LinearRegressor(lRate= 0.05, epochCap=20000, loggingGap=500)
regr.fit(trainingFeatues, trainingTargets)

predictions = regr.predict(testingFeatures)

