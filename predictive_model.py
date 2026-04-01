from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import numpy as np
import pandas as pd

# Set display options to see all columns
pd.set_option('display.max_columns', None)

# Loading the dataset from your specified location
Data = r"C:\Users\USER\Desktop\sales_data\GLOBAL SALES DATA.csv"
df = pd.read_csv(Data)

# Creating the target variable: 
# If Quantity is negative, it's a 'Refund'; otherwise, it's a 'Purchase'
df['Transaction_Type'] = np.where(df['Quantity'] < 0, 'Refund', 'Purchase')

# Convert Quantity to absolute values for training
df['Quantity'] = df['Quantity'].abs()

# Separate features and target variable
X = df[['Quantity', 'Unit_Price']] 
y = df['Transaction_Type'] # Target variable

# Split the dataset into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LogisticRegression()
model.fit(X_train, y_train)
print('This training is successful. The model has learned the pattern')

# Make predictions on the test set
y_predict = model.predict(X_test)
print(f'The predicted values are: {y_predict}')

# Calculate and print the accuracy score
score = accuracy_score(y_test, y_predict)
print(f'The accuracy of the model is: {score}')

# --- Example Usage 1 ---
new_transaction = np.array([[5, 500]]) 
prediction = model.predict(new_transaction)

if prediction[0] == 'Purchase':
    print("The model predicts this is a legitimate sale")
else:
    print("The model predicts this is a refund transaction")

# --- Example Usage 2 ---
new_transaction2 = np.array([[1, 0]]) 
prediction2 = model.predict(new_transaction2)

if prediction2[0] == 'Purchase':
    print("The model predicts this is a legitimate sale")
else:
    print("The model predicts this is a refund transaction")
