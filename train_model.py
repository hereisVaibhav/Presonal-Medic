import pandas as pd
import joblib
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.neighbors import KNeighborsClassifier

# Load Dataset
df = pd.read_csv("Brain/disease_symptom.csv")

# Convert symptom strings into lists
df["Symptom(s)"] = df["Symptom(s)"].apply(lambda x: x.split(", "))

# Use MultiLabelBinarizer to convert symptoms into binary matrix
mlb = MultiLabelBinarizer()
X = mlb.fit_transform(df["Symptom(s)"])
y = df["Possible Disease"]

# Train KNN model (K=1 because we only have 3 diseases)
model = KNeighborsClassifier(n_neighbors=1)
model.fit(X, y)

# Save Model & MultiLabelBinarizer
joblib.dump(model, "Brain/disease_model.pkl")
joblib.dump(mlb, "Brain/mlb.pkl")

print("✅ KNN Model Training Completed & Saved!")
