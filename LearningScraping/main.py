import requests
from bs4 import BeautifulSoup

URL ="https://realpython.github.io/fake-jobs/"
URLforbes = "https://www.forbes.com/profile/william-ackman/?sh=673a17d0298d"
page = requests.get(URL)

# print(page.text)
soup = BeautifulSoup(page.content, "html.parser")
print(soup.prettify)

# finding information using the tags
tags = soup.find_all('h2')
print(tags)

# extracting only the information not the complete tag easy done.
for tag in tags:
    print(tag.text)


    # soup.find_all('div', class_='card')

