from sklearn.ensemble import RandomForestClassifier  
from ai.utils.aiUtils import X_train, y_train

# Random Forest model
randomForestModel = RandomForestClassifier()
randomForestModel.fit(X_train, y_train)
