import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = pd.read_csv('data.csv',sep=',')

X = data['SAT'].values
y = data['GPA'].values

def fit_line_2d(X, y):

  X_mean = np.average(X)
  y_mean = np.average(y)

  k = np.sum((X - X_mean)*(y - y_mean)) / np.sum((X - X_mean)**2)

  b = y_mean - k * X_mean 

  line = k * X + b

  plt.scatter(X, y)
  plt.plot(X, line)
  plt.show()

fit_line_2d(X,y)  