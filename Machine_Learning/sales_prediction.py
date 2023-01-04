from os import lseek
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import seaborn as sns


data = pd.read_csv('https://raw.githubusercontent.com/pramodini18/Simple-Linear-Regression/master/advertising.csv',sep=',')

# print(data.head())
print(data.corr())

y = data["Sales"]
X = data.drop('Sales',axis=1).values

mymodel = LinearRegression()
mymodel.fit(X,y)
print(mymodel.coef_)

print(mymodel.score(X,y))

sns.pairplot(data,x_vars=['TV','Radio','Newspaper'],y_vars='Sales',kind='scatter',height=5)