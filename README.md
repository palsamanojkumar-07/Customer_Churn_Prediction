# 📊 Customer Churn Prediction

## 📌 Project Overview

Customer Churn Prediction is a Machine Learning project that predicts whether a telecom customer is likely to churn based on customer demographics, account information, and subscribed services.

The objective of this project is to help telecom companies identify customers at risk of leaving and take proactive retention measures to reduce customer churn and improve business profitability.

---

## 🎯 Business Objective

- Predict whether a customer will churn.
- Identify the key factors influencing customer churn.
- Support customer retention strategies through data-driven insights.
- Deploy the model as a Streamlit web application for real-time predictions.

---

## 📂 Dataset

- **Dataset:** Telco Customer Churn Dataset
- **Target Variable:** Churn
- **Rows:** 7,043
- **Features:** Customer demographics, services, billing information, and account details.

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Streamlit

---

## 📊 Exploratory Data Analysis (EDA)

Performed comprehensive EDA to understand customer behavior.

- Missing Value Analysis
- Target Variable Distribution
- Gender Distribution
- Contract Type Analysis
- Internet Service Analysis
- Monthly Charges Distribution
- Tenure Distribution
- Correlation Heatmap
- Churn Analysis using various customer attributes

---

## ⚙️ Data Preprocessing

- Removed unnecessary columns
- Converted data types
- Handled missing values
- One-Hot Encoding
- Feature Scaling
- Train-Test Split

---

## 🤖 Machine Learning Models

- Logistic Regression
- Decision Tree
- Random Forest

Hyperparameter tuning was performed using **GridSearchCV**.

---

## 📈 Model Evaluation

Evaluation metrics used:

- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC Score
- Confusion Matrix
- ROC Curve

---

## 🏆 Best Model

**Logistic Regression (Hyperparameter Tuned)**

**Performance:**

- Accuracy: **80.41%**
- ROC-AUC Score: **0.8413**

---

## 📌 Feature Importance

The most important features influencing customer churn include:

- Contract Type
- Internet Service
- Online Security
- Tech Support
- Monthly Charges
- Tenure
- Payment Method

---

## 💻 Streamlit Application

The trained model was deployed using **Streamlit**, allowing users to enter customer details and predict churn in real time.

---

## 📁 Project Structure

```
Customer_Churn_Prediction/
│
├── app.py
├── churn_model.pkl
├── feature_columns.pkl
├── requirements.txt
├── README.md
├── Customer_Churn_Prediction.ipynb
├── WA_Fn-UseC_-Telco-Customer-Churn.csv
└── .gitignore
```

---

## 🚀 How to Run the Project

### Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Customer_Churn_Prediction.git
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the Streamlit application

```bash
streamlit run app.py
```

---

## 📊 Business Insights

- Customers with Month-to-Month contracts are more likely to churn.
- Long-term contracts significantly improve customer retention.
- Customers with higher monthly charges have a higher probability of churn.
- Online Security and Tech Support services reduce customer churn.
- Contract Type, Internet Service, and Tenure are key factors influencing customer churn.

---

## 🎯 Conclusion

Successfully developed a Machine Learning model to predict customer churn using telecom customer data.

The tuned Logistic Regression model achieved strong predictive performance with a **ROC-AUC Score of 0.8413**. The Streamlit application enables real-time churn prediction, helping telecom companies identify at-risk customers and improve customer retention through data-driven decision-making.

---

## 👨‍💻 Author

**Palsa Manoj Kumar**

- GitHub: https://github.com/palsamanojkumar-07
