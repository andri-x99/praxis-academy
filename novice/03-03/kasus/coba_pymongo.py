import pymongo
from flask import Flask, render_template, request, url_for
from werkzeug.utils import secure_filename


# db = pymongo.MongoClient("mongodb://localhost:27017/")
# # database
# database = db["tabel1"]
# # collection
# namatabel = database['tabel1']
# kebetulan sama nama database dan collectionnya
# karena sebenarnya collection itu adalah suatu tabel


app = Flask(__name__)

@app.route("/")
def home():
  db = pymongo.MongoClient("mongodb://localhost:27017/")
  database = db["tabel1"]
  namatabel = database['tabel1']
  data = []
  for i in namatabel.find():
    data.append(i)
  
  nama = 'halo'
  return render_template('tampilan_coba_pymongo.html', data=data, datanama=nama, angka=2)

@app.route("/about")
def about():
  return render_template('tampilan_coba_pymongo.html')
  
    
@app.route("/contact")
def contact():
  return render_template('tampilan_coba_pymongo.html')
  
    
  



# import pymongo

# db = pymongo.MongoClient("mongodb://localhost:27017/")

# database = db["tabel1"]
# namatabel = database['tabel1']

# data = [
#     { "judul": "Tutorial perulangan di Python", "penulis": "Hamami" },
#     { "judul": "Tutorial percabangan di Python", "penulis": "Hamami" },
#     { "judul": "Memahami konsep NoSQL", "penulis": "Ina" },
#     { "judul": "Instalasi NoSQL di Ubuntu", "penulis": "Ina" }
# ]

# namatabel.insert_many(data)

# -------------------------------------------------------------------------------------------------------------
# import pymongo

# db = pymongo.MongoClient("mongodb://localhost:27017/")

# database = db["tabel1"]
# namatabel = database['tabel1']


# nilai_lama = { "judul": "belajar ngoding python-mongodb" }
# nilai_baru = { "$set": { "judul": "belajar ngoding kolaborasi python & mongodb" } }

# namatabel.update_one(nilai_lama, nilai_baru)
# -------------------------------------------------------------------------------------------------------------
# import pymongo

# db = pymongo.MongoClient("mongodb://localhost:27017/")

# database = db["tabel1"]
# namatabel = database['tabel1']

# for tabel1 in namatabel.find():
#   print(tabel1)

# -------------------------------------------------------------------------------------------------------------
# import pymongo

# db = pymongo.MongoClient("mongodb://localhost:27017/")

# database = db["tabel1"]
# namatabel = database['tabel1']

# nilai = { "judul": "Instalasi NoSQL di Ubuntu" }

# namatabel.delete_one(nilai)

# -------------------------------------------------------------------------------------------------------------
# import pymongo

# db = pymongo.MongoClient("mongodb://localhost:27017/")

# database = db["tabel1"]
# namatabel = database['tabel1']

# nilai = { "penulis": "Hamami" }

# namatabel.delete_many(nilai)

# root@aa:~# mkdir /data/db -p (biar ada penampungan databasenya)
# root@aa:~# mongo

# terminal 1 : mongod / mongo
# terminal 2 : mongo --port 27017
# terkadang tuh folder databasenya ilang coba, buat lagi aja