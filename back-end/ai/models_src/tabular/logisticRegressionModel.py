import os
from sklearn.linear_model import LogisticRegression
from ai.utils.aiUtils import X_train, y_train
import pickle

print("Training Logistic Regression model...")
# Logistic Regression model
logisticRegressionModel = LogisticRegression()
logisticRegressionModel.fit(X_train, y_train)

print("Logistic Regression model trained and saved to the disk.")
# Save the model to disk
base_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(base_dir, '..', '..', 'models', 'logistic_model.sav')
filename = os.path.abspath(model_path)

# Save the model
pickle.dump(logisticRegressionModel, open(filename, 'wb'))
