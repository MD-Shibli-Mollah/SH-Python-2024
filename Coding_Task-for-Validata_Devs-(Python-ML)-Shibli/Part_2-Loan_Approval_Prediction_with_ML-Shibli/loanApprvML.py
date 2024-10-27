import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (accuracy_score, precision_score, recall_score, 
                             f1_score, confusion_matrix)
import io
import matplotlib.pyplot as plt

# Specify the path to the output text file
output_file_path = "E:\\Python Projects for Validata\\Coding_Task-for-Validata_Devs-(Python-ML)-Shibli\\Part_2-Loan_Approval_Prediction_with_ML-Shibli\\output.txt"

# Function to load the data from a CSV file
def load_data(file_path):
    try:
        data = pd.read_csv(file_path)  # Load data into a DataFrame
        data.columns = data.columns.str.strip()  # Strip whitespace from column names
        return data
    except Exception as e:
        print(f"Error loading data: {e}")  # Print an error message if loading fails
        return None

# Function to preprocess the data
def preprocess_data(data):
    # Label encode the 'employment_status' column to convert categorical data to numerical
    data['employment_status'] = LabelEncoder().fit_transform(data['employment_status'])
    
    # Separate the features (X) and the target variable (y)
    X = data.drop('loan_approved', axis=1)  # Features
    y = data['loan_approved']  # Target variable
    
    # Scale numerical features to standardize them
    scaler = StandardScaler()
    X[['income', 'credit_score', 'loan_amount', 'loan_term']] = scaler.fit_transform(X[['income', 'credit_score', 'loan_amount', 'loan_term']])
    
    return X, y  # Return the preprocessed features and target

# Function to evaluate a model's performance using various metrics
def evaluate_model(y_true, y_pred, model_name, file):
    file.write(f"Evaluation Metrics for {model_name}\n")
    # Write evaluation metrics to the output file
    file.write(f"Accuracy: {accuracy_score(y_true, y_pred)}\n")
    file.write(f"Precision: {precision_score(y_true, y_pred)}\n")
    file.write(f"Recall: {recall_score(y_true, y_pred)}\n")
    file.write(f"F1 Score: {f1_score(y_true, y_pred)}\n")
    file.write(f"Confusion Matrix:\n{confusion_matrix(y_true, y_pred)}\n\n")

# Main Execution
with open(output_file_path, "w") as file:
    # Step 1: Load and Explore the Data
    data = load_data("E:\\Python Projects for Validata\\Coding_Task-for-Validata_Devs-(Python-ML)-Shibli\\Part_2-Loan_Approval_Prediction_with_ML-Shibli\\loan_data.csv")
    if data is not None:
        # Write data information to the output file
        data.info(buf=io.StringIO())
        file.write("Data Information:\n" + io.StringIO().getvalue() + "\n\n")
        file.write("Column names in dataset:\n" + str(data.columns) + "\n\n")
        file.write("First few rows of data:\n" + str(data.head()) + "\n\n")

        # Step 2: Preprocess the Data
        X, y = preprocess_data(data)  # Preprocess data to get features and target

        # Split the dataset into training and test sets (80% train, 20% test)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Step 3: Train KNN Model
        knn = KNeighborsClassifier(n_neighbors=5)  # Initialize KNN classifier with 5 neighbors
        knn.fit(X_train, y_train)  # Train the KNN model
        y_pred_knn = knn.predict(X_test)  # Make predictions on the test set

        # Step 4: Train Decision Tree Model
        dt = DecisionTreeClassifier(max_depth=5)  # Initialize Decision Tree classifier with a maximum depth of 5
        dt.fit(X_train, y_train)  # Train the Decision Tree model
        y_pred_dt = dt.predict(X_test)  # Make predictions on the test set

        # Step 5: Evaluate Models
        evaluate_model(y_test, y_pred_knn, "KNN", file)  # Evaluate the KNN model
        evaluate_model(y_test, y_pred_dt, "Decision Tree", file)  # Evaluate the Decision Tree model

        # Step 6: Feature Importance (Decision Tree Only)
        feature_importances = pd.DataFrame({'Feature': X.columns, 'Importance': dt.feature_importances_})  # Create DataFrame for feature importances
        feature_importances = feature_importances.sort_values(by='Importance', ascending=False)  # Sort by importance

        file.write("Feature Importances:\n" + str(feature_importances) + "\n\n")  # Write feature importances to the output file

        # Optional: Visualize feature importance
        feature_importances.plot(kind='bar', x='Feature', y='Importance')  # Create a bar plot for feature importances
        plt.title('Feature Importances from Decision Tree')  # Title for the plot
        plt.savefig("E:\\Python Projects for Validata\\Coding_Task-for-Validata_Devs-(Python-ML)-Shibli\\Part_2-Loan_Approval_Prediction_with_ML-Shibli\\feature_importances.png")  # Save the plot as a PNG file

        # Save the preprocessed dataset to a new CSV file
        data.to_csv('E:\\Python Projects for Validata\\Coding_Task-for-Validata_Devs-(Python-ML)-Shibli\\Part_2-Loan_Approval_Prediction_with_ML-Shibli\\preprocessed_loan_data.csv', index=False)
