from sklearn.linear_model import LogisticRegression
from ai.utils.aiUtils import X_train, y_train
import pickle

print("Training Logistic Regression model...")
# Logistic Regression model
logisticRegressionModel = LogisticRegression()
logisticRegressionModel.fit(X_train, y_train)

print("Logistic Regression model trained and saved to the disk.")
# Save the model to disk
filename = './ai/models/logistic_model.sav'
pickle.dump(logisticRegressionModel, open(filename, 'wb'))
