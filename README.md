# 🚀 Reusable Machine Learning, Deep Learning & NLP Code Snippets

These reusable snippets are useful for:

* 📊 Data Analysis
* 🧹 Data Cleaning
* 🤖 Machine Learning
* 🧠 Deep Learning
* 💬 NLP
* 📈 Model Evaluation

You can directly add these sections into your `README.md`.

---

# 📦 Common Imports

```python id="r6qivm"
# Data Handling
import pandas as pd
import numpy as np

# Visualization
import matplotlib.pyplot as plt
import seaborn as sns

# Machine Learning
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    mean_squared_error,
    r2_score
)

# Deep Learning
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout

# NLP
import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
```

---

# 📊 Basic Dataset Overview

```python id="thvvjq"
# Dataset Shape
print("Shape:", df.shape)

# First 5 Rows
print(df.head())

# Dataset Info
print(df.info())

# Statistical Summary
print(df.describe())

# Missing Values
print(df.isnull().sum())
```

---

# 🧹 Missing Value Handling

## Fill Numerical Missing Values

```python id="2z7pq4"
num_cols = df.select_dtypes(include=["int64", "float64"]).columns

for col in num_cols:
    df[col].fillna(df[col].median(), inplace=True)
```

---

## Fill Categorical Missing Values

```python id="s4u0hx"
cat_cols = df.select_dtypes(include=["object"]).columns

for col in cat_cols:
    df[col].fillna(df[col].mode()[0], inplace=True)
```

---

# 🔥 Correlation Heatmap

```python id="7zb79e"
plt.figure(figsize=(12,8))

sns.heatmap(
    df.corr(numeric_only=True),
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")
plt.show()
```

---

# 🎯 Label Encoding

```python id="d1yx97"
encoder = LabelEncoder()

for col in df.select_dtypes(include=["object"]):
    df[col] = encoder.fit_transform(df[col])
```

---

# 📏 Feature Scaling

```python id="rz5prz"
scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)
```

---

# ✂️ Train Test Split

```python id="r2phz7"
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
```

---

# 🤖 Basic Machine Learning Model

## Logistic Regression

```python id="bj4nwc"
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
```

---

# 🌲 Random Forest Classifier

```python id="84rwq2"
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
```

---

# 📉 Confusion Matrix

```python id="gfqitn"
cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(6,5))

sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues"
)

plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")

plt.show()
```

---

# 📄 Classification Report

```python id="4r67gx"
print(classification_report(y_test, y_pred))
```

---

# 🧠 Basic Deep Learning Model

```python id="s7v85k"
model = Sequential([
    Dense(128, activation="relu", input_shape=(X_train.shape[1],)),
    Dropout(0.3),

    Dense(64, activation="relu"),
    Dropout(0.3),

    Dense(1, activation="sigmoid")
])

model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

history = model.fit(
    X_train,
    y_train,
    epochs=10,
    batch_size=32,
    validation_split=0.2
)
```

---

# 📈 Deep Learning Training Graph

```python id="jws3jg"
plt.figure(figsize=(12,5))

# Accuracy
plt.subplot(1,2,1)

plt.plot(history.history["accuracy"], label="Train Accuracy")
plt.plot(history.history["val_accuracy"], label="Validation Accuracy")

plt.title("Model Accuracy")
plt.legend()

# Loss
plt.subplot(1,2,2)

plt.plot(history.history["loss"], label="Train Loss")
plt.plot(history.history["val_loss"], label="Validation Loss")

plt.title("Model Loss")
plt.legend()

plt.show()
```

---

# 💬 NLP Text Cleaning

```python id="1x5m2q"
stop_words = set(stopwords.words("english"))

def clean_text(text):

    # Lowercase
    text = text.lower()

    # Remove Special Characters
    text = re.sub(r"[^a-zA-Z]", " ", text)

    # Tokenization
    words = word_tokenize(text)

    # Remove Stopwords
    words = [word for word in words if word not in stop_words]

    return " ".join(words)
```

---

# 📝 TF-IDF Vectorization

```python id="13qkgo"
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(max_features=5000)

X = vectorizer.fit_transform(df["text"])
```

---

# 🤖 NLP Classification Model

```python id="fryi4f"
from sklearn.naive_bayes import MultinomialNB

model = MultinomialNB()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
```

---

# 💾 Save Machine Learning Model

```python id="x6ik1p"
import joblib

joblib.dump(model, "model.pkl")
```

---

# 📂 Load Saved Model

```python id="qg2p49"
model = joblib.load("model.pkl")
```

---

# 🛠️ Useful Debugging Snippets

## Check Data Types

```python id="3gu4eg"
print(df.dtypes)
```

---

## Unique Values

```python id="v3f7s4"
for col in df.columns:
    print(col, df[col].nunique())
```

---

## Duplicate Rows

```python id="09ut56"
print("Duplicates:", df.duplicated().sum())
```

---

# 🎯 Recommended README Sections

You can organize your repo like this:

```md id="8fwg5s"
# Project Name

## Dataset
## Data Cleaning
## Exploratory Data Analysis
## Feature Engineering
## Model Building
## Model Evaluation
## Results
## Future Improvements
```

---

# 💡 Pro Tip

Create a folder structure like this for every ML project:

```bash id="18g0kp"
project/
│
├── data/
├── notebooks/
├── models/
├── src/
├── README.md
├── requirements.txt
└── app.py
```

This keeps projects clean and professional.
