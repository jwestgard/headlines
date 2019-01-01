#!/usr/bin/env python3

from flask import Flask
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
    return   '''<html>
                    <body>
                        <h1>Hello World</h1>
                        <p>This is my project homepage.</p>
                        <h2>Links</h2>
                        <ul>
                            <li><a href="headlines">
                                Headlines project for learning Flask</a>
                                </li>
                            <li><a href="http://terpconnect.umd.edu/~westgard">
                                Personal homepage</a>
                                </li>
                            <li><a href="http://www.github.com/jwestgard">
                                Coding projects on Github</a>
                                </li>
                        </ul>
                      </body>
                </html>'''


@app.route('/headlines')
@app.route('/headlines/<source>')
def get_news(source='at'):
    feed = feedparser.parse(RSS_FEEDS[source])
    article = feed['entries'][0]
    return   """<html>
                    <body>
                        <h1>{0} Headlines</h1>
                        <b>{1}</b> <br />
                        <i>{2}</i> <br />
                        <p>{3}</p> <br />
                    </body>
                </html>""".format(source.upper(),
                                  article.get("title"),
                                  article.get("published"),
                                  article.get("summary")
                                  )


if __name__ == "__main__":
    app.run(port=5000, debug=True)
