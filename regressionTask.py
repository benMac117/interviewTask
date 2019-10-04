from __future__ import division
import numpy as np
from LinearRegressor import LinearRegressor
from os.path import expanduser

# If I couldn't use the os package I would either put everything in the same directory
# or use explicit paths everywhere
homeDir = expanduser('~') 
# Load the features and targets from the .csv
dataFilepath = '{}/Data/morsum/avocadoCleaned.csv'.format(homeDir)
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
regr = LinearRegressor(lRate=0.05, epochCap=15000, loggingGap=500)
trainingLosses, weights = regr.fit(trainingFeatues, trainingTargets)

# Print training loss over time
for lossEntry in trainingLosses:
    print('Epoch: {}, loss: {}'.format(lossEntry[0], lossEntry[1]))

# I would like to use a library for the logging rather than a csv
np.savetxt('{}/Data/morsum/training2.csv'.format(homeDir), trainingLosses, delimiter=',')

# I would normally pickle this type of variable
np.savetxt('{}/Data/morsum/model2.csv'.format(homeDir), weights, delimiter=',')

# Make price predictions and save alongside ground truth
predictions = regr.predict(testingFeatures)
output = np.vstack((testingTargets, predictions))
np.savetxt('{}/Data/morsum/output2.csv'.format(homeDir), output, delimiter=',')