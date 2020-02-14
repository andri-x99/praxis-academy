import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Andri../..-99",
    database="coba1"
)

if db.is_connected():
    print("Berhasil terhubung ke db")
else:
    print("gagal")

cursor = db.cursor()

buat_table = """create table nama_guru (
    nomor int auto_increment primary key,
    nama varchar(150),
    mapel varchar(200),
    umur int
)
"""
cursor.execute(buat_table)
print("Buat tabel nama_guru telah dibuat")
