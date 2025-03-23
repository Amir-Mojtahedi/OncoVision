#import libraries
import pandas as pd
import seaborn as sns
import numpy as np

import matplotlib.pyplot as plt

from scipy import stats
from sklearn import metrics
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

from scipy.special import inv_boxcox x

#copy path
csv_url = '/content/drive/MyDrive/AI-Acc.Project/breast cancer dataset/breast-cancer.csv'
# Connect to you Google Drive
from google.colab import drive
drive.mount("/content/drive")

# Reading the CSV data from the specified URL into a DataFrame named 'df'
df = pd.read_csv(csv_url)

# 'df' now contains the data from the CSV file and is ready for further analysis
df

#Analysis

# View first 5 rows of the dataset

df.head()

# Generating descriptive statistics for the dataset
df.describe()

# Displaying concise summary of features in the dataset,
# including the number of non-null values and data types
df.info()

# Checking if there are any missing values (NaN) in the dataset and printing the result
print("\nAre there any missing points in the dataset?:", df.isnull().values.any())

df.isnull().sum()

# Counting the number of duplicated rows in the DataFrame and printing the result
print("Number of Duplicated Rows:", df.duplicated().sum())

# Displaying the dimensions (number of rows and columns) for the dataset
print("Dimensions of the Data:", df.shape)

# Display the first few rows of the dataset to understand its structure
print("First 5 rows of the dataset:")
print(df.head())

# Display the first few rows of the dataset to understand its structure
print("Last 5 rows of the dataset:")
print(df.tail())

# Visualize the distribution of numerical features
numerical_features = ['radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean', 'smoothness_mean',
                      'compactness_mean', 'concavity_mean', 'concave points_mean', 'symmetry_mean',
                      'fractal_dimension_mean', 'radius_se', 'texture_se', 'perimeter_se', 'area_se',
                      'smoothness_se', 'compactness_se', 'concavity_se', 'concave points_se', 'symmetry_se',
                      'fractal_dimension_se', 'radius_worst', 'texture_worst', 'perimeter_worst',
                      'area_worst', 'smoothness_worst', 'compactness_worst', 'concavity_worst',
                      'concave points_worst', 'symmetry_worst', 'fractal_dimension_worst']
df[numerical_features].hist(bins=30, figsize=(15, 16))
plt.suptitle('Histograms of Numerical Features')
plt.show()

# Visualize the distribution of categorical features
categorical_features = ['diagnosis']
for feature in categorical_features:
    plt.figure(figsize=(3, 2))
    df[feature].value_counts().plot(kind='bar', color='skyblue')
    plt.title(f'Distribution of {feature}')
    plt.xlabel(feature)
    plt.ylabel('Count')
    plt.show()

# A higher (darker) value represents higher correlation between the variables
# A lower (lighter) value represents lower correlation between the variables
plt.figure(figsize=(6,5))
df_disp = df.drop(['id', 'diagnosis'], axis=1)
sns.heatmap(df_disp.corr(), cmap='Blues', annot=True);

# Create a figure with three subplots
fig, (ax0, ax1, ax2) = plt.subplots(1, 3, figsize=(20, 5))

# Plot diagnosis vs. radius_mean on the first subplot
sns.lineplot(x='diagnosis', y='radius_mean', data=df, ax=ax0)

# Plot diagnosis vs. perimeter_mean on the second subplot
sns.barplot(x='diagnosis', y='perimeter_mean', data=df, ax=ax1)

# Plot diagnosis vs. smoothness_mean on the third subplot
sns.barplot(x='diagnosis', y='smoothness_mean', data=df, ax=ax2)

# Display the plots
plt.show()

# Visualize the distribution of diagnosis based on radius_mean
plt.figure(figsize=(8, 5))
sns.boxplot(x='diagnosis', y='radius_mean', data=df, palette='Set3')
plt.title('diagnosis vs radius_mean')
plt.show()

# Visualize the distribution of charges based on region
plt.figure(figsize=(10, 6))
sns.boxplot(x='diagnosis', y='perimeter_mean', data=df, palette='viridis')
plt.title('diagnosis vs perimeter_mean')
plt.show()

# Visualize the relationship of diagnosis and smoothness_mean
plt.figure(figsize=(10, 6))
sns.scatterplot(x='diagnosis', y='smoothness_mean', data=df, hue='smoothness_mean', palette='magma', alpha=0.7)
plt.title('diagnosis vs smoothness_mean')
plt.show()

f = plt.figure(figsize=(12, 5))

# First subplot for Malignant
ax1 = f.add_subplot(121)
sns.histplot(df[df.diagnosis == 'M']["radius_mean"], color='c', ax=ax1, kde=True)
ax1.set_title('Relationship of Malignant and radius_mean')

# Second subplot for Benign
ax2 = f.add_subplot(122)
sns.histplot(df[df.diagnosis == 'B']["radius_mean"], color='b', ax=ax2, kde=True)
ax2.set_title('Relationship of Benign and radius_mean')

plt.tight_layout()
plt.show()

sns.catplot(x="diagnosis", kind="count",hue = 'radius_mean', palette="flare", data=df)

sns.jointplot(data=df, x="radius_mean", y="perimeter_mean", hue="diagnosis")

#Select and setup model

# Define the features (X) and target variable (y) for logistic regression
X = df[['radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean', 'smoothness_mean','compactness_mean', 'concavity_mean', 'concave points_mean', 'symmetry_mean',
                     'fractal_dimension_mean', 'radius_se', 'texture_se', 'perimeter_se', 'area_se',
                      'smoothness_se', 'compactness_se', 'concavity_se', 'concave points_se', 'symmetry_se',
                      'fractal_dimension_se', 'radius_worst', 'texture_worst', 'perimeter_worst',
                      'area_worst', 'smoothness_worst', 'compactness_worst', 'concavity_worst',
                      'concave points_worst', 'symmetry_worst', 'fractal_dimension_worst']]
y = df['diagnosis']
X.head()

# Split the dataset into training and testing sets for logistic regression
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=0)

# Instantiate a logistic regression model
logit_model = LogisticRegression(max_iter=500)

# Fit the logistic regression model using the training data
logit_model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = logit_model.predict(X_test)

from sklearn.metrics import accuracy_score

print('Accuracy: ', accuracy_score(y_true=y_test, y_pred=y_pred)*100)

# View a few samples of actual and predicted smoking status ##########################(0,1), (B,M)
num_samples_to_view = 5

for i in range(num_samples_to_view):
    print('===================================================')
    print(f'Test Sample #{i+1}')
    print()
    print(X_test.iloc[[i]])
    print()
    print(f'Actual Diagnosis Variable (0 for B, 1 for M): {y_test.iloc[i]}')
    print(f'Predicted Diagnosis Variable (0 for B, 1 for M): {y_pred[i]}')

    print()

# Generate the Confusion Matrix for this logistic regression model
cm = metrics.confusion_matrix(y_test, y_pred, labels=logit_model.classes_)
disp = metrics.ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=logit_model.classes_)
disp.plot(cmap='Blues')
plt.show();

print(metrics.classification_report(y_test, y_pred, target_names=['B', 'M']));
