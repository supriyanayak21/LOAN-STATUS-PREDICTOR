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
Random Forest
Decision Tree
Model evaluation with accuracy, confusion matrix, and classification report.
Integrated with a simple Flask web app for user input and prediction.
## Machine Learning Workflow 
Data Cleaning: Handle missing values, fix data types
Feature Engineering: Encode categorical variables, scale features
Model Training: Logistic Regression, Random Forest, Decision Tree, etc.
Evaluation Metrics: Accuracy, precision, recall, F1-score
Model Serialization: Exported using joblib or pickle

