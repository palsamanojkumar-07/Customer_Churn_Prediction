import streamlit as st
import pandas as pd
import joblib

# ==========================================================
# Page Configuration
# ==========================================================

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📞",
    layout="wide"
)

# ==========================================================
# Load Model
# ==========================================================

try:
    model = joblib.load("churn_model.pkl")
    feature_columns = joblib.load("feature_columns.pkl")
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

# ==========================================================
# Sidebar
# ==========================================================

st.sidebar.title("📞 Customer Churn Prediction")

st.sidebar.markdown("""
### 📌 About Project

This application predicts whether a telecom customer is likely to churn using Machine Learning.

### 🤖 Model

Logistic Regression

### 📊 Model Performance

- Accuracy : **80.41%**
- ROC-AUC : **72.49%**

### 👨‍💻 Developed By

**PALSA MANOJ KUMAR**
""")
st.sidebar.success("✅ Model Ready for Prediction")

# ==========================================================
# Title
# ==========================================================

st.title("📞 Customer Churn Prediction System")
st.markdown(
"""
Predict whether a telecom customer is likely to **Churn** or **Stay**
using Machine Learning.
"""
)

with st.expander("ℹ️ About Customer Churn Prediction"):

    st.write("""
This application predicts whether a telecom customer is likely to leave the company.

Businesses can use this prediction to identify at-risk customers and improve retention strategies.
""")
    
st.divider()

# ==========================================================
# User Inputs
# ==========================================================

col1, col2 = st.columns(2)

with col1:

    gender = st.selectbox("Gender", ["Male", "Female"])

    senior = st.selectbox("Senior Citizen", [0, 1])

    partner = st.selectbox("Partner", ["Yes", "No"])

    dependents = st.selectbox("Dependents", ["Yes", "No"])

    tenure = st.slider("Tenure (Months)", 0, 72, 12)

    phone_service = st.selectbox("Phone Service", ["Yes", "No"])

    multiple_lines = st.selectbox("Multiple Lines", ["Yes", "No", "No phone service"])

    internet_service = st.selectbox(
        "Internet Service",
        ["DSL", "Fiber optic", "No"]
    )

with col2:

    online_security = st.selectbox("Online Security", ["Yes", "No", "No internet service"])

    online_backup = st.selectbox("Online Backup", ["Yes", "No", "No internet service"])

    device_protection = st.selectbox("Device Protection", ["Yes", "No", "No internet service"])

    tech_support = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])

    streaming_tv = st.selectbox("Streaming TV", ["Yes", "No", "No internet service"])

    streaming_movies = st.selectbox("Streaming Movies", ["Yes", "No", "No internet service"])

contract = st.selectbox(
    "Contract",
    ["Month-to-month", "One year", "Two year"]
)

paperless = st.selectbox(
    "Paperless Billing",
    ["Yes", "No"]
)

payment = st.selectbox(
    "Payment Method",
    [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]
)

monthly = st.number_input(
    "Monthly Charges",
    min_value=0.0,
    max_value=200.0,
    value=70.0
)

total = st.number_input(
    "Total Charges",
    min_value=0.0,
    max_value=10000.0,
    value=1500.0
)

# ==========================================================
# Prediction
# ==========================================================

if st.button("🔍 Predict Churn", use_container_width=True):

    input_df = pd.DataFrame({

        "gender":[gender],
        "SeniorCitizen":[senior],
        "Partner":[partner],
        "Dependents":[dependents],
        "tenure":[tenure],
        "PhoneService":[phone_service],
        "MultipleLines":[multiple_lines],
        "InternetService":[internet_service],
        "OnlineSecurity":[online_security],
        "OnlineBackup":[online_backup],
        "DeviceProtection":[device_protection],
        "TechSupport":[tech_support],
        "StreamingTV":[streaming_tv],
        "StreamingMovies":[streaming_movies],
        "Contract":[contract],
        "PaperlessBilling":[paperless],
        "PaymentMethod":[payment],
        "MonthlyCharges":[monthly],
        "TotalCharges":[total]

    })
    # One-Hot Encoding
    input_df = pd.get_dummies(input_df)

    # Match Training Columns
    input_df = input_df.reindex(
        columns=feature_columns,
        fill_value=0
    )

    # Prediction
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0]

    st.divider()

    if prediction == 1:
        st.error("⚠️ Customer is likely to Churn")
    else:
        st.success("✅ Customer is likely to Stay")
    # ==========================================================
    # Prediction Probability
    # ==========================================================

    st.subheader("📊 Prediction Probability")

    st.progress(min(max(float(probability[1]), 0.0), 1.0))

    st.write(f"✅ Stay Probability : **{probability[0]*100:.2f}%**")
    st.write(f"⚠️ Churn Probability : **{probability[1]*100:.2f}%**")

    # ==========================================================
    # Customer Summary
    # ==========================================================

    st.subheader("📋 Customer Summary")

    summary = pd.DataFrame({
        "Feature": [
            "Gender",
            "Senior Citizen",
            "Partner",
            "Dependents",
            "Tenure",
            "Contract",
            "Monthly Charges",
            "Total Charges"
        ],
        "Value": [
            gender,
            senior,
            partner,
            dependents,
            tenure,
            contract,
            monthly,
            total
        ]
    })

    st.dataframe(summary, use_container_width=True)

    # ==========================================================
    # Business Insights
    # ==========================================================

    st.subheader("📊 Business Insights")

    st.info("""
    • Customers with Month-to-Month contracts have a higher churn risk.

    • Customers with shorter tenure are more likely to churn.

    • Higher Monthly Charges increase churn probability.

    • Long-term contracts improve customer retention.
    """)
# ==========================================================
# Footer
# ==========================================================

st.divider()

st.markdown("""
---
### 👨‍💻 Developed By

**PALSA MANOJ KUMAR**

📧 Email: palsamanojkumar@gmail.com

🔗 GitHub: https://github.com/palsamanojkumar-07
""")
