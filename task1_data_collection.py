# TrendPulse Task 1
# Fixed version (handles API errors + avoids blocking)

import requests
import json
import os
import time
from datetime import datetime

TOP_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/{}.json"

HEADERS = {"User-Agent": "TrendPulse/1.0"}

# slightly increased for better coverage
TOTAL_IDS = 800
MAX_PER_CATEGORY = 25

CATEGORIES = {
    "technology": ["ai","software","tech","code","computer","data","cloud","api","gpu","llm","startup","app","programming"],
    "worldnews": ["war","government","country","president","election","climate","attack","global","india","china","usa","policy","news"],
    "sports": ["nfl","nba","fifa","sport","game","team","player","league","championship","match","cricket","football","tournament"],
    "science": ["research","study","space","physics","biology","discovery","nasa","genome","experiment","scientists","earth","medicine"],
    "entertainment": ["movie","film","music","netflix","game","book","show","award","streaming","series","tv","celebrity"]
}

# fetch top IDs
def get_top_ids():
    try:
        res = requests.get(TOP_URL, headers=HEADERS, timeout=5)
        return res.json()[:TOTAL_IDS]
    except:
        print("Error fetching top stories")
        return []

# fetch single story with timeout + safe handling
def get_story(story_id):
    try:
        res = requests.get(ITEM_URL.format(story_id), headers=HEADERS, timeout=5)

        if res.status_code != 200:
            return None

        return res.json()
    except:
        # small delay to avoid rapid failures
        time.sleep(0.3)
        return None

# check keyword match
def matches_category(title, keywords):
    if not title:
        return False

    title = title.lower()

    for word in keywords:
        if word in title:
            return True

    return False


def main():
    story_ids = get_top_ids()
    collected_data = []

    for category, keywords in CATEGORIES.items():
        count = 0
        print(f"\nCollecting {category} stories...")

        for sid in story_ids:

            if count >= MAX_PER_CATEGORY:
                break

            story = get_story(sid)

            # IMPORTANT: slow down requests
            time.sleep(0.1)

            if not story or "title" not in story:
                continue

            if not matches_category(story["title"], keywords):
                continue

            item = {
                "post_id": story.get("id"),
                "title": story.get("title"),
                "category": category,
                "score": story.get("score", 0),
                "num_comments": story.get("descendants", 0),
                "author": story.get("by", "unknown"),
                "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }

            collected_data.append(item)
            count += 1

        print(f"{category}: {count} stories collected")

        # required sleep after each category
        time.sleep(2)

    # create data folder
    if not os.path.exists("data"):
        os.makedirs("data")

    filename = "data/trends_" + datetime.now().strftime("%Y%m%d") + ".json"

    with open(filename, "w") as f:
        json.dump(collected_data, f, indent=4)

    print(f"\nCollected {len(collected_data)} stories. Saved to {filename}")


if __name__ == "__main__":
    main()

