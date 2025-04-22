from sklearn.svm import SVC
from ai.utils.aiUtils import X_train, y_train
import pickle


print("Training SVM model...")
# SVM model
svmModel = SVC()
svmModel.fit(X_train, y_train)

print("SVM model trained and saved to the disk.")
# Save the model to disk
filename = './ai/models/svm_model.sav'
pickle.dump(svmModel, open(filename, 'wb'))
