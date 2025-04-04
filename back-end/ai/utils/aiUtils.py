import os
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv(f'{os.getcwd()}/ai/breast-cancer.csv')
df.drop(['id'], axis=1, inplace=True)
df['diagnosis'] = LabelEncoder().fit_transform(df['diagnosis'])

# Compute correlation of features with target
correlation = df.corr()['diagnosis'].abs().sort_values(ascending=False)
top_5_features = correlation[1:6]  # Exclude the target itself

# Separate our predictors and target
top_5 = top_5_features.index.tolist()  # Get column names as a list
X = df[top_5]  # Select only these columns
y = df['diagnosis']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split the data into training set and testing set
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.25, random_state=42)
