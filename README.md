# LOAN-STATUS-PREDICTOR
A smart machine learning solution that predicts whether a loan application will be approved or rejected based on applicant details. This project can help financial institutions automate risk assessment, reduce human error, and make informed decisions.
## PROJECT OBJECTIVE
The goal is to develop a predictive model that classifies loan applications into Approved or Rejected, using historical loan data. A user-friendly Flask-based web interface is also provided to make predictions in real-time.
## FEATURES
Predicts loan approval status based on customer details.
Trained on a publicly available loan dataset.
Handles data preprocessing: missing values, categorical encoding, feature scaling.
Built using machine learning models such as:
### Logistic Regression
Logistic Regression is a supervised learning algorithm used for binary classification problems. In this project, it is used to classify whether a news article is real or fake based on the text content provided.
Despite its name, Logistic Regression is a classification algorithm (not regression). It predicts the probability that an input sample belongs to a certain class. It is best suited for problems where the output is binary (e.g., real vs. fake, yes vs. no, etc.).
#### Why Use Logistic Regression?
✅ Simple and easy to implement

✅ Works well with high-dimensional text data (like TF-IDF)

✅ Interpretable and efficient

✅ Suitable for binary classification tasks
### Random Forest
**Random Forest** is an **ensemble learning** method that builds multiple decision trees and combines their predictions to improve accuracy and control overfitting. In this loan status prediction project, Random Forest is used to classify whether a loan application will be **Approved** or **Rejected** based on applicant features.
#### 🧠 How It Works

1. **Bootstrap Sampling:**  
   Create _N_ subsets of the training data by sampling with replacement.

2. **Tree Building:**  
   For each subset, grow a decision tree:
   - At each node, randomly select _m_ features.
   - Choose the best split among those _m_ features.
   - Grow the tree until a stopping criterion (max depth or minimum samples per leaf).

3. **Aggregation:**  
   To predict, each tree votes on the class label. The class with the most votes is the forest’s prediction.
### Decision Tree
A **Decision Tree** is a powerful and easy-to-understand supervised learning algorithm used for both classification and regression tasks. In this project, the Decision Tree model is used to classify whether a **loan application** will be **Approved** or **Rejected** based on multiple applicant features.
Model evaluation with accuracy, confusion matrix, and classification report.
Integrated with a simple Flask web app for user input and prediction.
A Decision Tree is a **tree-like structure** where:

- Each **internal node** represents a decision based on a feature (e.g., income, credit history)
- Each **leaf node** represents the final prediction (Approved or Rejected)
- Each **branch** represents the outcome of a decision

It splits the data into subsets based on feature values to create the most **informative splits**, usually using **Gini Impurity** or **Entropy (Information Gain)** as the splitting criterion.

---
#### 🧠 How It Works

1. Start with the full dataset at the root.
2. At each node:
   - Choose the best feature to split the data using a metric like **Gini** or **Entropy**.
   - Split into child nodes based on feature values.
3. Recursively repeat until a stopping condition is met (max depth, pure class, or min samples).
4. Final prediction is made based on the **majority class** in the leaf node.

## Machine Learning Workflow 
Data Cleaning: Handle missing values, fix data types
Feature Engineering: Encode categorical variables, scale features
Model Training: Logistic Regression, Random Forest, Decision Tree, etc.
Evaluation Metrics: Accuracy, precision, recall, F1-score
Model Serialization: Exported using joblib or pickle

