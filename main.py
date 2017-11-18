import requests
from bs4 import BeautifulSoup

def get_release_urls():
    page = requests.get('https://www.bungie.net/en/Explore/Category?category=Updates').text
    soup = BeautifulSoup(page, 'html.parser')
    cards = soup.find_all('a', { 'class': 'two-line-card-item' }, href=True)
    output = []
    for card in cards:
        output.append('https://www.bungie.net' + card['href'])
    return output

def get_release_notes(url):
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')
    update_content = soup.find('div', { 'class': 'content text-content' })
    titles = update_content.find_all('b')
    # notes = update_content.find_all('ul')
    for title in titles:
       print(title)
       print()
       print(title.parent.next_sibling)
       print()


if __name__ == "__main__":
    #get_release_urls()
    get_release_notes('https://www.bungie.net/en/Explore/Detail/Update/46352')
