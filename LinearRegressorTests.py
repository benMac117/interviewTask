# If this task was not restricted to numpy, I would be using unittest here rather than unenforced functions
import numpy as np
from LinearRegressor import LinearRegressor

regr = LinearRegressor()

costTest1 = regr.cost(np.array([1,2,3]), np.array([3,2,7]))
costTest2 = regr.cost(np.array([1.5,2000,3,11]), np.array([3,2,7,11]))
costTest3 = regr.cost(np.array([100,2,3]), np.array([3,200,7]))

print('Cost tests: 2/{}, 500.875/{}, 99.667.../{}'.format(costTest1, costTest2, costTest3))