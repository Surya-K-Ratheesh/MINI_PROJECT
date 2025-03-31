import pandas as pd
import joblib
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

# Load dataset
df = pd.read_csv("career_guidance_pathways.csv")

# Encode categorical columns
le_career = LabelEncoder()
df["Career_Label"] = le_career.fit_transform(df["Career"])

# Selecting features and labels
X = df[["Min_10th_Marks", "Min_12th_Marks"]]
y = df["Career_Label"]

# Train the model
model = DecisionTreeClassifier()
model.fit(X, y)

# Save the model
joblib.dump(model, "career_recommendation_model.pkl")
joblib.dump(le_career, "label_encoder.pkl")
