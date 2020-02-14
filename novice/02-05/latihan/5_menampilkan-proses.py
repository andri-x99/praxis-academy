import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Andri../..-99",
    database="coba1"
)

if db.is_connected():
    print("Berhasil terhubung ke {}"database)
else:
    print("gagal")

cursor = db.cursor()

sql = "select * from nama_guru"
cursor.execute(sql)

hasil = cursor.fetchall()

for data in hasil:
    print(data)
print(data)

# hasil2 = cursor.fetchmany()
# print(hasil2)