import requests
import csv
import urllib3
from bs4 import BeautifulSoup

f = csv.writer(open('coba_bhinneka.csv', 'w'))
f.writerow(['title', 'company' , 'location'])

URL = 'https://www.monster.com/jobs/search/?page=2'
halaman = requests.get(URL)

soup = BeautifulSoup(halaman.content,'html.parser')

# coba_kelas = soup.find_all('div',class_='company') #bisa terambil tanpa prettify
# print(coba_kelas)

''' mau pakai perulangan'''

pekerjaan = soup.find_all('section', class_='card-content')

pekerjaan2 = soup.find_all('h2',string=lambda text: 'Therapist' in text )

''' dibawah ini bisa menampilkan semua dan jenis kelas yang dicari'''
''' strip itu memiliki fungsi untuk membersihkan space yang berlebihan dan jika tidak ada ini hanya [] yang tertampil'''

for pekerjaan in pekerjaan:
    title   = pekerjaan.find('h2',class_='title')
    company = pekerjaan.find('div',class_='company')
    location= pekerjaan.find('div',class_='location')
    if None in (title,company,location):
        continue
    print(title.text.strip())
    print(company.text.strip())
    print(location.text.strip())
    print()
'''mulai dari sini kemudian ke atas yang di eksport ke .csv, yang dibawahnya belum'''
    f.writerow([title, company , location])
''' sedangkan ini hanya menampilkan berapa jumlah text dalam web tersebut'''
print(len(pekerjaan2))

''' menambahkan link pekerjaan terkait text dalam pekerjaan2'''
for situs in pekerjaan2:
    link = situs.find('a')['href']
    print(situs.text.strip())
    print(f"Lamarlah Kesini : {link}\n")

# https://realpython.com/beautiful-soup-web-scraper-python/
# https://www.monster.com/jobs/search/?page=2&jobid=e84b3145-aef1-47ad-96b0-c9c83cedb8e0