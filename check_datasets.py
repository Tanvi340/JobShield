import pandas as pd

# Kaggle dataset
kaggle = pd.read_csv("data/fake_job_postings.csv")

print("===== KAGGLE DATASET =====")
print("Rows:", len(kaggle))
print("Columns:")
print(kaggle.columns.tolist())
print("\nFraudulent labels:")
print(kaggle["fraudulent"].value_counts())


# Hugging Face dataset
hf = pd.read_parquet("data/train-00000-of-00001.parquet")

print("\n===== HUGGING FACE DATASET =====")
print("Rows:", len(hf))
print("Columns:")
print(hf.columns.tolist())

print("\nFirst 5 rows:")
print(hf.head())