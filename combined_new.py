import feedparser
from bs4 import BeautifulSoup


# Function to fetch RSS feed data
def get_rss_feed_data(url, num_posts=10):
    feed = feedparser.parse(url)
    data = []
    counter = 0
    news_website_name = feed.feed.title 
    for entry in feed.entries:
        if counter >= num_posts:
            break
        title = entry.title
        pub_date = entry.published
        summary_html = entry.summary
        summary_text = BeautifulSoup(summary_html, 'html.parser').get_text()
        source_url = entry.link 
        image_url = ''
        if 'enclosures' in entry and len(entry.enclosures) > 0:
            image_url = entry.enclosures[0]['url']
        if 'media_content' in entry and len(entry.media_content) > 0:
            image_url = entry.media_content[0]['url']
        
        if 'content' in entry and 'encoded' in entry.content:
            content_html = entry.content.encoded
            image_start = content_html.find('<img src="') + len('<img src="')
            image_end = content_html.find('"', image_start)
            image_url = content_html[image_start:image_end]

        data.append({
            'title': title,
            'published_date': pub_date,
            'summary': summary_text,
            'image_url': image_url,
            'source_url' : source_url,
            'source_name' :  news_website_name
        })
        counter += 1
    return data

def combine_feeds(url_list, num_posts=20):
    combined_data = []
    for url in url_list:
        feed_data = get_rss_feed_data(url, num_posts)
        combined_data.extend(feed_data)
        # website_name, feed_data = get_rss_feed_data(url, num_posts)
        # combined_data.extend(feed_data)
    combined_data.sort(key=lambda x: x['published_date'], reverse=True)
    return combined_data






