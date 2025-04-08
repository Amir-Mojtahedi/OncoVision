from sklearn.tree import DecisionTreeClassifier
from ai.utils.aiUtils import X_train, y_train

# Decision Tree model
decisionTreeModel = DecisionTreeClassifier()
decisionTreeModel.fit(X_train, y_train)


