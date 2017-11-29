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
    data = []
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')
    update_content = soup.find('div', { 'class': 'content text-content' })
    titles = update_content.find_all(['b','ul'])

    for title in titles:
        if title != None:
            if title.name == 'ul' and title.parent.name == 'div':
                for li in title:
                    if li.text != None:
                        # print('\t∙' + li.text)
                        data.append('\n\t∙' + li.text)
            elif title.name == 'b':
                if title.string != None:
                    # print('\n**' + title.string + '**')
                    data.append('\n**' + title.string + '**')
    # print(update_content)
    data_str = ""
    for line in data:
        if line != None:
            data_str += ''.join(str(line))
    return data_str

if __name__ == "__main__":
    #get_release_urls()
    notes = get_release_notes('https://www.bungie.net/en/Explore/Detail/Update/46472')
    # notes = get_release_notes('https://www.bungie.net/en/Explore/Detail/Update/46437')
    # notes = get_release_notes('https://www.bungie.net/en/Explore/Detail/Update/46352')
    print(len(notes))