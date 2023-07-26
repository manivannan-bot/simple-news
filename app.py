from flask import Flask, redirect, render_template, send_from_directory, request
import os
from combined import *
from tamil_test import * 
from tm_live_updates import * 
from tm_bbc_science import *
from datetime import datetime, timedelta
from urllib.parse import urlparse

app = Flask(__name__,  static_folder='static')
app.config["UPLOAD_FOLDER"] = "static"
app.use_static_route = True


#home
@app.route('/')
def home():
    # List of RSS feed URLs
    rss_urls = [
        'https://rss.app/feeds/_PnvpPtgIZfkdSUX6.xml'
        ]
    combined_feed = combine_feeds(rss_urls, num_posts=25)
    return render_template('index.html', data=combined_feed)
    
@app.route('/home')
def home_x():
    # List of RSS feed URLs
    rss_urls = [
        'https://rss.app/feeds/_PnvpPtgIZfkdSUX6.xml'
        ]
    combined_feed = combine_feeds(rss_urls, num_posts=25)
    return render_template('index.html', data=combined_feed)

#english
@app.route('/en')
def en():
    # List of RSS feed URLs
    rss_urls = [
        'https://www.news18.com/rss/latest.xml',
        'https://timesofindia.indiatimes.com/rssfeedstopstories.cms',
        ]
    combined_feed = combine_feeds(rss_urls, num_posts=15)
    return render_template('en.html', data=combined_feed)


#english/top
@app.route('/en/top')
def top():
    # List of RSS feed URLs
    rss_urls = [
        'https://www.news18.com/rss/latest.xml',
        'https://timesofindia.indiatimes.com/rssfeedstopstories.cms',
        ]
    combined_feed = combine_feeds(rss_urls, num_posts=15)
    return render_template('en-top.html', data=combined_feed)

#english/tech
@app.route('/en/tech')
def tech():
    rss_urls = [
        'https://rss.app/feeds/_BMWwRH1esZXYf1Bx.xml',
        'https://www.news18.com/rss/tech.xml',
        'https://timesofindia.indiatimes.com/rssfeeds/-2128672765.cms'
    ]
    combined_feed = combine_feeds(rss_urls, num_posts=10)
    return render_template('en-tech.html', data=combined_feed)

#english/entertainment
@app.route('/en/entertainment')
def en_entertain():
    rss_urls = [
        'https://rss.app/feeds/_yf28u8j80cd600FE.xml',
        'https://www.news18.com/rss/entertainment.xml',
        'http://timesofindia.indiatimes.com/rssfeeds/1081479906.cms'
    ]
    combined_feed = combine_feeds(rss_urls, num_posts=10)
    return render_template('en-entertainment.html', data=combined_feed)

#english/business
@app.route('/en/business')
def en_business():
    rss_urls= ['https://rss.app/feeds/_qW5dbRC4dgpHTiLx.xml','https://www.news18.com/rss/business.xml']

    combined_feed = combine_feeds(rss_urls, num_posts=10)
    return render_template('en-business.html', data=combined_feed)

#english/india
@app.route('/en/india')
def en_india():
    rss_urls = ['https://www.news18.com/rss/india.xml','https://timesofindia.indiatimes.com/rssfeeds/-2128936835.cms']
    combined_feed = combine_feeds(rss_urls, num_posts=13)
    return render_template('en-india.html', data=combined_feed)

#english/sports
@app.route('/en/sports')
def en_sports():
    rss_urls = ['https://rss.app/feeds/_4sHQgiWYauLwKwDK.xml','https://www.news18.com/rss/sports.xml','https://timesofindia.indiatimes.com/rssfeeds/4719148.cms']
    combined_feed = combine_feeds(rss_urls, num_posts=10)
    return render_template('en-sports.html', data=combined_feed)

#english/world
@app.route('/en/world')
def en_world():
    rss_urls = ['https://rss.app/feeds/_svhtCCTGal4YzXVz.xml','https://www.news18.com/rss/world.xml','http://timesofindia.indiatimes.com/rssfeeds/296589292.cms']
    combined_feed = combine_feeds(rss_urls, num_posts=10)
    return render_template('en-world.html', data=combined_feed)

#english/politics
@app.route('/en/politics')
def en_politics():
    rss_urls = ['https://rss.app/feeds/_zLguN8Y4JZDLnvS3.xml','https://www.news18.com/rss/politics.xml','http://timesofindia.indiatimes.com/rssfeeds/296589292.cms']
    combined_feed = combine_feeds(rss_urls, num_posts=10)
    return render_template('en-politics.html', data=combined_feed)

# tamil home
@app.route('/tamil')
def tamil_home():
    rss_urls = ['https://rss.app/feeds/_e8ITHRwacULSBlOw.xml']
    feed_data = combine_feeds(rss_urls, num_posts=10)
    return render_template('tm.html', data=feed_data)

@app.route('/tamil/top')
def tamil_top():
    rss_urls = ['https://rss.app/feeds/_e8ITHRwacULSBlOw.xml']
    feed_data = combine_feeds(rss_urls, num_posts=25)
    return render_template('tm-top.html', data=feed_data)
 
@app.route('/tamil/india')
def tamil_india():
    rss_urls = ['https://feeds.feedburner.com/Hindu_Tamil_india.xml']
    feed_data = tamil_feeds(rss_urls, num_posts=25)
    return render_template('tm-india.html', data=feed_data)


