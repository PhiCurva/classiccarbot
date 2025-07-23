import os
import tweepy
import random

# Ortam değişkenlerinden API anahtarlarını al
TW_API_KEY = os.environ["TW_API_KEY"]
TW_API_SECRET = os.environ["TW_API_SECRET"]
TW_ACCESS_TOKEN = os.environ["TW_ACCESS_TOKEN"]
TW_ACCESS_SECRET = os.environ["TW_ACCESS_SECRET"]

# Twitter'a bağlan
auth = tweepy.OAuth1UserHandler(TW_API_KEY, TW_API_SECRET, TW_ACCESS_TOKEN, TW_ACCESS_SECRET)
api = tweepy.API(auth)

def main():
    tweets = [
        "Klasik arabaların büyüsü... #classiccar",
        "Doğanın sakinliği ve güzelliği... #landscape",
        "Bir zamanlar yolları süsleyen klasik arabalar.",
        "Manzara ve huzur bir arada.",
        "Klasik araba tutkusu hiç bitmez.",
        "Yeni gün, yeni manzaralar.",
    ]

    tweet = random.choice(tweets)
    try:
        api.update_status(tweet)
        print("Tweet başarıyla gönderildi:", tweet)
    except Exception as e:
        print("Tweet gönderilirken hata oluştu:", e)

if __name__ == "__main__":
    main()

