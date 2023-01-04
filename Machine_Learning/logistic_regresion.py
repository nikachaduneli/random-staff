# from sklearn.linear_model import LogisticRegression
# from sklearn.datasets import load_breast_cancer
# from sklearn.model_selection import (
#             train_test_split, 
#             cross_val_score, 
#             cross_validate )



# X, y = load_breast_cancer(return_X_y=True)

# X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.4)

# mymodel = LogisticRegression(max_iter=5000)
# mymodel.fit(X_train,y_train)

# scores = cross_val_score(mymodel, X, y, scoring='accuracy', cv=10)


from sklearn.datasets import load_breast_cancer
from sklearn.metrics import accuracy_score,confusion_matrix
import time
t = time.time()
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
from  sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

X ,y =load_breast_cancer(return_X_y=True)

X_train,X_test,y_train,y_test =train_test_split(X,y,test_size=0.3,random_state=7)

mymodel =LogisticRegression(max_iter=6000,C=0.07,class_weight={0:0.4,1:0.6})

parameters={"C":[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.1]}

hybrid_model =GridSearchCV(mymodel,parameters,scoring='accuracy',n_jobs=-1,cv=5)

hybrid_model.fit(X_train,y_train)

print(hybrid_model.best_params_,hybrid_model.best_score_)

print(hybrid_model.score(X_test,y_test))

print('seconds' ,time.time()-t)
