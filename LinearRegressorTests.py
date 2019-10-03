# If this task was not restricted to numpy, I would be using unittest here rather than unenforced functions
import numpy as np
from LinearRegressor import LinearRegressor

regr = LinearRegressor()

# Testing the cost function
costTest1 = regr.cost(np.array([1, 2, 3]), np.array([3, 2, 7]))
costTest2 = regr.cost(np.array([1.5, 2000, 3, 11]), np.array([3, 2, 7, 11]))
costTest3 = regr.cost(np.array([100, 2, 3]), np.array([3, 200, 7]))
print('cost tests: 2/{}, 500.875/{}, 99.667.../{}'.format(costTest1, costTest2, costTest3))
 
# Testing the calculate_gradients function
gradTest1 = regr.calculate_gradients(np.array([1, 2, 3]), np.array([3, 2, 7]), np.array([3, 2, 7]))
gradTest2 = regr.calculate_gradients(np.array([1.5, 2000, 3, 11]), np.array([3, 2, 7, 11]), np.array([3, 2, 7, 10]))
gradTest3 = regr.calculate_gradients(np.array([100, 2, 3]), np.array([3, 200, 7]), np.array([-30, 202, -70]))
print('calculate_gradients tests: 0/{}, 2.75/{}, 1175/{}'.format(gradTest1, gradTest2, gradTest3))

# Testing the apply_gradients function
gradApplyTest1 = regr.apply_gradients(np.array([1, 2, 3]), 0.1, np.array([3, 2, 7]))
gradApplyTest2 = regr.apply_gradients(np.array([1.5, 2000, 3, 11]), 10, np.array([3, 2, 7, 10]))
gradApplyTest3 = regr.apply_gradients(np.array([100, 2, 3]), 0.01, np.array([-30, 202, -70]))
print('apply_gradients tests: [0.7, 1.8, 2.3]/{}, [-28.5, 1980, -67, -89]/{}, [100.3, -0.02, 3.7]/{}'.format(gradApplyTest1, gradApplyTest2, gradApplyTest3))

# Testing the predict function
prediction1 = regr.predict(np.array([1, 2, 3]), np.array([1, -1.1, 0.2]))
prediction2 = regr.predict(np.array([1.5, 2000, 3, 11]), np.array([-0.3, 2, -2, 0.1]))
prediction3 = regr.predict(np.array([100, 2, 3]), np.array([0.01, -0.75, 1.4]))
print('predict tests: -0.6/{}, 3994.65/{}, 3.7/{}'.format(prediction1, prediction2, prediction3))
