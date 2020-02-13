import requests
import csv
from bs4 import BeautifulSoup


# f = csv.writer(open('z-artist-names.csv', 'w'))
# f.writerow(['Name', 'Link'])


url = 'https://www.detik.com'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

print(soup)