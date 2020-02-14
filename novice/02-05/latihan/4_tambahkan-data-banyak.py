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

sql = "insert into nama_guru (nomor,nama,mapel,umur) values(%s,%s,%s,%s)"
isi = [
    ("1","Yaha","Sejarah","54"),
    ("2","Yehe","Sejarah","46"),
    ("3","Yihi","Sejarah","31"),
    ("4","Yoho","Sejarah","45")
    # ("Yuhu","Sejarah","28")
]

for value in isi:
    cursor.execute(sql,value)
    db.commit()

print("{} data ditambahkan".format(len(isi)))