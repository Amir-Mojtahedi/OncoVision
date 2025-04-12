from sklearn.linear_model import LogisticRegression
from ai.utils.aiUtils import X_train, y_train

# Logistic Regression model
logisticRegressionModel = LogisticRegression()
logisticRegressionModel.fit(X_train, y_train)
