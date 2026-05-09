# Exploratory Data Analysis (EDA) Visualization

This script automatically visualizes both **categorical** and **numerical** columns in a dataset using **Seaborn** and **Matplotlib**.

---

## 📌 Features

### Categorical Columns

* Count Plot
* Pie Chart (Percentage Distribution)

### Numerical Columns

* Histogram with KDE
* Boxplot for Outlier Detection

---

## 📦 Required Libraries

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```

---

# 📊 Categorical Data Visualization

```python
# Select categorical columns
catgorical_values = df.select_dtypes(include=["object"])

# Loop through categorical columns
for catgorical in catgorical_values:

    # Count values
    counts = df[catgorical].value_counts()

    # Create figure
    plt.figure(figsize=(12,5))

    # -------------------------
    # Count Plot
    # -------------------------
    plt.subplot(1,2,1)

    sns.countplot(
        data=df,
        x=catgorical,
        palette="Set2"
    )

    plt.title(f"Count of {catgorical} values")
    plt.xticks(rotation=90)
    plt.ylabel("Count")

    # -------------------------
    # Pie Chart
    # -------------------------
    plt.subplot(1,2,2)

    plt.pie(
        counts,
        labels=counts.index,
        autopct='%1.1f%%',
        startangle=90
    )

    plt.title(f"Percentage of {catgorical} values")

    # Make pie chart circular
    plt.axis('equal')

    # Adjust spacing
    plt.tight_layout()

    # Show plots
    plt.show()

    print("\n")
```

---

# 📈 Numerical Data Visualization

```python
# Select numerical columns
num_values = df.select_dtypes(include=["int64"])

# Loop through numerical columns
for num in num_values:

    # Create figure
    plt.figure(figsize=(12,5))

    # -------------------------
    # Histogram + KDE
    # -------------------------
    plt.subplot(1,2,1)

    sns.histplot(
        data=df,
        x=num,
        kde=True,
        bins=20
    )

    plt.title(f"Distribution of {num} values")
    plt.xlabel(num)
    plt.ylabel("Count")

    # -------------------------
    # Boxplot
    # -------------------------
    plt.subplot(1,2,2)

    sns.boxplot(
        data=df,
        x=num,
        palette="Set2"
    )

    plt.title(f"Boxplot of {num} values")
    plt.xlabel(num)

    # Adjust spacing
    plt.tight_layout()

    # Show plots
    plt.show()
```

---

# ✅ Output

## Categorical Columns

* Frequency distribution
* Percentage share of each category

## Numerical Columns

* Data distribution
* Outlier detection using boxplots

---

# 💡 Tip

To include float columns as well:

```python
num_values = df.select_dtypes(include=["int64", "float64"])
```

---

# 🚀 Example

```python
df = pd.read_csv("data.csv")
```

Run the visualization cells after loading your dataset.
