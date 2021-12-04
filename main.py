import bs4
import requests

import rssgen


def html_page_parser(html_page):
    soup = bs4.BeautifulSoup(html_page, "html5lib")
    table = soup.find("table", id="datatable")
    body_rows = table.tbody.find_all("tr")

    data = []
    for row in body_rows:
        cols = row.find_all("td")

        links = [col.find("a") for col in cols]
        downloadLink, previewLink = (
            link.get("href") for link in links if link
        )  # Remove None type values

        cols = [col.text.strip() for col in cols]
        data.append(
            [col for col in cols if col] + [downloadLink, previewLink]
        )  # Remove empty values

    return data


def prettify_data(data: list):
    prettified_data = []
    for item in data:
        s_no = item[0]
        title = item[1]
        date = item[2]
        link = item[3]
        download_link = item[3]
        preview_link = item[4]

        data_dict = {
            "title": f"{title}",
            "link": link,
            "published_date": f"{date} {s_no}:{s_no}:{s_no} UTC",
            "description": f"<h2>{title}</h2><br>Published Date: {date}<br>Download URL: {download_link}<br>Preview URL: {preview_link}",
        }
        prettified_data.append(data_dict)
    return prettified_data


def main():
    URL = "https://exam.ioe.edu.np"
    TITLE = "IOE Examination Control Division"
    DESCRIPTION = "Latest updates from Examination Control Division, IOE, TU"

    response = requests.get(URL)
    latest_data = html_page_parser(response.text)

    feed_meta = {
        "title": TITLE,
        "description": DESCRIPTION,
        "link": URL,
        "webmaster": "jarp0l@secret.fyi",
    }
    rssgen.generate_feed(feed_meta, prettify_data(latest_data), output="public/exam.xml")


if __name__ == "__main__":
    main()
