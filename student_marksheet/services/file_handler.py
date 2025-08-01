import csv, json

class FileHandler:
    @staticmethod
    def save_csv(filepath, students):
        keys = ['name', 'id', 'total', 'grade'] + list(students[0]['marks'].keys())
        with open(filepath, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=keys)
            writer.writeheader()
            for student in students:
                row = {
                    'name': student['name'],
                    'id': student['id'],
                    'total': student['total'],
                    'grade': student['grade'],
                    **student['marks']
                }
                writer.writerow(row)
    @staticmethod
    def save_json(filepath, students):
        with open(filepath, 'w') as file:
            json.dump(students, file, indent=2)