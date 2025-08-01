from .person import Person

class Student(Person):
    def __init__(self, name, student_id, marks):
        super().__init__(name, student_id)
        self._marks = marks

    def total(self):
        return sum(self._marks.values())
    
    def grade(self):
        avg = self.total() / len(self._marks)
        if avg >= 90:
            return 'A'
        elif avg >= 80:
            return 'B'
        elif avg >= 70:
            return 'C'
        elif avg >= 60:
            return 'D'
        else:
            return 'F'
        
    def to_dict(self):
        return {
            "name": self.name,
            "student_id": self.student_id,
            "marks": self._marks,
            "total": self.total(),
            "grade": self.grade()
        }