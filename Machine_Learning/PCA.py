import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot  as plt

data =pd.read_csv("https://raw.githubusercontent.com/Statology/Python-Guides/main/mtcars.csv",sep=",")
data = data[["mpg", "disp", "drat", "wt", "qsec", "hp"]]


y =data["hp"].values
X =data.drop("hp",axis=1).values

# print(X.shape)
n_columns =X.shape[1]
explained_variance =[]
scores =[]


X_train,X_test,y_train,y_test =train_test_split(X,y,test_size=0.3,random_state=1)

myscaler =StandardScaler()

X_train =myscaler.fit_transform(X_train)
X_test =myscaler.transform(X_test)

for i in range(1,n_columns+1):
 
    myPCA =PCA(n_components=i)
    
    X_train_updated =myPCA.fit_transform(X_train)
    X_test_updated =myPCA.transform(X_test)

    print(X_train_updated,'\n')
    
    explained_variance.append(np.sum(myPCA.explained_variance_ratio_))
    
    mymodel =LinearRegression()

    mymodel.fit(X_train_updated,y_train)
   
    scores.append(mymodel.score(X_test_updated,y_test))

# plt.plot(range(n_columns),explained_variance)
# plt.plot(range(n_columns),scores)
# plt.show()