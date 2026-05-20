# Customer Churn Prediction System

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![ML](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange)
![Status](https://img.shields.io/badge/Status-Production--Ready-brightgreen)
![UI](https://img.shields.io/badge/UI-Streamlit-red)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## Overview

An end-to-end machine learning pipeline that predicts customer churn in telecom systems — from raw data to an interactive prediction interface.

**Goal:** Identify customers likely to churn and enable proactive retention strategies.

---

## Why This Project Stands Out

- End-to-end ML pipeline: data → model → deployment
- Business-critical metric focus: **Recall**
- Proper feature scaling and preprocessing
- Model + scaler + column persistence via Pickle
- Interactive UI built with Streamlit
- Clean evaluation using Confusion Matrix and F1-score

---

## System Architecture

```
User Input → Data Preprocessing → Feature Scaling → ML Model → Prediction → UI Output
```

---

## Tech Stack

| Category         | Tools           |
|------------------|-----------------|
| Language         | Python 3.10     |
| Data Handling    | Pandas, NumPy   |
| Machine Learning | Scikit-learn    |
| Deployment UI    | Streamlit       |
| Serialization    | Pickle          |

---

## Project Structure

```
customer-churn-prediction/
│
├── app.py
├── main.py
├── churn.csv
├── model.pkl
├── scaler.pkl
├── columns.pkl
├── screenshots/
│   ├── churn-dashboard.png
│   └── churn-prediction-result.png
├── requirements.txt
└── README.md
```

---

## Setup & Installation

**1. Clone the repository**

```bash
git clone https://github.com/charlie00769/customer-churn-prediction
cd customer-churn-prediction
```

**2. Create a virtual environment**

```bash
python -m venv venv
venv\Scripts\activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Train the model** *(optional — pre-trained model included)*

```bash
python main.py
```

**5. Run the app**

```bash
streamlit run app.py
```

---

## Model Details

| Property    | Value               |
|-------------|---------------------|
| Algorithm   | Logistic Regression |
| Scaling     | StandardScaler      |
| Key Metric  | Recall              |

---

## Application Preview

**Dashboard Input**

<img width="1918" height="994" alt="churn-prediction-ui" src="https://github.com/user-attachments/assets/1f1b6622-d0a8-4d55-b384-0cff3f1139c2" />

**Prediction Output**

<img width="370" height="796" alt="churn-prediction-result" src="https://github.com/user-attachments/assets/60bc01e9-751d-4907-afde-18401dc057d2" />

---

## Sample Prediction

| Feature                | Value |
|------------------------|-------|
| Day Minutes            | 200   |
| Customer Service Calls | 2     |
| International Plan     | No    |
| Voice Mail Plan        | Yes   |

**Output:** No Churn — Probability: `0.23`

---

## Future Enhancements

- Data visualization dashboard
- Bulk predictions via CSV upload
- Cloud deployment (Streamlit Cloud / AWS)
- Advanced models: XGBoost, Random Forest

---

## Real-World Applications

- Telecom churn prediction
- SaaS customer retention
- Subscription analytics

---

## Author

**Kaustubh Valanjuwani**

---

## Support

If this project was useful, give it a ⭐ on GitHub and share it with others.
