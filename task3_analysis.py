# TrendPulse Task 3
# Data Analysis using Pandas and NumPy

import pandas as pd
import numpy as np
import os

def main():

    # -------- Step 1: Load CSV --------
    file_path = "data/trends_cleaned.csv"

    if not os.path.exists(file_path):
        print("CSV file not found. Run Task 2 first.")
        return

    df = pd.read_csv(file_path)

    print("Data loaded:", len(df))

    # -------- Step 2: Basic Info --------
    print("\nData Info:")
    print(df.info())

    print("\nFirst 5 rows:")
    print(df.head())

    # -------- Step 3: Average Score --------
    avg_score = np.mean(df["score"])
    print("\nAverage Score:", avg_score)

    # -------- Step 4: Top Category --------
    top_category = df["category"].value_counts().idxmax()
    print("Top Category:", top_category)

    # -------- Step 5: Posts per Category --------
    category_counts = df["category"].value_counts()
    print("\nPosts per category:")
    print(category_counts)

    # -------- Step 6: Top 5 Highest Scored Posts --------
    top_posts = df.sort_values(by="score", ascending=False).head(5)

    print("\nTop 5 posts:")
    print(top_posts[["title", "score", "category"]])

    # -------- Step 7: Average Comments per Category --------
    avg_comments = df.groupby("category")["num_comments"].mean()

    print("\nAverage comments per category:")
    print(avg_comments)

    # -------- Step 8: Summary Statistics --------
    print("\nSummary statistics:")
    print(df.describe())

    # -------- Step 9: Save Top Posts --------
    output_file = "data/top_posts.csv"
    top_posts.to_csv(output_file, index=False)

    print("\nTop posts saved to:", output_file)


# run program
if __name__ == "__main__":
    main()