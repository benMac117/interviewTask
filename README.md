# Interview coding task

I used Python 2.7 for these tasks.

# Task One - Linear Regression
I first used a Jupyter Notebook ('Data Exploration.ipynb') to examine and reshape the data to my needs. The cleaned dataset has not been included in this repository but can be added upon request. LinearRegressor.py holds the class with my implementation of multiple linear regression. I created a small set of tests for this class in LinearRegressorTests.py. I ran a separate Python script (regressionTask.py) to load the cleaned data, perform the regression, and save the results. Finally, I performed my analysis of the results and the regression model in 'Results Analysis.ipynb'.

I am happy with how I reorganised and cleaned the dataset, and with how I have analysed my results. I was hoping for a model which explained a higher portion of the variance, this may be achieved with a different encoding of the categorical features, using a different loss function, or perhaps applying a different method of normalisation.


# Task Two - REST API
I implemented my API in the myService.py script, and created a set of tests in myServiceTests.py. In terms of running this on another machine, a MYSQL user must be created with the name 'ben' and the password pickled in a local file named 'config'. In addition, a database must be created named recipeBook.

I believe I have effectly implemented the requirements for the task, but I am not very happy with the script itself. This is my first time using Flask and SQLAlchemy so I have not produced a very well structured or maintainable codebase in my opinion, I would like to spend more time working with these frameworks and improving my understanding here. In particular I would like to move the database models to a separate file and reorganise the routing (perhaps with flask-restful). In both cases my main difficulty was with the db object, in ensuring it would be available in other files as needed.
