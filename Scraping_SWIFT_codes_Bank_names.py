import os
import bs4
import requests
import pandas as pd

PATH = os.path.join("C:\\","Users","frevert","Documents","py")

def table_to_df(table):
	return pd.DataFrame([[td.text for td in row.findAll('td')] for row in table.tbody.findAll('tr')])

def next_page(soup):
	return "http:" + soup.find('a', attrs={'rel':'next'}).get('href')

res = pd.DataFrame()
url = "http://bank-code.net/country/FRANCE-%28FR%29/"
counter = 0

while True:
	print(counter)
	page = requests.get(url)
	soup = bs4.BeautifulSoup(page.content, 'lxml')
	table = soup.find(name='table', attrs={'id':'tableID'})
	res = res.append(table_to_df(table))
	res.to_csv(os.path.join(PATH,"BIC","table.csv"), index=None, sep=';', encoding='iso-8859-1')
	url = next_page(soup)
	counter += 1