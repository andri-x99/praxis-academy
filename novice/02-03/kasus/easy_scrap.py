import requests
import re

data = requests.get('http://teknikelektromercubuana22.blogspot.com/2013/04/daftar-alamat-email-dan-nomor-telepon.html')

phones = re.findall(r'(\(?[0-9]{3}\)?(?:\-|\s|\.)?[0-9]{3}(?:\-|\.)[0-9]{4})', data.text)
emails = re.findall(r'([\d\w\.]+@[\d\w\.\-]+\.\w+)',data.text)

print(phones,emails)

# you must try scraping in this videos, very easy! there are many python programming like how raw data processes with python
# https://www.youtube.com/watch?v=F1kZ39SvuGE