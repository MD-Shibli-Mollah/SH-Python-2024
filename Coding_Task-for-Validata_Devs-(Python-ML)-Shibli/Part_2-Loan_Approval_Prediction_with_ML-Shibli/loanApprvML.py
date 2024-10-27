import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

# Step 1: Load and Explore the Data
data = pd.read_csv('loan_data.csv')  # Assume data is in 'loan_data.csv'
print(data.head())
print(data.info())

# Step 2: Preprocess the Data
# Encoding categorical features
data['employment_status'] = LabelEncoder().fit_transform(data['employment_status'])
X = data.drop('loan_approved', axis=1)
y = data['loan_approved']

# Scaling numerical features
scaler = StandardScaler()
X[['income', 'credit_score', 'loan_amount', 'loan_term']] = scaler.fit_transform(X[['income', 'credit_score', 'loan_amount', 'loan_term']])

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Train KNN Model
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
y_pred_knn = knn.predict(X_test)

# Step 4: Train Decision Tree Model
dt = DecisionTreeClassifier(max_depth=5)
dt.fit(X_train, y_train)
y_pred_dt = dt.predict(X_test)

# Step 5: Evaluate Models
def evaluate_model(y_true, y_pred, model_name):
    print(f"Evaluation Metrics for {model_name}")
    print("Accuracy:", accuracy_score(y_true, y_pred))
    print("Precision:", precision_score(y_true, y_pred))
    print("Recall:", recall_score(y_true, y_pred))
    print("F1 Score:", f1_score(y_true, y_pred))
    print("Confusion Matrix:\n", confusion_matrix(y_true, y_pred))
    print("\n")

evaluate_model(y_test, y_pred_knn, "KNN")
evaluate_model(y_test, y_pred_dt, "Decision Tree")

# Step 6: Feature Importance (Decision Tree Only)
feature_importances = pd.DataFrame({'Feature': X.columns, 'Importance': dt.feature_importances_})
feature_importances = feature_importances.sort_values(by='Importance', ascending=False)
print("Feature Importances:\n", feature_importances)

# Save the preprocessed dataset and results
data.to_csv('preprocessed_loan_data.csv', index=False)
