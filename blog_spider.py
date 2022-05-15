import requests
from bs4 import BeautifulSoup

urls = [
    f"https://www.cnblogs.com/#p{page}"
    for page in range(1, 51)
]


def craw(url):
    r = requests.get(url)
    # return html
    return r.text


def parse(html):
    soup = BeautifulSoup(html, "html.parser")
    # find all links and titles
    links = soup.find_all("a", class_="post-item-title")
    return [(link["href"], link.get_text())for link in links]


if __name__ == "__main__":
    for res in parse(craw(urls[0])):
        # ('https://www.cnblogs.com/dragonir/p/16265984.html', '使用CSS实现《声生不息》节目Logo')
        print(res)

