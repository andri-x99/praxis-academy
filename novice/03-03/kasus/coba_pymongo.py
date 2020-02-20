import pymongo

db = pymongo.MongoClient("mongodb://localhost:27017/")

# database
dbku = db["blog"]
# collection
collectionku = dbku['artikel']

# data yang akan diinsert
data = { "judul": "belajar ngoding python-mongodb", "penulis": "Faqih" }

# data diinsert
collectionku.insert_one(data)

import pymongo

db = pymongo.MongoClient("mongodb://localhost:27017/")

dbku = db["blog"]
collectionku = dbku['artikel']

data = [
    { "judul": "Tutorial perulangan di Python", "penulis": "Hamami" },
    { "judul": "Tutorial percabangan di Python", "penulis": "Hamami" },
    { "judul": "Memahami konsep NoSQL", "penulis": "Ina" },
    { "judul": "Instalasi NoSQL di Ubuntu", "penulis": "Ina" }
]

collectionku.insert_many(data)

import pymongo

db = pymongo.MongoClient("mongodb://localhost:27017/")

dbku = db["blog"]
collectionku = dbku['artikel']


nilai_lama = { "judul": "belajar ngoding python-mongodb" }
nilai_baru = { "$set": { "judul": "belajar ngoding kolaborasi python & mongodb" } }

collectionku.update_one(nilai_lama, nilai_baru)


import pymongo

db = pymongo.MongoClient("mongodb://localhost:27017/")

dbku = db["blog"]
collectionku = dbku['artikel']

for artikel in collectionku.find():
  print(artikel)

import pymongo

db = pymongo.MongoClient("mongodb://localhost:27017/")

dbku = db["blog"]
collectionku = dbku['artikel']

nilai = { "judul": "Instalasi NoSQL di Ubuntu" }

collectionku.delete_one(nilai)

import pymongo

db = pymongo.MongoClient("mongodb://localhost:27017/")

dbku = db["blog"]
collectionku = dbku['artikel']

nilai = { "penulis": "Hamami" }

collectionku.delete_many(nilai)

root@aa:~# mkdir /data/db -p (biar ada penampungan databasenya)
root@aa:~# mongo

terminal 1 : mongod / mongo
terminal 2 : mongo --port 27017
terkadang tuh folder databasenya ilang coba, buat lagi aja