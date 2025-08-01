import unittest
from models.student import Student

class TestStudent(unittest.TestCase):
    def test_total_and_grade(self):
        s = Student("Test", "T001", {"Math": 80, "English": 70, "Python": 90})
        self.assertEqual(s.total(), 240)
        self.assertEqual(s.grade(), "B")

if __name__ == "__main__":
    unittest.main()