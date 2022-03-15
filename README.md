# rss-generator
## Generate RSS feeds

We use the code in this repo to check if there is any update in IOE Examination Division's website and send new updates in a specific channel in the Discord server of our class.

## Steps:
1. Check for new updates in https://exam.ioe.edu.np every 3 hours.
    - [Line 54 in main.py](https://github.com/jarp0l/rss-generator/blob/main/main.py#L54)
    - [Line 12 in workflow file](https://github.com/jarp0l/rss-generator/blob/main/.github/workflows/main.yml#L12)

2. Construct RSS feed out of the data scraped from the website.
    - [Line 63 in main.py](https://github.com/jarp0l/rss-generator/blob/main/main.py#L63)

3. Send the feed to another website.
    - [Line 35 in workflow file](https://github.com/jarp0l/rss-generator/blob/main/.github/workflows/main.yml#L35)

4. Check the website with RSS monitoring bot in Discord and send any new updates in a channel.
