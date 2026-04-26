## HEPro AI Business Analytics Fellowship (Jan 2026-June 2026)

###  Customer Churn Prediction & Optimization
**An End-to-End Machine Learning Solution: From Exploratory Data Analysis to Cloud Deployment Using Streamlit App**

---
### Project Overview
This project addresses a critical business challenge in the telecommunications sector: **Customer Attrition**. Leveraging the Telco Customer Churn dataset, I developed a predictive framework to identify high-risk customers. The solution integrates rigorous data preprocessing, behavioral analysis, and machine learning to provide actionable retention strategies for stakeholders.

### Key Insights & Observations
From the **Exploratory Data Analysis (EDA)** and **Feature Importance** analysis:
* **Contract Risk:** Customers on **Month-to-Month** contracts exhibit a significantly higher churn rate compared to those on one or two-year commitments.
* **The "Early Exit" Window:** Churn is most prevalent during the first **6-12 months** of tenure, highlighting a critical window for loyalty programs.
* **Service Stickiness:** Customers without **Tech Support** or **Online Security** services are twice as likely to churn, indicating that value-added services increase customer "stickiness."
* **Financial Friction:** Users paying via **Electronic Check** show higher attrition rates than those using automated payment methods.

---
### 🛠️ Technical Architecture
The project follows a standard production-grade directory structure:

```text
├── data/
│   ├── original/          # Raw dataset (source of truth)
│   └── cleaned/           # Preprocessed CSVs used for modeling
├── models/
│   ├── baseline_model.pkl # Trained Logistic Regression model
│   └── scaler.pkl         # Fitted StandardScaler object
├── notebooks/
│   └── Churn_Prediction.ipynb # Full EDA and experiment log
├── app.py                 # Streamlit application UI logic
├── requirements.txt       # Python dependencies for deployment
└── README.md              # Project documentation
```
---
### Model Development & Performance
- I evaluated multiple algorithms (Decision Trees, Random Forest, Gradient Boosting), ultimately deploying a Logistic Regression model optimized for interpretability and real-time inference.
Metric Focus: Given the class imbalance (26.5% churn), I prioritized AUC-ROC and F1-Score over simple accuracy to ensure high-risk customers are correctly identified.

- Preprocessing: Implemented StandardScaler for numerical normalization and manual encoding for categorical features to ensure deployment stability.

---

### 🌐 Live Deployment
The model is successfully deployed as a real-time web application via **Streamlit Cloud**. This interactive interface allows business users and stakeholders to input specific customer attributes—such as tenure, contract type, and monthly charges—to receive an instant churn risk assessment.

**👉 [Launch the Customer Churn Predictor](https://customer-churn-prediction-optimization-7rfajyvdswxzptc7zryhwr.streamlit.app/)**
