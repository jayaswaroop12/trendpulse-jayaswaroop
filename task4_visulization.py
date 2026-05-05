# TrendPulse Task 4
# Data Visualization using matplotlib

import pandas as pd
import matplotlib.pyplot as plt
import os

def main():

    file_path = "data/trends_cleaned.csv"

    if not os.path.exists(file_path):
        print("CSV file not found. Run Task 2 first.")
        return

    df = pd.read_csv(file_path)

    # -------- Graph 1: Posts per Category --------
    category_counts = df["category"].value_counts()

    plt.figure()
    category_counts.plot(kind="bar")
    plt.title("Posts per Category")
    plt.xlabel("Category")
    plt.ylabel("Number of Posts")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("data/posts_per_category.png")
    plt.show()

    # -------- Graph 2: Score Distribution --------
    plt.figure()
    plt.hist(df["score"], bins=20)
    plt.title("Score Distribution")
    plt.xlabel("Score")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig("data/score_distribution.png")
    plt.show()

    # -------- Graph 3: Top 5 Posts --------
    top_posts = df.sort_values(by="score", ascending=False).head(5)

    plt.figure()
    plt.barh(top_posts["title"], top_posts["score"])
    plt.title("Top 5 Highest Scored Posts")
    plt.xlabel("Score")
    plt.ylabel("Title")
    plt.tight_layout()
    plt.savefig("data/top_posts.png")
    plt.show()

    print("Graphs saved in data/ folder")


if __name__ == "__main__":
    main()