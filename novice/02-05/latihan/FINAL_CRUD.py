import mysql.connector
import os

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Andri../..-99",
    database = "coba1"
)

def datamasuk(db):
    nama = input("Masukkan nama : ")
    mapel = input("Masukkan mapel : ")
    umur = input("Masukkan umur : ")
    isi = (nama,mapel,umur)

    cursor = db.cursor()
    sql = "insert into nama_guru (nama, mapel, umur) values (%s, %s,%s)"
    
    cursor.execute(sql,isi)
    db.commit()
    print("{} data berhasil ditambahkan".format(cursor.rowcount))

def datatampil(db):
    cursor = db.cursor()
    sql = "select * from nama_guru"
    cursor.execute(sql)

    hasil = cursor.fetchall()

    if cursor.rowcount < 0:
        print("Tidak terdapat data")
    else:
        for data in hasil:
            print(data)
    
def dataupdate(db):
    cursor = db.cursor()
    datatampil(db)
    nomor = input("Nomor yang Anda pilih : ")
    nama  = input("Nama : ")
    mapel = input("Mata Pelajaran : ")
    umur  = input("Usia saat ini : ")

    sql = "update nama_guru set nama=%s,mapel=%s,umur=%s where nomor=%s"
    isi = (nama,mapel,umur,nomor)
    cursor.execute(sql,isi)
    db.commit()
    print("{} data berhasil diubah!".format(cursor.rowcount))

def datahapus(db):
    cursor = db.cursor()
    datatampil(db)
    nomor = input("Masukkan nomor yang akan dihapus : ")

    sql = "delete from nama_guru where nomor=%s"
    isi = (nomor,)

    cursor.execute(sql,isi)
    db.commit()
    print("{} data telah dihapus!".format(cursor.rowcount))

def datacari(db):
    cursor = db.cursor()
    x = input("Masukkan kata kunci : ")
    sql = "select * from nama_guru where nama like %s or mapel like %s or umur like %s"
    isi = ("%{}%".format(x),"%{}%".format(x),"%{}%".format(x))
    
    cursor.execute(sql,isi)
    hasil = cursor.fetchall()

    if cursor.rowcount < 0:
        print("Tidak ada data yang ditemukan!")
    else:
        for data in hasil:
            print(data)

# fungsi backend diatas telah dibuat

def menu(db):
    print("=== Python with MYSQL ===")
    print("1. Insert Data")
    print("2. Tampilkan Data")
    print("3. Update Data")
    print("4. Hapus Data")
    print("5. Cari Data")
    print("0. Keluar")
    print("------------------")
    menu = input("Pilih menu> ")

    #clear screen
    os.system("clear")

    if menu == "1":
        datamasuk(db)
    elif menu == "2":
        datatampil(db)
    elif menu == "3":
        dataupdate(db)
    elif menu == "4":
        datahapus(db)
    elif menu == "5":
        datacari(db)
    elif menu == "0":
        exit()
    else:
        print("Menu salah!")

# fungsi front end telah dibuat diatas

if __name__ == "__main__":
  while(True):
    menu(db)

# pemanggilan fungsi main