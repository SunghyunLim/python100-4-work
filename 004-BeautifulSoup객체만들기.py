import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Seoul_Metropolitan_Subway"
resp = requests.get(url)
html_src = resp.text

soup = BeautifulSoup(html_src, 'html.parser')
print(type(soup))
print('\n')

print(soup.head)
print('\n')
print(soup.body)
print('\n') 

print('title 테그요소:', soup.title)
print('title 테그이름:', soup.title.name)
print('title 테그문자열:', soup.title.string)