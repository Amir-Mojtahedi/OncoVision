import os
from sklearn.ensemble import RandomForestClassifier  
from ai.utils.aiUtils import X_train, y_train
import pickle

print("Training Random Forest model...")
# Random Forest model
randomForestModel = RandomForestClassifier()
randomForestModel.fit(X_train, y_train)

print("Random Forest model trained and saved to the disk.")
# Save the model to disk
base_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(base_dir, '..', '..', 'models', 'random_forest_model.sav')
filename = os.path.abspath(model_path)

# Save the model
pickle.dump(randomForestModel, open(filename, 'wb'))
