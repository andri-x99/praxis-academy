#contoh ke 1 didefiniskan fungsinya, tidak asal buat
def add(a, b):
    return a + b

plus = add

print(plus(3, 4))

#contoh ke 2 menggunakan lambda agar terstruktur
(lambda a, b : a + b)(3, 4)

addition = (lambda a, b : a + b)(3, 4)
print(addition)

addition = (lambda a, b : a + b)
print(addition(3, 4))

#contoh ke 3 
authors = ['Octavia Butler', 'Isaac Asimov', 'Neal Stephenson', 'Margaret Atwood', 'Usula K Le Guin', 'Ray Bradbury']
sorted(authors, key=len)  # Returns list ordered by length of author name
sorted(authors, key=lambda name: name.split()[-1])  # Returns list ordered alphabetically by last name.
print(sorted(authors))

# contoh ke 4
val = [1, 2, 3, 4, 5, 6]

# Multiply every item by two
list(map(lambda x: x * 2, val)) # [2, 4, 6, 8, 10, 12]
# Take the factorial by multiplying the value so far to the next item
reduce(lambda: x, y= x * y, val, 1) # 1 * 1 * 2 * 3 * 4 * 5 * 6
