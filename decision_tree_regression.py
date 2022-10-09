# -*- coding: utf-8 -*-
"""decision_tree_regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aMR0zekbfv90TOtY-wp0tf1auEZYxuXa

# Decision Tree Regression

## Importing the libraries
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""## Importing the dataset"""

dataset=pd.read_csv('POSITI~1.CSV')
X=dataset.iloc[:,1:2].values
y=dataset.iloc[:,-1].values

print(X)
print(y)

"""## Training the Decision Tree Regression model on the whole dataset"""

from sklearn.tree import DecisionTreeRegressor
regressor=DecisionTreeRegressor(random_state=0)
regressor.fit(X,y)

"""## Predicting a new result"""

print(regressor.predict([[6.5]] ))

"""## Visualising the Decision Tree Regression results (higher resolution)"""

X_grid=np.arange(min(X),max(X),0.1)
X_grid=X_grid.reshape(len(X_grid),1)
plt.scatter(X,y,color='red')
plt.plot(X_grid,regressor.predict(X_grid),color='green')
plt.xlabel('Years of experience')
plt.ylabel('salary')
plt.show()