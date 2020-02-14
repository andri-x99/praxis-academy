import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Andri../..-99"
)

if db.is_connected():
    print("Berhasil terhubung ke db")
else:
    print("gagal")

cursor = db.cursor()
cursor.execute("drop database nama_guru")

print("Database telah dihapus!")