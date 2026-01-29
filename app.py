from flask import Flask, render_template
import feedparser
import datetime
app = Flask(__name__)



rss_feed = [
        "https://bleepingcomputer.com/feed",
        "https://www.ncsc.gov.uk/api/1/services/v1/all-rss-feed.xml",
        "https://feeds.feedburner.com/TheHackersNews?format=xml"
        ]

import datetime

def retrieve_news():
    articles = []

    for url in rss_feed:
        feed = feedparser.parse(url)

        for entry in feed.entries[:10]:
            published_parsed = entry.get("published_parsed")

            if published_parsed:
                published_dt = datetime.datetime(*published_parsed[:6])
            else:
                published_dt = datetime.datetime.min  # fallback for missing dates

            articles.append({
                "title": entry.title,
                "link": entry.link,
                "date_published": entry.get("published", "No date"),
                "published_dt": published_dt,
                "source": feed.feed.get("title", "unknown")
            })

    articles.sort(key=lambda x: x["published_dt"], reverse=True)

    return articles


@app.route('/')
def index():
    news = retrieve_news()
    return render_template('index.html', news=news)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
