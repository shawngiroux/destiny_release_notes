import requests
from bs4 import BeautifulSoup

def get_urls():
    page = requests.get('https://www.bungie.net/en/Explore/Category?category=Updates').text
    soup = BeautifulSoup(page, 'html.parser')
    cards = soup.find_all('a', { 'class': 'two-line-card-item' }, href=True)
    output = []
    for card in cards:
        output.append('https://www.bungie.net' + card['href'])
    return output

if __name__ == "__main__":
    get_urls()
