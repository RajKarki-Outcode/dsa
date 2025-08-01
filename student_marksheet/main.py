from services.marksheet_manager import MarksheetManager
from services.file_handler import FileHandler
from services.logger import setup_logger

logger = setup_logger()
manager = MarksheetManager()

student = manager.add_student("Haz", "S001", {"Python": 95, "Math": 90, "English": 88})
logger.info(f"Added student: {student.name}")

data = manager.list_students()
FileHandler.save_csv('student_marksheet/data/students.csv', data)
FileHandler.save_json('student_marksheet/data/students.json', data)