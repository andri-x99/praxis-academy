import unittest
from kasus01inheritance import SchoolMember
from kasus01inheritance import Teacher
from kasus01inheritance import Student


class TestSchoolMember(unittest.TestCase):
    
    def test_name(self):
        sc_1 = Teacher('Budi',35,500000)
        self.assertEqual(sc_1.name,'Budi')
    def test_age(self):
        sc_1 = Teacher('Budi',35,500000)
        self.assertEqual(sc_1.age,35)
    def test_salary(self):
        sc_1 = Teacher('Budi',35,500000)
        self.assertEqual(sc_1.salary,500000)
    def test_marks(self):
        sc_2 = Student('Anton',17,90)
        self.assertEqual(sc_2.marks)

if __name__ == '__main__':
    unittest.main()

#youtube.com/watch?v=6tNS--WetLI | Corey Schafer