from models.student import Student

class MarksheetManager:
    def __init__(self):
        self.students = []

    def add_student(self, name, student_id, marks):
        student = Student(name, student_id, marks)
        self.students.append(student)
        return student
    
    def list_students(self):
        return [student.to_dict() for student in self.students]