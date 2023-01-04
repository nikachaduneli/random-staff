import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from  sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

data = pd.read_csv('Data.csv', sep=',')

# კორელაცია სიტყვით როგორ უნდა აღწერო არვიცი მარა რო დაიბეჭდება ჩანს სად არი >0.75
print(data.corr())

X = data.drop('Y', axis=1)
y = data['Y'].values

scores = []
exp_variance = []


X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.3, random_state=1)

#სტანდარტიზაცია
myscalar = StandardScaler()
X_train = myscalar.fit_transform(X_train)
X_test = myscalar.transform(X_test)

for i in range(1,X.shape[1]+1):

  #განზომილებებეის შემცირება i სვეტამდე
  mypca = PCA(n_components=i)
  new_X_train = mypca.fit_transform(X_train)
  new_X_test = mypca.transform(X_test)

  exp_variance.append(np.sum(mypca.explained_variance_ratio_))

  mymodel = LinearRegression()
  mymodel.fit(new_X_train,y_train)

  score = mymodel.score(new_X_test,y_test)
  scores.append(score)

#ყვითლად გამოჩნდება exp_variance, მწვანედ ქულები 
plt.plot(range(1, X.shape[1]+1), exp_variance, c='y')
plt.plot(range(1, X.shape[1]+1), scores, c='g')
plt.show()

#შვიდივე სვეტის გამოყენების დროს გვაქ ყველაზე კარგი შედეგი. 




