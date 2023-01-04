import numpy as np
import pandas  as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data =pd.read_csv("data.csv",sep=",")

# print(data.head())
print(data.corr())

#SAT იყოს როგორც X  ანუ დამოუკიდებელი ცვლადი და  GPA იყოს როგორც  y  ანუ დამოკიდებული ცვლადი
#plt.scatter(data["SAT"],data["GPA"])

X =data["SAT"].values
X =X.reshape(-1,1)

Y =data["GPA"].values

mymodel =LinearRegression()
mymodel.fit(X,Y)

new_SAT =np.array([[1664]])

predicted_GPA =mymodel.predict(new_SAT)

#0.00165569*1664+0.27504029966028076

# print(predicted_GPA)

predicted_y = mymodel.predict(X)

plt.scatter(data['SAT'],data['GPA'])
plt.plot(X, predicted_y)
plt.show()

print(mymodel.score(X,Y))