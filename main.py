"""
Main code
"""


import pandas as pd
import matplotlib.pyplot as plt
import polars as pl


def summary(csv):
    """summary statistics in csv"""
    df = pl.read_csv(csv)
    return df.describe()


def histogram_blood_pressure(csv):
    """generate example visualization of the heart dataset"""
    pd.set_option("display.max_columns", None)
    polars_df = pl.read_csv(csv)
    plt.figure(figsize=(10, 6))
    plt.hist(polars_df["trtbps"], bins=20, edgecolor="black")
    plt.title("Resting Blood Pressure Distribution")
    plt.xlabel("Resting Blood Pressure")
    plt.ylabel("Frequency")
    plt.show()


# if __name__ == "__main__":
# summary("heart.csv")
# histogram_blood_pressure("heart.csv")
