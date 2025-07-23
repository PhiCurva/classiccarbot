import os
import requests
import tweepy
import random

# API anahtarlarını ortam değişkenlerinden al
TW_API_KEY = os.environ["TW_API_KEY"]
TW_API_SECRET = os.environ["TW_API_SECRET"]
TW_ACCESS_TOKEN = os.environ["TW_ACCESS_TOKEN"]
TW_ACCESS_SECRET = os.environ["TW_ACCESS_SECRET"]
UNSPLASH_ACCESS_KEY = os.environ["UNSPLASH_ACCESS_KEY"]

# Twitter'a bağlan
auth = tweepy.OAuth1UserHandler(TW_API_KEY, TW_API_SECRET, TW_ACCESS_TOKEN, TW_ACCESS_SECRET)
api = tweepy.API(auth)

def get_unsplash_photo(query):
    url = f"https://api.unsplash.com/search/photos?query={query}&client_id={UNSPLASH_ACCESS_KEY}&per_page=30"
    response = requests.get(url)
    data = response.json()
    results = data.get("results", [])
    if not results:
        return None, None
    photo = random.choice(results)
    photo_url = photo["urls"]["regular"]
    photo_author = photo["user"]["name"]
    photo_link = photo["links"]["html"]
    return photo_url, f"Photo by {photo_author} on Unsplash {photo_link}"

def download_photo(url, filename="temp.jpg"):
    response = requests.get(url)
    with open(filename, "wb") as f:
        f.write(response.content)

def tweet_photo(filename, status):
    api.update_status_with_media(status=status, filename=filename)

def main():
    queries = ["classic car", "landscape"]
    query = random.choice(queries)
    photo_url, caption = get_unsplash_photo(query)
    if not photo_url:
        print("No photo found.")
        return
    download_photo(photo_url)
    tweet_photo("temp.jpg", caption)
    os.remove("temp.jpg")
    print("Tweet sent successfully.")

if __name__ == "__main__":
    main()
