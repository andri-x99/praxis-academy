class SchoolMember:
    '''Represents any school member.'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        #print('(Initialized SchoolMember: {})'.format(self.name))
    def tell(self):
        '''Tell my details.'''
        print('Name:"{}" Age:"{}"'.format(self.name, self.age), end=" ")
 
class Teacher(SchoolMember):
    '''Represents a teacher.'''#kemarin salah indentasi gara2 maju satu space
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        # super() / bisa diganti ke SchoolMember
        self.salary = salary
        self.balance= "keren"
        #print('(Initialized Teacher: {})'.format(self.name))
    def tampil (self):
        return "namanya {} umurnya{} gajinya {} style {}".format(self.name,self.age,self.salary,self.balance)
    def tell(self):
        SchoolMember.tell(self)
        print('Salary: "{:d}"'.format(self.salary))
  
class Student(SchoolMember):
    '''Represents a student.'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Initialized Student: {})'.format(self.name))

    
    def tell(self):
        SchoolMember.tell(self)
        print('Marks: "{:d}"'.format(self.marks))

t = Teacher('Mrs. Shrividya', 40, 30000)
# s = Student('Swaroop', 25, 75)
# # data guru dan murid yang diibaratkan t n s 

# # prints a blank line
print(t.tampil())

# members = [t, s]
# # menyebutkan anggota

# for member in members:
#     # Works for both Teachers and Students
#     member.tell()
# # setiap anggota akan ditampilkan karena telah terekan datanya dengan tellN