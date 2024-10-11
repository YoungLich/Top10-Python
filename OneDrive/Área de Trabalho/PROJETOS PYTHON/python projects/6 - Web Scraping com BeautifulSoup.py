import requests
from bs4 import BeautifulSoup

url = "https://site_de_noticias.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

titulos = soup.find_all('h2')

for titulo in titulos:
    print(titulo.get_text())
