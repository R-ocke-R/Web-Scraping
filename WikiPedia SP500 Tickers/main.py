import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"

#wikiPage = requests.get(url)

#Create a soup
# soup = BeautifulSoup(wikiPage.content, "html.parser")

# Symbols = soup.find('table')
# print(Symbols)


# you can do this via beautiful soup or try this:
import pandas as pd
sp_list = pd.read_html(url) 
# this brings back all the tables on the page and convert them to pandas dataframe.

sp_list_500 = sp_list[0]
print(sp_list_500.head())
