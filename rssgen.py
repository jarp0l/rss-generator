from feedgen.feed import FeedGenerator


def generate_feed(feed_meta: dict, feed_data: list, **kwargs):
    filename = kwargs["output"] or "rss.xml"
    fg = FeedGenerator()
    fg.title(feed_meta["title"])
    fg.description(feed_meta["description"])
    fg.link(href=feed_meta["link"])
    fg.webMaster(feed_meta["webmaster"])

    for data in feed_data:
        fe = fg.add_entry()
        fe.title(data["title"])
        fe.link(href=data["link"])
        fe.published(data["published_date"])
        fe.description(data["description"])

    fg.rss_str(pretty=True)
    fg.rss_file(filename)
