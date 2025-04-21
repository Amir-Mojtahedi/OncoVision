from sklearn.tree import DecisionTreeClassifier
from ai.utils.aiUtils import X_train, y_train
import pickle

print("Training Decision Tree model...")
# Decision Tree model
decisionTreeModel = DecisionTreeClassifier()
decisionTreeModel.fit(X_train, y_train)

print("Decision Tree model trained and saved to the disk.")
# Save the model to disk
filename = './ai/models/decision_tree_model.sav'
pickle.dump(decisionTreeModel, open(filename, 'wb'))
