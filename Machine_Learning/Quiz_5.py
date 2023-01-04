from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split   
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score

X, y = make_classification(n_samples=4000, n_features=30, n_informative=10, n_redundant=20)

##ნაწილი პირველი

scores = {}
mymodel = DecisionTreeClassifier()

for i in range(3):

  X_train,X_test, y_train, y_test = train_test_split(X,y,test_size=0.35, random_state=i)

  mymodel.fit(X_train, y_train)

  scores[f'random_state = {i}'] = mymodel.score(X_test, y_test) 

print(f'ქულები random_state-ის ცვლილებისას:\n{scores}')

#ნაწილი მეორე

cross_val_score_scores = cross_val_score(mymodel, X, y, scoring='accuracy', cv=10)
print(f'საშუალო ქულა:\n {cross_val_score_scores.mean()}')
