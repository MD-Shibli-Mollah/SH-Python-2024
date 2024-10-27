# Part 2 (Machine Learning – Python): Predicting Loan Approval Using KNN and Decision Trees

This project aims to predict loan approval decisions based on K-Nearest Neighbors (KNN) and Decision Trees. The dataset contains information about loan applicants, including income, credit score, employment status, loan amount, and loan term.

## Table of Contents
- [Technologies Used](#technologies-used)
- [Prerequisites](#Prerequisites)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Evaluation Metrics](#evaluation-metrics)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Technologies Used
- Python 3.x
- Pandas
- NumPy
- Scikit-learn
- Matplotlib

## Prerequisites
- Python 3.x
- Pandas
- NumPy
- Scikit-learn
- Matplotlib

## Dataset
The dataset used for this project is `loan_data.csv`, which includes the following columns:
- `income`: Applicant's income.
- `credit_score`: Applicant's credit score.
- `loan_amount`: Amount of the loan requested.
- `loan_term`: Term of the loan in months.
- `employment_status`: Applicant's employment status (e.g., employed, unemployed).
- `loan_approved`: Target variable indicating if the loan was approved (1) or not (0).

## Getting Started

### Step 1: Clone the Repository
```bash
git clone https://github.com/MD-Shibli-Mollah/SH-Python-2024.git
```

Navigate to the project directory
```bash
cd SH-Python-2024-main/Coding_Task-for-Validata_Devs-(Python-ML)-Shibli/Part_2-Loan_Approval_Prediction_with_ML-Shibli
```

### Step 2: Installation
To run this project, ensure you have Python installed on your machine along with the necessary packages. You can install the required packages using pip:

```bash
pip install pandas numpy scikit-learn matplotlib
```

## Usage
### Run the script:
```bash
python loanApprvML.py
```
## Results
After running the models, the evaluation metrics and feature importances are saved in an output text file (`output.txt`). A bar plot of feature importances is also saved as an image (`feature_importances.png`).

## Features
- Data preprocessing including label encoding and scaling.
- Implementation of KNN and Decision Tree classifiers for loan approval prediction.
- Evaluation of models using accuracy, precision, recall, F1 score, and confusion matrix.
- Visualization of feature importances from the Decision Tree model.

## Evaluation Metrics
The following metrics are used to evaluate the models:

- Accuracy: The ratio of correctly predicted instances to the total instances.
- Precision: The ratio of true positive predictions to the total positive predictions.
- Recall: The ratio of true positive predictions to the total actual positives.
- F1 Score: The harmonic mean of precision and recall.
- Confusion Matrix: A matrix showing the true positives, false positives, true negatives, and false negatives.