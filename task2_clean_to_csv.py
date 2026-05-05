# TrendPulse Task 2
# Convert JSON data into cleaned CSV

import pandas as pd
import json
import os

def main():

    # -------- Step 1: Load JSON --------
    file_path = "data/trends_20260505.json"   # change date if needed

    if not os.path.exists(file_path):
        print("JSON file not found. Run Task 1 first.")
        return

    with open(file_path, "r") as f:
        data = json.load(f)

    print("Loaded", len(data), "records")

    # -------- Step 2: Convert to DataFrame --------
    df = pd.DataFrame(data)

    # -------- Step 3: Cleaning --------

    # remove duplicate posts
    df = df.drop_duplicates(subset="post_id")

    # remove rows with missing title
    df = df[df["title"].notna()]

    # fill missing values
    df["score"] = df["score"].fillna(0)
    df["num_comments"] = df["num_comments"].fillna(0)
    df["author"] = df["author"].fillna("unknown")

    # convert data types
    df["score"] = df["score"].astype(int)
    df["num_comments"] = df["num_comments"].astype(int)

    # optional: remove very low quality posts
    df = df[df["score"] >= 0]

    # -------- Step 4: Sorting --------
    df = df.sort_values(by="score", ascending=False)

    # -------- Step 5: Save CSV --------
    if not os.path.exists("data"):
        os.makedirs("data")

    output_file = "data/trends_cleaned.csv"
    df.to_csv(output_file, index=False)

    # -------- Step 6: Print info --------
    print("\nCleaned data saved to:", output_file)
    print("Total records after cleaning:", len(df))

    print("\nTop 5 rows:")
    print(df.head())


# run program
if __name__ == "__main__":
    main()