use tabel1
'''db.tabel1.insert(
    [
        {
        "membership_id":"1",
        "full_names":"Janet Jones",
        "physical_address":"1st Street Plot No 4",
        "salutation_id":"2"
        },
        {
            "membership_id":"2",
            "full_names":"Robert Phil",
            "physical_address":"3rd Street 34",
            "salutation_id":"1"
        },
        {
            "membership_id":"3",
            "full_names":"Robert Phil",
            "physical_address":"5th Avenue",
            "salutation_id":"1"
        }
    ]
)
'''
Jadi kenapa mongo berbeda karena konsepnya unik :
1. Membuat database dengan "use" lihatnya dengan "show dbs"
2. Auto increment dan primary key dibuat otomatis
3. Collection itu sama dengan tabel
4. Makanya cocok jika dijadikan penyimpanan API, karena formatnya kalo dilihat sama dengan .json

Teknik :
1.  Melihat data
    db.tabel1.find()
    db.tabel1.find().pretty()
    db.tabel1.findOne()

2.  Menghapus data
    db.tabel1.remove({"_id":ObjectId("")} )

3.  Mengupdate data
    db.tabel1.update({"_id" : .....("")}, {"","",""})
    
4.  Menghapus collection
    db.tabel1.drop()
