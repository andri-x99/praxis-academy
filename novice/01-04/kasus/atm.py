Saldo=300000
print("           ATM    ")
print("""
1)        Saldo
2)        Tarik Tunai
3)        Setor Tunai
4)        Keluar


""")
Option=int(input("Masukkan Pilihan: "))

if Option==1:
    print("Saldo  Rp ",Saldo)


if Option==2:
    print("Saldo  Rp  ",Saldo)
    Withdraw=float(input("Masukkan uang yang akan diambil Rp "))
    if Withdraw>0:
        forewardbalance=(Saldo-Withdraw)
        print("Saldo Sekarang  Rp ",forewardbalance)
    elif Withdraw>Saldo:
        print("Maaf, Saldo Anda tidak mencukupi")
    else:
        print("Tidak ada transaksi yang diproses")

if Option==3:
    print("Saldo Rp ",Saldo)
    Deposit=float(input("Masukkan Uang"))
    if Deposit>0:
        forewardbalance=(Saldo+Deposit)
        print("Saldo Sekarang Rp ",forewardbalance)
    else:
        print("Tidak ada transaksi yang diproses")


if Option==4:
    exit()

# http://pythonfiddle.com/atm-program-in-python/











