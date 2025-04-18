from sklearn.svm import SVC
from ai.utils.aiUtils import X_train, y_train

# SVM model
svmModel = SVC()
svmModel.fit(X_train, y_train)