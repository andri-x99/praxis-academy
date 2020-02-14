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

sql = "delete from nama_guru where nomor=%s"
isi = (4,)

cursor.execute(sql,isi)
db.commit()

print("{} data dihapus".format(cursor.rowcount))
