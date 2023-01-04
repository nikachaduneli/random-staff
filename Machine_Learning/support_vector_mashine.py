import numpy as np
from sklearn.svm  import LinearSVC, SVC
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

#x->features; y->target
X, y = load_breast_cancer(return_X_y=True)

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=1)

linsvc = LinearSVC(C=0.87, max_iter=100000)

linsvc.fit(X_train,y_train)

print(linsvc.score(X_train,y_train))
print(linsvc.score(X_test,y_test))
