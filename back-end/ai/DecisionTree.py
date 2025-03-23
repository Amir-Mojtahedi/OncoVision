import pandas as pd
import seaborn as sns
import numpy as np

import matplotlib.pyplot as plt

from scipy import stats
from sklearn.metrics import accuracy_score
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

from scipy.special import inv_boxcox

csv_url = '/breast-cancer.csv' #Make sure in your personal drive, you have a folder called ai_accel and upload the breask-cancer.csv file there
from google.colab import drive
drive.mount('/content/drive')
df = pd.read_csv(csv_url)

from sklearn import tree
df['diagnosis_encode'] = LabelEncoder().fit_transform(df['diagnosis'])
# Define the features (X) and target variable (y) for decision tree
X = df.drop(['id', 'diagnosis', 'diagnosis_encode'], axis=1)
y = df['diagnosis_encode']
X.head()

# Split the dataset into training and testing sets for decision tree
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#instantial model
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X_train, y_train)

# Make predictions on the test set
y_pred = clf.predict(X_test)

from sklearn.metrics import accuracy_score

print('Accuracy: ', accuracy_score(y_true=y_test, y_pred=y_pred)*100)

# View a few samples of actual and predicted diagnosis
sample_to_view = 10

for i in range(sample_to_view):
    #print(X_test.iloc[[i]])
    print(f"Actual diagnosis: {y_test.iloc[i]}, Predicted diagnosis: {y_pred[i]}")
