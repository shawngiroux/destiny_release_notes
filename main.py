import requests
import html2text
from bs4 import BeautifulSoup


class Article:
    url = ''
    title = ''
    text = ''

    def __init__(self, url):
        self.url = url
        page = requests.get(url).text
        soup = BeautifulSoup(page, 'html.parser')
        article = soup.find('div', { 'id': 'article-container' })
        self.title = article.find('h1', { 'class': 'section-header' }).get_text().strip()
        content = article.find('div', { 'class': 'text-content' })
        for b in content.find_all('b'):
            b.unwrap()
        for big in content.find_all('big'):
            big.unwrap()
        for bq in content.find_all('blockquote'):
            bq.unwrap()
        self.text = ''.join(str(content).split('\n')[1:-1])

    def markdown(self):
        ret = '**' + self.title + '**\n\n'
        ret += html2text.html2text(self.text)
        return ret


def get_urls():
    page = requests.get('https://www.bungie.net/en/Explore/Category?category=Updates').text
    soup = BeautifulSoup(page, 'html.parser')
    cards = soup.find_all('a', { 'class': 'two-line-card-item' }, href=True)
    output = []
    for card in cards:
        output.append('https://www.bungie.net' + card['href'])
    return output


if __name__ == "__main__":
    urls = get_urls()
    article = Article(urls[2])
    print(article.markdown())
