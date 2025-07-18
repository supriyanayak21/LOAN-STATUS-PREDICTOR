from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load model
model = joblib.load('loan_status_predict')
@app.route('/about')
def about():
    return render_template("about.html")
@app.route('/')
def index():
    return render_template("home.html")
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            p1 = float(request.form['Gender'])
            p2 = float(request.form['Married'])
            p3 = float(request.form['Dependents'])
            p4 = float(request.form['Education'])
            p5 = float(request.form['Self_Employed'])
            p6 = float(request.form['ApplicantIncome'])
            p7 = float(request.form['CoapplicantIncome'])
            p8 = float(request.form['LoanAmount'])
            p9 = float(request.form['Loan_Amount_Term'])
            p10 = float(request.form['Credit_History'])
            p11 = float(request.form['Property_Area'])

            df = pd.DataFrame({
                'Gender': [p1],
                'Married': [p2],
                'Dependents': [p3],
                'Education': [p4],
                'Self_Employed': [p5],
                'ApplicantIncome': [p6],
                'CoapplicantIncome': [p7],
                'LoanAmount': [p8],
                'Loan_Amount_Term': [p9],
                'Credit_History': [p10],
                'Property_Area': [p11]
            })

            result = model.predict(df)

            if result[0] == 1:
                prediction = "Loan Approved"
            else:
                prediction = "Loan Not Approved"

            return render_template('index.html', prediction=prediction)
        except Exception as e:
            return render_template('index.html', prediction="Error: " + str(e))

    return render_template('index.html', prediction="")

if __name__ == '__main__':
    app.run(debug=True)
