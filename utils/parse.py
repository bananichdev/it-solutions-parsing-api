from bs4 import BeautifulSoup

from settings import HOST_URL


def get_sub_urls_list(homepage_html: str) -> list[str]:
    soup = BeautifulSoup(homepage_html, "lxml")
    a_tags_list = soup.find_all("a", class_="bulletinLink bull-item__self-link auto-shy", limit=10)

    return [HOST_URL + a_tag.get("href") for a_tag in a_tags_list]


def get_views_list(homepage_html: str) -> list[int]:
    soup = BeautifulSoup(homepage_html, "lxml")
    span_views_list = soup.find_all("span", class_="views nano-eye-text", limit=10)

    return [int(span.text) for span in span_views_list]


def get_ad_dict(ad_html: str) -> dict[str, str]:
    soup = BeautifulSoup(ad_html, "lxml")
    title = soup.find("span", class_="inplace auto-shy").text
    author = soup.find("div", class_="seller-summary-user").find("a").text

    return {"title": title, "author": author}
