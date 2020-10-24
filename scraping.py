import requests
from bs4 import BeautifulSoup


with open('/home/fabio/Projetos/git/hackerranck_python/tipo_peticao_judicial.html', 'r',  encoding='iso8859-1') as f:

    soup = BeautifulSoup(f.read(), 'html.parser')
    print(len(soup.find_all('td', class_='col2')))
    for td in soup.find_all('td', class_='col2'):
        print(td.getText().capitalize())
