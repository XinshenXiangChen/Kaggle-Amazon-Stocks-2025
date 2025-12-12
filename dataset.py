import kagglehub
import pandas as pd
import os
import matplotlib.pyplot as plt

# Download latest version
path = kagglehub.dataset_download("meharshanali/amazon-stocks-2025")

print("Path to dataset files:", path)
csv_path = os.path.join(path, "AMZN_stock_data.csv")


dataset = pd.read_csv(csv_path)

if __name__ == "__main__":
    print(dataset["Close"])
    close = dataset["Close"]
    high = dataset["High"]

    fig, axs = plt.subplots(2, 2, figsize=(10,8))  # 2x2 grid
    axs[0, 0].plot(close)
    axs[0, 0].set_title('Close')
    axs[0, 1].scatter(close, close - high, color='red')
    axs[0, 1].set_title('Close - High')

    plt.show()


    print(dataset.index)
    print(dataset.columns)
    print(dataset.loc[0])



