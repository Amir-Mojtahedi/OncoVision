from sklearn.ensemble import RandomForestClassifier  
from ai.utils.aiUtils import X_train, y_train
import pickle

print("Training Random Forest model...")
# Random Forest model
randomForestModel = RandomForestClassifier()
randomForestModel.fit(X_train, y_train)

print("Random Forest model trained and saved to the disk.")
# Save the model to disk
filename = './ai/models/random_forest_model.sav'
pickle.dump(randomForestModel, open(filename, 'wb'))
