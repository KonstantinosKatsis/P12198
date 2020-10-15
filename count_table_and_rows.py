import requests
from bs4 import BeautifulSoup

url = input("Enter URL to count number of tables and their rows: ")

request=requests.get(url)
soup=BeautifulSoup(request.text, "html.parser")

table = soup.findAll('table')

print('Number of tables: ' +str(len(table)))

for tbl in range(len(table)):
  rows = table[tbl].find_all('tr')
  print('Table ' + str(tbl + 1) + ' number of rows: ' + str(len(rows)))
