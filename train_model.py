import pandas as pd

# Load dataset
df = pd.read_csv("data/fake_job_postings.csv")

# Combine important job text fields
df["text"] = (
    df["title"].fillna("") + " " +
    df["company_profile"].fillna("") + " " +
    df["description"].fillna("") + " " +
    df["requirements"].fillna("") + " " +
    df["benefits"].fillna("") + " " +
    df["location"].fillna("") + " " +
    df["employment_type"].fillna("") + " " +
    df["required_experience"].fillna("") + " " +
    df["required_education"].fillna("") + " " +
    df["industry"].fillna("") + " " +
    df["function"].fillna("")
)

# Input and output
X = df["text"]
y = df["fraudulent"]

print("Dataset loaded successfully!")
print("Total jobs:", len(df))
print("Real jobs:", (y == 0).sum())
print("Fake jobs:", (y == 1).sum())

from sklearn.model_selection import train_test_split

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\nData split completed!")
print("Training jobs:", len(X_train))
print("Testing jobs:", len(X_test))

from sklearn.feature_extraction.text import TfidfVectorizer

# Convert job text into numerical features
vectorizer = TfidfVectorizer(
    max_features=10000,
    stop_words="english",
    ngram_range=(1, 2)
)


X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

print("\nTF-IDF conversion completed!")
print("Training data shape:", X_train_tfidf.shape)
print("Testing data shape:", X_test_tfidf.shape)

from sklearn.svm import LinearSVC

# Create the ML model
model = LinearSVC(
    class_weight="balanced"
)

# Train the model
model.fit(X_train_tfidf, y_train)

print("\nModel training completed!")

from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Predict on test data
y_pred = model.predict(X_test_tfidf)

# Check accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:", accuracy)

# Detailed performance
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:")
print(cm)

import joblib

joblib.dump(model, "model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("\nModel and vectorizer saved successfully!")