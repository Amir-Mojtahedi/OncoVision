import os
from sklearn.tree import DecisionTreeClassifier
from ai.utils.aiUtils import X_train, y_train
import pickle

print("Training Decision Tree model...")
# Decision Tree model
decisionTreeModel = DecisionTreeClassifier()
decisionTreeModel.fit(X_train, y_train)

print("Decision Tree model trained and saved to the disk.")
# Save the model to disk
base_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(base_dir, '..', '..', 'models', 'decision_tree_model.sav')
filename = os.path.abspath(model_path)

# Save the model
pickle.dump(decisionTreeModel, open(filename, 'wb'))
