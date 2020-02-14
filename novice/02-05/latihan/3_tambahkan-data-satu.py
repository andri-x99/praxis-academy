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

# buat_data = """insert into nama_guru (nama,mapel,umur)
# values ("joko","ips",35)
# """
# cursor.execute(buat_data)
# db.commit()
# print("Buat data di nama_guru berhasil")

sql = "insert into nama_guru (nama,mapel) values(%s,%s)"
isi = ("Bo","B.Ing")
cursor.execute(sql,isi)
db.commit()

print("{} data ditambahkan".format(cursor.rowcount))