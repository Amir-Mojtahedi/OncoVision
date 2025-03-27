import os
import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler
import joblib

# Load the dataset (ensure the path is correct)
data_path = os.path.join(os.getcwd(), 'back-end', 'ai', 'breast-cancer.csv')
df = pd.read_csv(data_path)

# Preprocess the data:
# Convert diagnosis labels to numeric (M: malignant=1, B: benign=0)
df["diagnosis"] = df["diagnosis"].map({"M": 1, "B": 0})
df.drop(columns=["id"], inplace=True)  # Remove the ID column

# Separate features and target variable
X = df.drop(columns=["diagnosis"])
y = df["diagnosis"]

# Scale the features using StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split the data into training and testing sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Function to train and evaluate an SVM model
def train_svm(X_train, X_test, y_train, y_test, kernel="rbf", save_model=False, model_name="svm_model.pkl"):
    # Set up SVM parameters based on the kernel choice
    if kernel == "poly":
        model = SVC(kernel=kernel, degree=2, C=1.0, gamma=0.005, class_weight={0: 1, 1: 2.5})
    else:
        model = SVC(kernel=kernel, C=10.0, gamma=0.005, class_weight={0: 1, 1: 2.5})
    
    # Train the model on the training data
    model.fit(X_train, y_train)
    
    # Predict on the test set and calculate accuracy
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    
    # Save the model if specified
    if save_model:
        joblib.dump(model, model_name)
    
    return model, acc, y_pred

# Train SVM on all features and save the model to 'svm_all_features.pkl'
svm_model, accuracy, y_pred = train_svm(X_train, X_test, y_train, y_test, save_model=True, model_name="svm_all_features.pkl")

# Print model performance
# print(f"SVM Model (all features) Accuracy: {accuracy * 100:.2f}%")
# print(classification_report(y_test, y_pred))
