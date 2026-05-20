import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# =========================
# 1. Load Dataset
# =========================
df = pd.read_csv("churn.csv")

# =========================
# 2. Data Cleaning
# =========================
if "Phone" in df.columns:
    df.drop("Phone", axis=1, inplace=True)

df["Churn?"] = df["Churn?"].str.replace(".", "", regex=False)
df["Churn?"] = df["Churn?"].map({"True": 1, "False": 0})

df.dropna(inplace=True)

# =========================
# 3. Encoding
# =========================
df = pd.get_dummies(df, drop_first=True)

# =========================
# 4. Split Features & Target
# =========================
target_col = "Churn?"
y = df[target_col]
X = df.drop(target_col, axis=1)

# ✅ 👉 ADD HERE (IMPORTANT)
print("\n✅ Sample Input Row (Use this in your app):\n")
print(X.iloc[0])

print("\n✅ Column Order (VERY IMPORTANT):\n")
print(X.columns.tolist())

# ✅ SAVE COLUMN ORDER
pickle.dump(X.columns.tolist(), open("columns.pkl", "wb"))

# =========================
# 5. Scaling
# =========================
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# =========================
# 6. Train-Test Split
# =========================
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

# =========================
# 7. Model Training
# =========================
model = LogisticRegression(max_iter=2000)
model.fit(X_train, y_train)

# =========================
# 8. Prediction
# =========================
y_pred = model.predict(X_test)

# =========================
# 9. Evaluation
# =========================
print("\nAccuracy:", accuracy_score(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# =========================
# 10. Save Model & Scaler
# =========================
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(scaler, open("scaler.pkl", "wb"))

print("\n✅ Model, Scaler, and Columns saved successfully")