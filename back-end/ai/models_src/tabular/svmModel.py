import os
from sklearn.svm import SVC
from ai.utils.aiUtils import X_train, y_train
import pickle


print("Training SVM model...")
# SVM model
svmModel = SVC()
svmModel.fit(X_train, y_train)

print("SVM model trained and saved to the disk.")
# Save the model to disk
base_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(base_dir, '..', '..', 'models', 'svm_model.sav')
filename = os.path.abspath(model_path)

# Save the model
pickle.dump(svmModel, open(filename, 'wb'))
