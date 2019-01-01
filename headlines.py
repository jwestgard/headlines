#!/usr/bin/env python3

from flask import Flask, render_template
import feedparser

RSS_FEEDS = {
    'bbc':  "http://feeds.bbci.co.uk/news/rss.xml",
    'at':   "http://feeds.arstechnica.com/arstechnica/index",
    'mit':  "https://www.technologyreview.com/topnews.rss",
    'wapo': "http://feeds.washingtonpost.com/rss/politics"
    }

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/headlines')
@app.route('/headlines/<source>')
def get_news(source='at'):
    feed = feedparser.parse(RSS_FEEDS[source])
    article = feed['entries'][0]
    return   render_template('headlines.html', 
                             articles=feed['entries'],
                             source=source.upper()
                             )

if __name__ == "__main__":
    app.run(port=5000, debug=True)
