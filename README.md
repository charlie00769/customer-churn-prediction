# 🚀 📊 Customer Churn Prediction System

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![ML](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange)
![Status](https://img.shields.io/badge/Status-Production--Ready-brightgreen)
![UI](https://img.shields.io/badge/UI-Streamlit-red)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## 💡 Project Overview

This project presents a **production-grade machine learning pipeline** designed to predict customer churn in telecom systems.

Built with a focus on **real-world deployment**, the system integrates data preprocessing, feature engineering, model training, and an interactive prediction interface.

> 🎯 **Goal:** Identify customers likely to churn and enable proactive retention strategies.

---

## 🔥 Why This Project Stands Out

* 🚀 End-to-end ML pipeline (data → model → deployment)
* 📊 Focus on **business-critical metric: Recall**
* ⚙️ Proper feature scaling & preprocessing
* 💾 Model + scaler + column persistence
* 🌐 Interactive UI (Streamlit)
* 🧪 Clean evaluation (Confusion Matrix + F1-score)

---

## 🧠 System Architecture

```id="hy3oq9"
User Input → Data Preprocessing → Feature Scaling → ML Model → Prediction → UI Output
```

---

## 🛠️ Tech Stack

| Category         | Tools Used    |
| ---------------- | ------------- |
| Language         | Python        |
| Data Handling    | Pandas, NumPy |
| Machine Learning | Scikit-learn  |
| Deployment UI    | Streamlit     |
| Serialization    | Pickle        |

---

## 📂 Project Structure

```id="c7s84o"
customer-churn-prediction/
│
├── app.py              # Streamlit UI
├── main.py             # Training pipeline
├── churn.csv           # Dataset
├── model.pkl           # Trained model
├── scaler.pkl          # StandardScaler
├── columns.pkl         # Feature order
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup & Installation

### 1️⃣ Clone Repository

```bash id="z55dn6"
git clone https://github.com/charlie00769/customer-churn-prediction
cd customer-churn-prediction
```

---

### 2️⃣ Create Virtual Environment

```bash id="j1rfca"
python -m venv venv
venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```bash id="7ydpnq"
pip install -r requirements.txt
```

---

### 4️⃣ Train Model (Optional)

```bash id="0xv2nt"
python main.py
```

---

### 5️⃣ Run App

```bash id="j64dwb"
streamlit run app.py
```

---

## 📊 Model Insights

* **Algorithm:** Logistic Regression
* **Scaling:** StandardScaler
* **Key Metric:** Recall (to detect churn customers)
* **Evaluation:**

  * Accuracy
  * Precision
  * Recall
  * F1-score

---

## 📸 Application Preview

> 📌 Add screenshots to make your project visually impressive

```id="b2i5e1"
screenshots/
   ├── <img width="1918" height="994" alt="churn-prediction-ui" src="https://github.com/user-attachments/assets/49528c38-eb97-49fe-9603-d85ae9a47288" />

   ├── <img width="370" height="796" alt="churn-prediction-result" src="https://github.com/user-attachments/assets/60249831-2f82-4b7b-a876-6f263bffbf4b" />

```

```id="o5sf6o"
![App UI](screenshots/app-ui.png)
![Prediction Result](screenshots/prediction.png)
```

---

## 🎯 Sample Prediction

| Feature                | Value |
| ---------------------- | ----- |
| Day Minutes            | 200   |
| Customer Service Calls | 2     |
| Intl Plan              | No    |
| Voice Mail Plan        | Yes   |

➡️ Output:

* ✅ No Churn
* 📊 Probability: 0.23

---

## 🔮 Future Enhancements

* 📊 Data visualization dashboard
* 📁 Bulk predictions via CSV
* ☁️ Cloud deployment (Streamlit Cloud / AWS)
* 🤖 Advanced ML models (XGBoost, Random Forest)

---

## 📌 Real-World Applications

* Telecom churn prediction
* SaaS customer retention
* Subscription analytics

---

## 👨‍💻 Author

**Kaustubh Valanjuwani**

---

## ⭐ Support

If you found this project useful:

👉 Give it a ⭐ on GitHub
👉 Share it with others




