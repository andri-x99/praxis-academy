import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Andri../..-99",
    database="coba1"
)

if db.is_connected():
    print("Berhasil terhubung ke {}database")
else:
    print("gagal")

cursor = db.cursor()

sql = "update nama_guru set nama=%s, mapel=%s where nomor=%s"
isi = ("Jian Aody","SSD",6)

cursor.execute(sql,isi)
db.commit()

print("{} data diubah".format(cursor.rowcount))
