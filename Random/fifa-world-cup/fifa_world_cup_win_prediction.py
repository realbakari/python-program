import csv
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# Load the data from the CSV file into a pandas DataFrame
df = pd.read_csv('fifa-world-cup-2022.csv')

# Remove rows with missing values
df = df.dropna()

# Scale the features using standard scaling
df = (df - df.mean(numeric_only=True)) / df.std(numeric_only=True)

# Print the names of the columns in the DataFrame
print(df.columns)

# Select the columns to use as the features and labels
X = df[['Match Number','Round Number','Date','Location','Home Team','Away Team','Group','Result']]
y = df['correct_column_name']

# Split the data into a training set (80%) and a test set (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Create a logistic regression model
model = LogisticRegression()

# Train the model on the training data
model.fit(X_train, y_train)

# Make predictions on the test data
y_pred = model.predict(X_test)

# Evaluate the model's performance using the accuracy metric
accuracy = accuracy_score(y_test, y_pred)
print('Model accuracy:', accuracy)

# Load the data on the teams that are likely to participate in the 2022 World Cup
df = pd.read_csv('fifa-world-cup-2022.csv')

# Preprocess the data by removing missing values and scaling the features
df = df.dropna()
df = (df - df.mean(numeric_only=True)) / df.std(numeric_only=True)

# Make predictions on the teams using the trained model
y_pred = model.predict(df)

# Print the predicted labels for the teams
print(y_pred)
