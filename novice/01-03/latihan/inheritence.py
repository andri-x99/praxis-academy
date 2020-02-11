class SchoolMember:
    '''Represents any school member.'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Initialized SchoolMember: {})'.format(self.name))
   
    # membuat suatu function inisialisasi yang didalamnya terdapat 2 objek, 1 objek bernama init memang harus ada karena akan menunjuk ke kelas SchoolMember
    # sedangkan name dan age sendiri adalah variabel pribadi dari si init
    # dan ketika dipanggilpun diawali dengan self, itu karena menerangkan bahwa objek schoolmember itu punya nama serta punya umur


    def tell(self):
        '''Tell my details.'''
        print('Name:"{}" Age:"{}"'.format(self.name, self.age), end=" ")
    # tell sendiri memiliki kegunaan, ketika semua data telah di masukkan, maka tell merekan setiap data yang dimasukkan
    # ada library format bertujuan untuk menyisipkan self.name dan self.age ke kurung kurawalnya

class Teacher(SchoolMember):
    # ini menunjukkan bahwa Teacher adalah bagian dari SchoolMember
    '''Represents a teacher.'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Initialized Teacher: {})'.format(self.name))
    # init disini memiliki turunan dari school, yaitu name dan age, karena sifat turunan bisa berbeda juga, tidak masalah menambahkan salary pada Teacher
    # memanggil kelas school yang bertujuan meringkas code juga
    # karena, salary belum ada pada schoolmember maka dibuatlah salary sendiri

    def tell(self):
        SchoolMember.tell(self)
        print('Salary: "{:d}"'.format(self.salary))
    # tell sendiri memiliki kegunaan, ketika semua data telah di masukkan, maka tell merekan setiap data yang dimasukkan
    # ada format, buat menyisipkan nya ke salary, dan kurung kurawalnya ditambahi :d karena penyisipannya angka

class Student(SchoolMember):
    '''Represents a student.'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Initialized Student: {})'.format(self.name))
    # init disini memiliki turunan dari school, yaitu name dan age, karena sifat turunan bisa berbeda juga, tidak masalah menambahkan salary pada Teacher
    # memanggil kelas school yang bertujuan meringkas code juga
    # karena, salary belum ada pada schoolmember maka dibuatlah marks sendiri

    def tell(self):
        SchoolMember.tell(self)
        print('Marks: "{:d}"'.format(self.marks))
    # tell sendiri memiliki kegunaan, ketika semua data telah di masukkan, maka tell merekan setiap data yang dimasukkan
    # sama dengan salary, karena nilai bersifat integer jadinya

t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 25, 75)
# data guru dan murid yang diibaratkan t n s 

# prints a blank line
print()

members = [t, s]
# menyebutkan anggota

for member in members:
    # Works for both Teachers and Students
    member.tell()
# setiap anggota akan ditampilkan karena telah terekan datanya dengan tellN