class Dog:

    tricks = []             # mistaken use of a class variable

    def __init__(self, name):
        self.name = name
        # nanti bedanya, bawah ini tinggal kasih pagar aja
        self.tricks = [] #buat list kosong, biar ga numpuk
    def add_trick(self, trick):
        self.tricks.append(trick)
d=Dog('Zushi')
e=Dog('Shenryu')
d.add_trick('play')
e.add_trick('hidenseek')
print('ini contoh d.tricks')
print(d.tricks)
print('ini contoh e.tricks')
print(e.tricks)