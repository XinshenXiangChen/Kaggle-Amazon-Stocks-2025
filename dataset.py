import kagglehub
import pandas as pd
import os

# Download latest version
path = kagglehub.dataset_download("meharshanali/amazon-stocks-2025")

print("Path to dataset files:", path)
csv_path = os.path.join(path, "AMZN_stock_data.csv")


dataset = pd.read_csv(csv_path)