# http://feeds.feedburner.com/Hindu_Tamil_business
@app.route('/tamil/business')
def tamil_business():
    # rss_urls = [' http://feeds.feedburner.com/Hindu_Tamil_business.xml','https://rss.app/feeds/_q41GWepEG8mNeHJ6.xml']
    rss_urls = ['https://rss.app/feeds/_q41GWepEG8mNeHJ6.xml']
    feed_data = combine_feeds(rss_urls, num_posts=25)
    return render_template('tm-business.html', data=feed_data)


@app.route('/tamil/sports')
def tamil_sports():
    # rss_urls = ['http://feeds.feedburner.com/Hindu_Tamil_sports.xml','https://rss.app/feeds/_k2rqiIeSPSyaOO6Q.xml']
    rss_urls = ['https://rss.app/feeds/_k2rqiIeSPSyaOO6Q.xml']
    feed_data = combine_feeds(rss_urls, num_posts=25)
    return render_template('tm-sports.html', data=feed_data)


# http://feeds.feedburner.com/Hindu_Tamil_world

@app.route('/tamil/world')
def tamil_world():
    # rss_urls = ['http://feeds.feedburner.com/Hindu_Tamil_world.xml']
    rss_urls = ['https://rss.app/feeds/_MdfoYWnwjAxKbABX.xml']
    feed_data = combine_feeds(rss_urls, num_posts=25)
    return render_template('tm-world.html', data=feed_data)


@app.route('/tamil/tech')
def tamil_tech():
    # rss_urls = ['https://feeds.feedburner.com/Hindu_Tamil_technology.xml']
    rss_urls = ['https://rss.app/feeds/_ZeQaG5gCo2OeTdZi.xml']
    feed_data = combine_feeds(rss_urls, num_posts=25)
    return render_template('tm-tech.html', data=feed_data)


# ---------------------------------------tamil entertainment-------------------------------------
@app.route('/tamil/entertainment')
def tamil_cinema():
    rss_urls = ['http://feeds.feedburner.com/Hindu_Tamil_cinema.xml','https://rss.app/feeds/_p0h70aFAPUUGKRSK.xml']
    feed_data = combine_feeds(rss_urls, num_posts=15)
    return render_template('tm-cinema.html', data=feed_data)


# ---------------------------------------tamil politics-------------------------------------

@app.route('/tamil/politics')
def tm_politics():
    rss_urls = ['https://rss.app/feeds/_PmtcEvLWGCljeeTv.xml']
    feed_data = combine_feeds(rss_urls, num_posts=25)
    return render_template('tm-politics.html', data=feed_data)


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/terms-and-conditions')
def tnc():
    return render_template('tnc.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')
    
@app.route('/robots.txt')
def robots():
    return render_template('robots.txt')

    
last_modification_times = {}

def get_current_time():
    return datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")

@app.route("/sitemap")
@app.route("/sitemap/")
@app.route("/sitemap.xml")
def sitemap():
    host_components = urlparse(request.host_url)
    host_base = host_components.scheme + "://" + host_components.netloc

    static_urls = [
        {"loc": f"{host_base}/terms-and-conditions"},
        {"loc": f"{host_base}/about"},
        {"loc": f"{host_base}/privacy"},
    ]

    # Dynamic routes with dynamic content
    dynamic_urls = []
    d_urls = [
        f"{host_base}/",
        f"{host_base}/en",
        f"{host_base}/en/sports",
        f"{host_base}/en/entertainment",
        f"{host_base}/en/top",
        f"{host_base}/en/politics",
        f"{host_base}/en/world",
        f"{host_base}/en/business",
        f"{host_base}/en/technology",

        f"{host_base}/tamil",
        f"{host_base}/tamil/sports",
        f"{host_base}/tamil/entertainment",
        f"{host_base}/tamil/top",
        f"{host_base}/tamil/politics",
        f"{host_base}/tamil/world",
        f"{host_base}/tamil/business",
        f"{host_base}/tamil/technology",
        # Add other dynamic URLs here
    ]

    for url in d_urls:
        # Check if the URL exists in the last_modification_times dictionary
        if url in last_modification_times:
            # Check if it's time to update the last modification time (15 minutes)
            if datetime.now() - last_modification_times[url] >= timedelta(minutes=15):
                last_modification_times[url] = datetime.now()
        else:
            # If the URL doesn't exist in the dictionary, add it with the current time
            last_modification_times[url] = datetime.now()

        url_entry = {
            "loc": url,
            "lastmod": last_modification_times[url].strftime("%Y-%m-%dT%H:%M:%SZ"),
            "priority": "0.9",
        }
        dynamic_urls.append(url_entry)

    xml_sitemap = render_template("sitemap.xml", static_urls=static_urls, dynamic_urls=dynamic_urls)
    response = make_response(xml_sitemap)
    response.headers["Content-Type"] = "application/xml"

    return response
    

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')
    
@app.route("/google8815b0e15504e06d.html")
def google_site_verf():
    return render_template("google8815b0e15504e06d.html")

@app.route('/ads.txt')
def ads_txt():
    return render_template('ads.txt')
    

if __name__ == "__main__":
    app.run()
