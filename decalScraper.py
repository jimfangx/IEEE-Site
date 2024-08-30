from bs4 import BeautifulSoup
import requests
import os

url = "https://ieee.berkeley.edu/micromouse/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

for link in soup.find_all('a'):
    print(link.get('href'))
