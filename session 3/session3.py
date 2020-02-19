"""
    Import data and divide them into predictors and outcomes measures to be used
    in subsequent regression anallysis
"""
import pandas as pd
df = pd.read_csv('data.csv')
X = df.iloc[:,0:13]
y = df.iloc[:,-1]


"""
    Some visualizations on the input dataset using the two common data visualiztion
    modules in Python: matplotlib and seaborn
"""
import matplotlib.pyplot as plt
plt.figure(figsize=(5, 4))
plt.hist(y, bins = 30)
plt.title('Boston Housing Prices and Count Histogram')
plt.xlabel('price ($1000s)')
plt.ylabel('count')

import seaborn as sns
plt.figure()
sns.distplot(y, bins=30)
plt.show()


for label in X.columns:
    plt.figure(figsize=(5, 4))
    plt.scatter(X[label], y)
    plt.ylabel('Price', size=12)
    plt.xlabel(label, size=12)


plt.figure()
correlation_matrix = df.corr().round(2)
sns.heatmap(correlation_matrix, cmap="YlGnBu",annot=True)
plt.show()


"""
    Import statmodels module to perform standard statistical analysis. We will
    first conduct a univariate regression analysis and then perfrom a multivariate
    one.
"""
import statsmodels.api as sm
model = sm.OLS(y, X['RM']) #Here we tell Python that X and y will be put into an ordinary least square model
results = model.fit() #Here we tell Python to use the given X and y data and fit a model
print(results.summary()) #This will print a summary of the obtained statistical model
print(results.params) #This will print only coefficients of each predictors in the regression model
preds = results.predict(X['RM']) #This will compute predicted outcome measures using the obtained regression model
plt.figure() #plotting the obtained results
plt.scatter(X['RM'],y,hold='on')
plt.plot(X['RM'],preds,color='red',linestyle='-.')


model = sm.OLS(y, X).fit() #The difference between this section and the one above is that here we incorporate all columns of X, and thus this is a multivariate regression.
print(model.summary())
preds = model.predict(X)


"""
    Below is a very brief introduction to the dataflow in a standard maching 
    learning problem.
"""

train = df.sample(frac = 0.8, random_state = 42) #We will first divid the whole dataset into train and test subsets. As an example, 80% of data is given to the train and the rest to test.
test = df.drop(train.index)
trainX = train.iloc[:,0:13]
trainY = train.iloc[:,-1]
testX = test.iloc[:,0:13]
testY = test.iloc[:,-1]

"""
    Training a linear regression model, this time using the SciKit Learn module.
    This module is the most common module for maching learnining in Python. The 
    difference between the linear regression model obtained here and the one in 
    the above section is that, here the empahsis in on the accuracy of predictions
    while in the above, we had various inferential stastics handy to conduct 
    statistical interpretations.
"""
from sklearn import linear_model
model = linear_model.LinearRegression()
model.fit(trainX, trainY)
preds = model.predict(testX)

"""
    Here we use some of the most common factors used to evaluate the effectiveness
    of a standard regression model in maching learning.
"""
from sklearn.metrics import mean_squared_error, r2_score
param1 = mean_squared_error(testY, preds)
param2 = r2_score(testY, preds)
print('mean squared error is:', param1)
print('R2 is:', param2)
print('coefficients are', model.coef_)

"""
    Below we repeat the same process above, but instead of usig a linear regression
    model, we use some more advanced maching learning models such as decision tree.
"""
from sklearn.tree import DecisionTreeRegressor
model = DecisionTreeRegressor(max_depth=5)
model.fit(trainX, trainY)
preds = model.predict(testX)

param1 = mean_squared_error(testY, preds)
param2 = r2_score(testY, preds)
print('mean squared error is:', param1)
print('R2 is:', param2)
